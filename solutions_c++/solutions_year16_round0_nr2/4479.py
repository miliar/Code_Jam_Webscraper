#include <bits/stdc++.h>
using namespace std;
#define ll long long
char s[105];
int main()
{
	ll t,n;
	scanf("%lld",&t);
	ll c=1;
	while(t--)
	{
		scanf("%s",s);
		n=strlen(s);
		ll ans=0;
		for(int i=0;i<n-1;i++)
		{
			if(s[i]!=s[i+1])
			{
				ans++;
			}
		}
		if(s[n-1]=='-')
			ans++;
		cout<<"Case #"<<c<<": "<<ans<<endl;
		c++;
	}
	return 0;
}