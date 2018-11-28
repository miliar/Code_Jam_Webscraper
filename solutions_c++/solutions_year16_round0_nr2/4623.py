#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
	ll t;
	string s;
	cin>>t;
	for(ll i=1;i<=t;i++)
	{
		cin>>s;
		char r=s[0];
		
		ll ans=1;
		
		for(int j=1;j<s.length();j++)
		{
			if(r==s[j])
				continue;
			r=s[j];
			ans++;
		}
		if(s[s.length()-1]=='+')
		ans--;
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	
}