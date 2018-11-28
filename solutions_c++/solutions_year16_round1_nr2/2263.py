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

#define MAXN	(50)

int n, m;
VI arr[2 * MAXN];
VI cannext[2 * MAXN];
int board[MAXN][MAXN];
bool used[2 * MAXN];
int ans[MAXN];

bool solve(int step, int idx) {
	//copy to board
	rep(i, n) {
		board[step][i] = arr[idx][i];
	}
	if (step + 1 == n) {//col missing
		int c = 0;
		int miss = 0;
		bool matched[MAXN] = {};//col matching
		
		rep(i, m)if (!used[i] && i != idx) {
			while (c < n && miss <= 1) {
				bool match = true;
				rep(r, n)if (board[r][c] != arr[i][r]) {
					match = false;
					break;
				}
				if (match) {
					matched[c] = true;
					++c;
					break;
				} else {
					++miss;
					++c;
				}
			}
		}
		if (miss <= 1 && count(matched, matched + n, false) == 1) {
			c = find(matched, matched + n, false) - matched;
			rep(r, n)ans[r] = board[r][c];
			
			return true;
		}
		return false;
	}
	//estimate this is possible
	//int cnt = 0;
	//for (int nidx : cannext[idx])if (!used[nidx])
	//	++cnt;
	//if (cnt + step < n - 1)
	//	return false;

	used[idx] = true;
	for (int nidx : cannext[idx])if (!used[nidx]) {
		if (solve(step + 1, nidx))
			return true;
	}
	used[idx] = false;
	return false;
}

bool comp(VI A, VI B) {
	rep(i, n)if (A[i] >= B[i])return false;
	return true;
}

int main()
{
	int degree[MAXN * 2];
	int longdist[2 * MAXN];
	VI canpre[2 * MAXN];

	int TC;
	scanf("%d", &TC);
	FOR(T, 1, TC)
	{
		//fprintf(stderr, "Case #%d:", T);

		scanf("%d", &n);
		m = 2 * n - 1;
		rep(i, m)arr[i].clear();
		rep(i, m)rep(j, n) {
			int k; scanf("%d", &k);
			arr[i].push_back(k);
		}
		//first sort all arr
		sort(arr, arr + m);

		rep(i, m) {
			cannext[i].clear();
			canpre[i].clear();
		}
		rep(i, m)rep(j, m)
			if (comp(arr[i], arr[j])) {
				cannext[i].push_back(j);
				canpre[j].push_back(i);
			}
		CLEAR(ans);
		rep(i, m) {
			CLEAR(used);
			if (solve(0, i))break;
		}
		printf("Case #%d:", T);
		rep(i, n)printf(" %d", ans[i]);
		puts("");
	}

	return 0;
}