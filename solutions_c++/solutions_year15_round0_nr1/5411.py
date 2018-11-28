#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
	freopen("input1.txt","r",stdin);
	freopen("output.txt","w",stdout);
	ll t;
	cin>>t;
	ll ca, i;
	for(ca=1;ca<=t;ca++)
	{
		ll x;
		string s;
		cin>>x>>s;
		x++;
		ll ans=0;
		ll khada=0;
		khada=(s[0]-'0');
		for(i=1;i<x;i++)
		{
			ll temp=0;
			if(s[i]=='0')
				continue;
			if(khada < i)
			{
				temp=(i-khada);
			}
			khada+=(s[i]-'0'+temp);
			ans+=temp;
			//cout<<khada<<"::"<<i<<"-->"<<ans<<"\n";
		}
		cout<<"Case #"<<ca<<": "<<ans<<"\n";
	}
	return 0;
}