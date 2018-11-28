#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
char str[100000];
int main()
{
	ll t;
	cin>>t;
	ll c=1;
	while(t--)
	{
		ll n;
		cin>>n;
		cin>>str;
		ll ans=0;
		ll co=str[0]-'0';
		for(ll i=1;i<=n;i++)
		{
			if(co<i)
			{
				ans+=i-co;
				co+=i-co;
				co+=str[i]-'0';
			}
			else
			{
				co+=str[i]-'0';
			}
		}
		cout<<"Case #"<<c<<": "<<ans<<endl;
		c++;
	}
	return 0;
}