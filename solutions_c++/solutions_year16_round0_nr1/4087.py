#include <cstdio>
#include <set>
using namespace std;

typedef long long LL;

int T;
LL N;

LL solve(LL n)////////////////////////////////////
{
	set<int> S;

	for(LL i=1; ;i++)
	{
		LL t = i*n;
		LL x = t;
		while(x)
		{
			int d = x%10;
			S.insert(d);
			if(S.size()==10)return t;

			x = x/10;
		}
	}
}

int main()////////////////////////////////////////
{
//	freopen("..\\A-small-attempt0.in","r",stdin);
//	freopen("..\\A-small-attempt0.out","w",stdout);

	freopen("..\\A-large.in","r",stdin);
	freopen("..\\A-large.out","w",stdout);

	scanf("%d",&T);
	for(int kase=1;kase<=T;kase++)
	{
		scanf("%lld",&N);
		printf("Case #%d: ",kase);

		if(N==0)printf("INSOMNIA\n");
		else printf("%lld\n",solve(N));
	}
	return 0;
}