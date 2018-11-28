#include<functional>
#include<algorithm>
//#include<iostream>
#include<numeric>
#include<cassert>
#include<cstring>
#include<cstdio>
#include<vector>
#include<queue>
//#include<cmath>
#include<set>
#include<map>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef vector<LL> VLL;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,b,e) for(int i=(b);i<=(e);++i)
#define FORD(i,b,e) for(int i=(b);i>=(e);--i)
#define FOReach(it,V) for(__typeof((V).begin()) it=(V).begin();it!=(V).end();++it)

#define PB push_back
#define ALL(V) (V).begin(),(V).end()
#define SIZE(V) ((int)(V).size())

#define MP make_pair
#define ST first
#define ND second

#define DBG

#ifdef DBG
	#define debug(...) fprintf(stderr, __VA_ARGS__)
#else
	#define debug(...)
#endif

int stmp;
#define scanf stmp=scanf


const int MAX = 100000;
const int INF = 1000000001;

int n;
LL p;

bool win1(LL x) {
	LL l = x;
	LL pos = 0;
	REP(foo,n)
	{
		pos *= 2LL;
		if(l > 0) {
			--l;
			++pos;
			l /= 2;
		}
	}
	return pos < p;
}

LL solve1() {
	LL lo = 0, hi = 1LL<<n;
	while(lo + 1 < hi)
	{
		LL mid = (lo+hi)/2;
		if(win1(mid)) lo = mid;
		else hi = mid;
	}
	return lo;
}

bool win2(LL x) {
	LL w = (1LL<<n)-x-1;
	LL pos = 0;
	REP(foo,n)
	{
		pos *= 2LL;
		++pos;
		if(w > 0) {
			--w;
			--pos;
			w /= 2;
		}
	}
	return pos < p;
}

LL solve2() {
	LL lo = 0, hi = 1LL<<n;
	while(lo + 1 < hi)
	{
		LL mid = (lo+hi)/2;
		if(win2(mid)) lo = mid;
		else hi = mid;
	}
	return lo;
}

int main(int argc, char *argv[]) {
	int Z;
	scanf("%d", &Z);
	FOR(z,1,Z)
	{
		printf("Case #%d: ", z);
		scanf("%d %lld", &n, &p);
		printf("%lld %lld\n", solve1(), solve2());
	}
	return 0;
}

