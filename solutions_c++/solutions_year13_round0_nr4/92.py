#define _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <numeric>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>

using namespace std;

#define REP(i,n) for (int i=0,_n=(n); i < _n; i++)
#define REPD(i,n) for (int i=(n)-1; i >= 0; i--)
#define FOR(i,a,b) for (int _b=(b), i=(a); i <= _b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))

#define CLEAR(x) memset(x,0,sizeof x);
#define CLEARA(x) memset(&x,0,sizeof x);
#define FILL(x,v) memset(x,v,sizeof x);
#define FILLA(x,v) memset(&x,v,sizeof x);

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 0x7fffffff
#define X first
#define Y second
#define pb push_back
#define SZ(c) (int)(c).size()
#define MP make_pair
#define eps 1.0e-11
const double pi = acos(-1.0);

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;

#define FN "D-small-attempt0"
#define N 222
int n,k;
int need[N];
VI provide[N];
int have[N];
int nxt[1<<20];

bool go(int mask) {
	int& res = nxt[mask];
	if (res != -1) return res != -2;
	REP(i,n) if ((mask&(1<<i))==0 && have[need[i]]) {
		--have[need[i]];
		REP(j,SZ(provide[i]))
			++have[provide[i][j]];
		bool r = go(mask|(1<<i));
		REP(j,SZ(provide[i]))
			--have[provide[i][j]];
		++have[need[i]];
		if (r) {
			res = i;
			return true;
		}
	}
	res = -2;
	return false;
}

int main()
{
	freopen(FN ".in","r",stdin);
	freopen(FN ".out","w",stdout);

	int tests;
	scanf("%d",&tests);
	for (int test = 1; test<=tests; test++)
	{
		printf("Case #%d:",test);
		CLEAR(have);
		scanf("%d%d",&k,&n);
		REP(i,k)
		{
			int x;
			scanf("%d",&x);
			have[x]++;
		}
		REP(i,n)
		{
			int cnt;
			scanf("%d%d",need+i,&cnt);
			provide[i].resize(cnt);
			REP(j,cnt)
				scanf("%d",&provide[i][j]);
		}
		FILL(nxt,-1);
		nxt[(1<<n)-1]=0;
		bool r = go(0);
		if (!r)
			printf(" IMPOSSIBLE\n");
		else {
			for (int m = 0; m != (1<<n)-1; m |= 1<<nxt[m])
				printf(" %d",nxt[m]+1);
			printf("\n");
		}
	}
	return 0;
}