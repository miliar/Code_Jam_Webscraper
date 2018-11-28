//Grzegorz Prusak
#include <cstdio>
#include <algorithm>
#include <vector>

#define REP(i,n) for(int i=0; i<(n); ++i)
#define FOR(i,p,k) for(int i=(p); i<=(k); ++i)

template<typename T> void checkmin(T &a, T b){ if(a>b) a = b; }

typedef long long LL;

LL sure(int n, LL p)
{
	LL res = 0;
	REP(k,n+1)
	{
		//printf("%lld - %lld <= %lld\n",1LL<<n,(1LL<<n-k)-1,p);
		if((1LL<<n)-((1LL<<n-k)-1)<=p) res = (1LL<<k+1)-1;
	}
	if(res>1LL<<n) res = 1LL<<n;
	return res;
}


int main()
{
	int t; scanf("%d",&t);
	FOR(_,1,t)
	{
		int n; LL p; scanf("%d%lld",&n,&p);	
		printf("Case #%d: %lld %lld\n",_,sure(n,p)-1,(1LL<<n)-1-sure(n,(1LL<<n)-p));
	}

	return 0;
}

