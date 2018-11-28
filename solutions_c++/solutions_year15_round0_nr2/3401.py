#include<bits/stdc++.h>

using namespace std;

#define ll long long 

int main()
{
	freopen("inp12.txt","r",stdin);
	freopen("out12.txt","w",stdout);
	ll t;
	cin>>t;
	for(ll j=1;j<=t;j++)
	{
		ll n;
		cin>>n;
		ll ar[n];
		for(int i=0;i<n;i++)
		cin>>ar[i];
		sort(ar,ar+n);
		int ans=1000000,ans1=0;
		for(int i=1;i<=1000;i++)
		{
			ans1=i;
			for(int k=n-1;k>=0;k--)
			{
				if(ar[k]%i==0)
				{
					ans1+=(ar[k]/i)-1;
				}
				else
				{
					ans1+=(ar[k]/i);
				}
			}
			if(ans>=ans1)
			ans=ans1;
			
		}
		cout<<"Case #"<<j<<": "<<ans<<endl;
	}
	return 0;
}
