#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back

int main()
{
	freopen("ip.txt","r",stdin);
	freopen("op.txt","w",stdout);
	ll t,n,i,l,aud,ans,c;
	cin>>t;
	string s;
	c = 1;
	while(t--)
	{
		cin>>n>>s;
		l = n+1;
		aud = ans = 0;
		
		for(i=0;i<l;i++)
		{
			ans = min(ans,aud-i);
			aud+=(int(s[i]-48));
		}
		
		cout<<"Case #"<<c++<<": ";
		if(ans>=0)
		{
			cout<<0<<"\n";
		}
		else
		{
			cout<<(-1)*ans<<"\n";
		}
		
	}
    return 0;
}

