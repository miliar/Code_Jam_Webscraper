#include<iostream>
#include<string.h>
#include<math.h>

using namespace std;
int main()
{
	int t,n,k,p,f,i,j,nl,l,arr[100][100],step[100],mean[100];
	char str[100][100],nstr[100][100];
	cin>>t;
	for(p=0;p<t;p++)
	{
		f=-1;
		cin>>n;
		for(i=0;i<n;i++)
	    {
	    	cin>>str[i];
	    	l=strlen(str[i]);
	    	nstr[i][0]=str[i][0];
	    	k=0;
	    	arr[i][0]=1;
	    	for(j=1;j<l;j++)
	    	{
	    		if(str[i][j]!=nstr[i][k])
	    		{
	    		 nstr[i][++k]=str[i][j];
	    		 arr[i][k]=1;
	    	    }
	    		else
	    		 arr[i][k]++;
	    	}
	    
	    	nstr[i][++k]='\0';
	    	if(i!=0)
	    	{
	    		if(strcmp(nstr[0],nstr[i]))
	    		{
	    			f=0;
	    		}
	    	}
	    	else
	    	 nl=k;
	    }
		if(f==0)
	    {
	    	cout<<"Case #"<<p+1<<": Fegla Won\n";
	    }
	    else
	    {
	    	for(i=0;i<nl;i++)
	    	{
	    		mean[i]=0;
	    		for(j=0;j<n;j++)
	    		{
	    			mean[i]+=arr[j][i];
	    		}
	    		mean[i]=mean[i]/n;
	    	}
	    
	    	step[p]=0;
	    	for(i=0;i<nl;i++)
	    	{
	    		for(j=0;j<n;j++)
	    		 step[p]+=fabs(mean[i]-arr[j][i]);
	    	}
	    	cout<<"Case #"<<p+1<<": "<<step[p]<<"\n";
	    }	    
	}
	return 0;
}
