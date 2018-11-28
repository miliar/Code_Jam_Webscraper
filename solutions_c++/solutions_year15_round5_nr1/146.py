#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <ctime>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <list>
#include <stack>
#include <bitset>
#include <algorithm>
#include <iomanip>

using namespace std;

#define forn(i,n) for (int i = 0; i < int(n); i++)
#define ford(i,n) for (int i = int(n) - 1; i >= 0; i--)
#define fore(i,l,r) for (int i = int(l); i <= int(r); i++)
#define all(a) a.begin(), a.end()
#define sz(a) int(a.size())
#define mp make_pair
#define pb push_back
#define ft first
#define sc second
#define x first
#define y second

template<typename X> inline X abs(const X& a) { return a < 0 ? -a : a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9;
const ld PI = acosl(ld(-1));

const int N = 1000 * 1000 + 13;
int n, d;
int s0, as, cs, rs;
int m0, am, cm, rm;

inline bool read()
{
	if (scanf ("%d%d", &n, &d) != 2)
		return false;

	assert(scanf ("%d%d%d%d", &s0, &as, &cs, &rs) == 4);
	assert(scanf ("%d%d%d%d", &m0, &am, &cm, &rm) == 4);

	return true;
}

int s[N], m[N];

vector<int> g[N];
pt seg[N];
pt e[2 * N];
int sze;

void dfs (int v, int l, int r)
{
	l = max(l, s[v] - d), r = min(r, s[v]);
	seg[v] = mp(l, r);

	forn (i, sz(g[v]))
	{
		int to = g[v][i];

		dfs(to, l, r);
	}
}

inline void solve(int test)
{
	printf ("Case #%d: ", test + 1);

	s[0] = s0;
	m[0] = m0;

	for (int i = 1; i < n; i++)
	{
		s0 = int((s0 * 1ll * as + cs) % rs);
		m0 = int((m0 * 1ll * am + cm) % rm);

		s[i] = s0;
		m[i] = m0 % i;
	}

	forn (i, n)
		g[i].clear();

	fore (i, 1, n - 1)
		g[ m[i] ].pb(i);

	dfs(0, -INF, INF);

	sze = 0;
	forn (i, n)
	{
//		cerr << seg[i].ft << ' ' << seg[i].sc << endl;

		if (seg[i].ft > seg[i].sc)
			continue;

		e[sze++] = mp(seg[i].ft, -1);
		e[sze++] = mp(seg[i].sc, +1);
	}

	sort(e, e + sze);

	int ans = 1;
	int b = 0;
	forn (i, sze)
	{
		if (e[i].sc == -1)
			b++;
		else
			b--;
//
//		cerr << e[i].ft << ' ' << b << endl;

		ans = max(ans, b);
	}

	printf ("%d\n", ans);
}

int main()
{
#ifdef SU2_PROJ
	assert(freopen("input.txt", "r", stdin));
	assert(freopen("output.txt", "w", stdout));
#endif

	cout << setprecision(25) << fixed;
	cerr << setprecision(10) << fixed;

	srand(int(time(NULL)));

	int testCnt;
	assert(scanf ("%d", &testCnt) == 1);

	forn (test, testCnt)
	{
		assert(read());
		solve(test);
	}

#ifdef SU2_PROJ
	cerr << "TIME: " << clock() << endl;
#endif

	return 0;
}
