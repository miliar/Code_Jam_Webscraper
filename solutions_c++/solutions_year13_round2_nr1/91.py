#pragma comment(linker,"/STACK:64000000")
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <memory.h>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <cassert>
#include <time.h>
#include <bitset>

using namespace std;

#define mp make_pair
#define pb push_back
#define _(a,b) memset( (a), b, sizeof( a ) )
#define all(a) a.begin(), a.end()
#define sz(a) (int)a.size()
#ifdef WIN32
#define dbg(...) {fprintf(stderr, __VA_ARGS__); fflush(stderr);}
#define dbgx(x) {cerr << #x << " = " << x << endl;}
#define dbgv(v) {cerr << #v << " = {"; for (typeof(v.begin()) it = v.begin(); it != v.end(); it ++) cerr << *it << ", "; cerr << "}"; cerr << endl;}
#else
#define dbg(...) { }
#define dbgx(x) { }
#define dbgv(v) { }
#endif

typedef unsigned long long ull;
typedef long long lint;
typedef pair < int , int > pii;
typedef long double ld;

const int INF = 1000 * 1000 * 1000;
const lint LINF = 1000000000000000000LL;
const double eps = 1e-9;

void prepare()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
}

const int nmax = 105, mmax = 1000000;

int dp[nmax][mmax + 5];
int A, n, a[nmax];

bool solve()
{
	scanf("%d%d",&A,&n);
	for (int i = 0; i < n; i ++)
		scanf("%d",&a[i]);
	for (int i = 0; i <= n; i ++)
	{
		for (int j = 0; j <= mmax; j ++)
		{
			dp[i][j] = INF;
		}
	}
	sort(a, a + n);
	dp[0][A] = 0;
	for (int i = 0; i < n; i ++)
	{
		for (int j = 0; j <= mmax; j ++)
		{
			if (dp[i][j] != INF)
			{
				int nj;
				if (j > a[i])
				{
					nj = min(mmax, j + a[i]);
					dp[i + 1][nj] = min(dp[i + 1][nj], dp[i][j]);
				}
				else
				{
					dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1);
				}
				nj = min(mmax, j + (j - 1));
				dp[i][nj] = min(dp[i][nj], dp[i][j] + 1);
			}
		}
	}

	int ans = INF;
	for (int i = 0; i <= mmax; i ++)
		ans = min(ans, dp[n][i]);
	printf("%d\n", ans);
	return false;
}

int main()
{
	prepare();
	int t;
	scanf("%d",&t);
	for (int i = 0; i < t; i ++)
	{
		dbgx(i);
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}
