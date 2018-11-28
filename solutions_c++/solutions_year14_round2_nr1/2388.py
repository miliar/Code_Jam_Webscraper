#include<iostream>
#include<string.h>
#include<math.h>

using namespace std;
int main()
{
	int t,n,k,p,y,i,j,nl,l,arr[100][100],tram[100],mess[100];
	char s1[100][100],s2[100][100];
	cin>>t;
	for(p=0;p<t;p++)
	{
		y=-1;
		cin>>n;
		for(i=0;i<n;i++)
	    {
	    	cin>>s1[i];
	    	l=strlen(s1[i]);
	    	s2[i][0]=s1[i][0];
	    	k=0;
	    	arr[i][0]=1;
	    	for(j=1;j<l;j++)
	    	{
	    		if(s1[i][j]!=s2[i][k])
	    		{
	    		 s2[i][++k]=s1[i][j];
	    		 arr[i][k]=1;
	    	    }
	    		else
	    		 arr[i][k]++;
	    	}
	    
	    	s2[i][++k]='\0';
	    	if(i!=0)
	    	{
	    		if(strcmp(s2[0],s2[i]))
	    		{
	    			y=0;
	    		}
	    	}
	    	else
	    	 nl=k;
	    }
		if(y==0)
	    {
	    	cout<<"Case #"<<p+1<<": Fegla Won\n";
	    }
	    else
	    {
	    	i=-1;
	    	while(++i<nl)
	    	{
	    		mess[i]=0;
	    		j=-1;
	    		while(++j<n)
	    		{
	    			mess[i]+=arr[j][i];
	    		}
	    		mess[i]=mess[i]/n;
	    	}
	    
	    	tram[p]=0;
	    	i=-1;
	    	while(++i<nl)
	    	{
	    		j=-1;
	    		while(++j<n)
	    		 tram[p]=tram[p]+fabs(mess[i]-arr[j][i]);
	    	}
	    	cout<<"Case #"<<p+1<<": "<<tram[p]<<"\n";
	    }	    
	}
	return 0;
}
