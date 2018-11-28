#include<bits/stdc++.h>
using namespace std;

long long t,tt=1,m,ans,i,j,n,a[1105],ma;

int main()
{
    cin>>t;
    while(t--)
    {
    	cin>>n;
    	ma=-1;
    	for(i=0;i<n;i++)
    	{
    		cin>>a[i];
    		ma = max(ma,a[i]);


    	}
    	ans = ma;
    	for(i=1;i<ma;i++)
    	{
    		m = i;
    		for(j=0;j<n;j++)
    		{
    		   if(a[j]>i)
    		   {
    		   if(a[j]%i==0){
    		   	m+=a[j]/i ;
    		   	m-=1;
    		   }
    		   else m += a[j]/i;
    		   }
    		}
    		ans = min(ans,m);
    	}

    	printf("Case #%lld: %lld\n",tt,ans);
    	tt++;
    }




}
