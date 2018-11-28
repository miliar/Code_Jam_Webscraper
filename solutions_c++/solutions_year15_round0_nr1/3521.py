#include<bits/stdc++.h>

using namespace std;

#define ll long long 

int main()
{
	freopen("inp11.txt","r",stdin);
	freopen("out11.txt","w",stdout);
	ll t;
	cin>>t;
	for(ll j=1;j<=t;j++)
	{
		ll n;
		cin>>n;
		string s;
		cin>>s;
		ll count=s[0]-'0';
		ll ans=0;
		for(ll i=1;i<n+1;i++)
		{
			if(count<i)
			{
				ans+=(i-count);
				count+=(i-count);
			}
			count+=(s[i]-'0');
		}
		cout<<"Case #"<<j<<": "<<ans<<endl;
	}
	return 0;
}
