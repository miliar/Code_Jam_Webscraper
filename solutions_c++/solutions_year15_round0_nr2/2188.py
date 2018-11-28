#include <bits/stdc++.h>
using namespace std;
int main()
{
	long long a,b,c,d,i,j,l,sum,result,n,m,k,s,t,max1;
    a=0;
	scanf("%lld",&t);
	while(t--)
	{
		long long arr[1005]={0};
		scanf("%lld",&n);
        for(i=0;i<n;i++)
        {
        	scanf("%lld",&arr[i]);
        }
        sort(arr,arr+n);
        max1=0;
        for(i=0;i<n;i++)
        {
        	max1=max(max1,arr[i]);
        }
        long long mini=1004;
	    for(i=1;i<=max1;i++)
	    {
	    	s=0;
	        for(j=0;j<n;j++)
	        {
	        	if(arr[j]%i==0)
	        	{
	        		s+=((arr[j]/i)-1);
	        	}
	        	else
	        	{
	        		s+=(arr[j]/i);
	        	}
	        }
	        
	        s+=i;
	        
	        mini=min(mini,s);
	        
	    }
		printf("Case #%lld: %lld\n",++a,mini);
	}
	return 0;
}




