#include<bits/stdc++.h>
#define ll long long int
#define MOD 1000000007
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out2.out","w",stdout);
	ll t,ans,n,x,i,d;
	scanf("%lld",&t);
	for(x=1;x<=t;++x)
	{
		scanf("%lld",&n);
		set<ll> s;
		ans=0;
		for(i=1;i<75;++i)
		{
			d=i*n;
			while(d!=0)
			{
				s.insert(d%10);
				d/=10;
			}
			if(s.size()==10)
			{
				ans=i*n;
				break;
			}
		}
		if(ans)
		printf("Case #%lld: %lld\n",x,ans);
		else
		printf("Case #%lld: INSOMNIA\n",x,ans);
	}
	return 0;
}
