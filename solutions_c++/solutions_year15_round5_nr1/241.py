#pragma comment(linker, "/stack:128000000")

#include <algorithm>
#include <iostream>
#include <cassert>
#include <iomanip>
#include <climits>
#include <utility>
#include <cstring>
#include <complex>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <bitset>
#include <string>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <set>
#include <map>

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define forl(i, n) for (int i = 1; i <= int(n); i++)
#define fore(i, l, r) for (int i = int(l); i <= int(r); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(a, b) make_pair((a), (b))
#define x first
#define y second
#define ft first
#define sc second

using namespace std;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = INT_MAX / 2;
const ld EPS = 1e-9;
const ld PI = 3.1415926535897932384626433832795;

const int N = 1000 * 1000 + 13;

int n, d;
int s[N];
int par[N];
vector<int> g[N];
vector<int> vert[N];

inline void readGen(int a[N])
{
	assert(scanf("%d", &a[0]) == 1);
	int aa, bb, cc;
	assert(scanf("%d%d%d", &aa, &bb, &cc) == 3);

	fore(i, 1, n - 1)
	{
		li val = li(a[i - 1]);
		val = (val * li(aa) + li(bb));
		val %= li(cc);

		a[i] = int(val);
	}
}

inline bool read()
{
	if (scanf("%d%d", &n, &d) != 2)
		return false;

	readGen(s);
	readGen(par);

	/*forn(i, n)
		cerr << s[i] << " ";
	cerr << endl;
	forn(i, n)
		cerr << par[i] << " ";*/
	
    return true;
}

int used[N];

inline int dfs(int v, int lf, int rg)
{
	assert(!used[v]);
	used[v] = true;
	int ans = 1;
	assert(lf <= s[v] && s[v] <= rg);

	forn(i, sz(g[v]))
	{
		int to = g[v][i];

		if (!used[to] && lf <= s[to] && s[to] <= rg)
			ans += dfs(to, lf, rg);
	}

	return ans;
}

inline int dfsOut(int v)
{
	int ans = 1;
	assert(used[v]);
	used[v] = false;

	forn(i, sz(g[v]))
	{
		int to = g[v][i];

		if (used[to])
			ans += dfsOut(to);
	}

	return ans;
}

inline int out(int val)
{
	int ans = 0;

	forn(i, sz(vert[val]))
	{
		int v = vert[val][i];

		if (used[v])
			ans += dfsOut(v);
	}

	return ans;
}

inline int in(int val)
{
	int ans = 0;

	forn(i, sz(vert[val]))
	{
		int v = vert[val][i];
		if (v == 0)
		{
			assert(used[v]);
			continue;
		}

		if (used[ par[v] ] && !used[v])
		{
			ans += dfs(v, val - d, val);
		}
	}

	return ans;
}

inline void solve(int test)
{
	printf("Case #%d: ", test + 1);
	cerr << test + 1 << endl;

	forn(i, n)
	{
		g[i].clear();
		used[i] = false;
	}

	int maxs = 0;
	forn(i, n)
		maxs = max(maxs, s[i]);

	int lf = max(0, s[0] - d);
	int rg = min(maxs, s[0]);

	fore(i, lf, rg + d + 2)
		vert[i].clear();

	forn(i, n)
		vert[ s[i] ].pb(i);

	fore(i, 1, n - 1)
	{
		par[i] %= i;
		g[ par[i] ].pb(i);
	}

	int cur = dfs(0, lf, lf + d);
	int ans = cur;

	fore(val, lf, rg - 1)
	{
		/*cerr << val << " " << val + d << " " << cur << endl;
		forn(i, n)
			cerr << used[i] << " ";
		cerr << endl;*/
		cur -= out(val);
		cur += in(val + d + 1);
		ans = max(ans, cur);
	}

	cout << ans << endl;
}

int main()
{
#ifdef HP
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif

	int testCnt;
	assert(cin >> testCnt);

	forn(test, testCnt)
	{
    	assert(read());
    	solve(test);
	}

    return 0;
}

