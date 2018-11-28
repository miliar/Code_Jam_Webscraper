#include<bits/stdc++.h>
#define ll long long int
#define MOD 1000000007
using namespace std;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out2.out","w",stdout);
	ll t,n,x,i,d;
	scanf("%lld",&t);
	for(x=1;x<=t;++x)
	{
		string s;
		cin>>s;
		n=s.length();
		d=1;
		for(i=1;i<n;++i)
		{
			if(s[i]!=s[i-1])
			d++;
		}
		if(s[n-1]=='+')
		d--;
		printf("Case #%lld: %lld\n",x,d);
	}
	return 0;
}
