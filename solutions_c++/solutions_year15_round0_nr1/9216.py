#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{

	ll t;
	cin>>t;
	for(ll j=1;j<=t;j++)
	{
	
		ll c;
		string s;
		cin>>c;
		cin>>s;
		ll k=s.length();
		ll ct=0;
		ll ans=0;
		
		for(ll i=0;i<s.length();i++)
		{
		   ll h=int(s[i])-48;
		   if(i>ct)
		   {
		   	ans=ans+i-ct;
		   	ct=i+h;
		   }
		   else
		   ct=ct+h;
		}
		cout<<"Case #"<<j<<": "<<ans<<endl;
		
	}
	return 0;
}
