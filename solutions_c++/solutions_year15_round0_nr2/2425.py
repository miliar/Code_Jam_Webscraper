#include<bits/stdc++.h>
using namespace std;
#define ll long long
ll a[1001];
int main()
{
	ll i,j,k,l,m,n,t;
	scanf("%lld",&t);
	k=1;
	while(t--)
	{
		scanf("%lld",&n);
		ll maxi=0;
        for(i=0;i<n;i++)
        {
        	scanf("%lld",&a[i]);
        	if(a[i]>maxi)
        	maxi=a[i];
        }
        m=maxi;
        //cout<<m<<endl;
        maxi=1001;
		for(j=1;j<=m;j++)
		{
           ll sum=0;
           for(i=0;i<n;i++)
           {
             if(a[i]%j==0)
             sum=sum+(a[i]/j)-1;
             else
             sum=sum+a[i]/j;    
           }
           sum=sum+j;
           if(sum<maxi)
           	maxi=sum;
		}
		cout<<"Case #"<<k<<": "<<maxi<<endl;
		k++;
	}
}
