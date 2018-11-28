//TAG : 
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cstring>
#include<cmath>
#include<vector>
#include<map>
#include<queue>
#include<set>
#include<algorithm>
#include<climits>
#include<functional>
#include<numeric>
using namespace std;
#define rep(i,n)	for(int (i)=0;(i)<(n);(i)++)
#define repd(i,n)	for(int (i)=(n)-1;(i)>=0;(i)--)
#define REP(i,j,n)  for(int (i)=(j),_n=(n); (i) < _n; (i)++)
#define FOR(i,a,b)  for(int _b=(b), (i)=(a); (i) <= _b; (i)++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define CLEAR(x) memset((x),0,sizeof(x))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define X first
#define Y second
#define MP make_pair
#define MT make_tuple
#define EPS 	(1e-9)
typedef pair<int, int>	PII;
typedef vector<int>		VI;
typedef unsigned int	uint;
typedef long long		LL;
typedef unsigned long long	ULL;
template<typename T> void check_max(T& a, T b) { if (a < b) a = b; }
template<typename T> void check_min(T& a, T b) { if (a > b) a = b; }
#ifdef _MSC_VER
#include "builtin_gcc_msvc.h"
#define gets	gets_s
#else
#define popcnt(x)	__builtin_popcount(x)
#define ctz(x)		__builtin_ctz(x)
#define clz(x)		__builtin_clz(x)
#define popcntll(x)	__builtin_popcountll(x)
#define ctzll(x)	__builtin_ctzll(x)
#define clzll(x)	__builtin_clzll(x)
#endif

#define MAXN	(1000)

int n;
int bff[MAXN + 1];
VI r_bff[MAXN + 1];
int ans;
bool visit[MAXN + 1];
bool incircle[MAXN + 1];
int circle[MAXN];

void solve(int step, int u) {
	if (incircle[u])return;
	incircle[u] = true;
	//visit[u] = true;
	circle[step] = u;
	if (step == 0) {
		solve(step + 1, bff[u]);
	} else {
		if (bff[u] == circle[step - 1] || bff[u] == circle[0]) {
			check_max(ans, step + 1);
		}
		if (circle[step - 1] == bff[u]) {//can choose anyone
			FOR(i, 1, n)if (!incircle[i]) {
				solve(step + 1, i);
			}
		} else {
			solve(step + 1, bff[u]);
		}
	}
	incircle[u] = false;
}

int main()
{
	int TC;
	scanf("%d", &TC);
	FOR(T, 1, TC)
	{
		scanf("%d", &n);
		FOR(i, 1, n)r_bff[i].clear();
		FOR(i, 1, n) {
			scanf("%d", &bff[i]);
			r_bff[bff[i]].push_back(i);
		}
		ans = 0;
		CLEAR(visit);
		FOR(i, 1, n)if (!visit[i]) {
			CLEAR(incircle);
			solve(0, i);
		}

		printf("Case #%d: %d\n", T, ans);
	}

	return 0;
}