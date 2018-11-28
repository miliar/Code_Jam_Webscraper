#define _CRT_SECURE_NO_DEPRECATE
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

const int nmax = 1005;

vector < int > X;
int a[nmax], n, wh[nmax];
int cntLeft[nmax], cntRight[nmax];

void read()
{
	scanf("%d",&n);
	X.clear();
	for (int i = 0; i < n; i ++)
	{
		scanf("%d",&a[i]);
		X.pb(a[i]);
	}
	sort(all(X));
	for (int i = 0; i < n; i ++)
	{
		a[i] = lower_bound(all(X), a[i]) - X.begin();
		wh[a[i]] = i;
	}

	for (int i = 0; i < n; i ++)
	{
		cntLeft[i] = wh[i];
		cntRight[i] = n - 1 - wh[i];
		for (int j = wh[i] - 1; j >= 0; j --)
		{
			if (a[j] < i)
			{
				cntLeft[i]--;
			}
		}
		for (int j = wh[i] + 1; j < n; j ++)
		{
			if (a[j] < i)
			{
				cntRight[i]--;
			}
		}
	}
}

int dp[nmax][nmax];

int calc(int l, int r, int cur)
{
	int &ret = dp[l][cur];
	assert(l + r == cur);
	if (ret >= 0) return ret;
	if (l + r == n) return ret = 0;
	
	ret = INF;
	ret = min(ret, calc(l + 1, r, cur + 1) + cntLeft[cur]);
	ret = min(ret, calc(l, r + 1, cur + 1) + cntRight[cur] );

	return ret;
}

bool solve()
{
	read();
	_(dp, -1);
	int ans = calc(0, 0, 0);
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
		dbg("Test %d\n", i);
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}
