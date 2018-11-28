#include<iostream>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<cstdio>
#include<vector>
#include<map>
using namespace std;
 
    
 
int main ()
{
	long long int t,i,n,x,y,ans,j,a,b,c,k=1,m;
	cin>>t;
	string str;
	while(t--)
	{
		long long int arr[1005]={};
		cin>>n;
		long long int max=0;


		for(i=0;i<n;i++)
		{
			cin>>arr[i];
			if(arr[i]>max)
			max=arr[i];
		}



		long long int min=max;
		


	    for(i=1;i<max;i++)
	    {
	    	ans=i;
	    	for(j=0;j<n;j++)
	    	{
	    		if(arr[j]>i)
	    		{
	    			if(arr[j]%i==0)
	    			   ans+=(arr[j]/i-1);
	    			else
	    				ans+=(arr[j]/i);
	    		}
	    	}
	    	if(ans<min)
	    	{
	    		min=ans;
	    	}
	    }

        
		cout<<"Case #"<<k<<": "<<min<<endl;
		k++;
	}
	return 0;
}