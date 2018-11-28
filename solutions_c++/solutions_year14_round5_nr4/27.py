#undef NDEBUG
#ifdef SU2_PROJ
#define _GLIBCXX_DEBUG
#endif

#include <iostream>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <climits>
#include <cstring>
#include <ctime>
#include <cmath>
#include <cassert>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <utility>
#include <numeric>
#include <functional>

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define forl(i, n) for (int i = 1; i <= int(n); i++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define fore(i, l, r) for (int i = int(l); i <= int(r); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(x, y) make_pair((x), (y))
#define ft first
#define sc second
#define x first
#define y second

using namespace std;

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }
inline ostream& operator<< (ostream& out, const pt& p) { return out << '(' << p.x << ", " << p.y << ')'; }

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9, PI = 3.1415926535897932384626433832795;

const int N = 80 + 3;

int n;
int c[N];
int w[N][N];
vector<int> g[N];

inline bool read()
{
	if (scanf("%d", &n) != 1) return false;
	
	forn(i, n) assert(scanf("%d", &c[i]) == 1);
	
	forn(i, n) g[i].clear();
	
	forn(i, n) forn(j, n) w[i][j] = (i == j ? 0 : INF);	
	
	forn(x, n - 1)
	{
		int y;
		assert(scanf("%d", &y) == 1);
		y--;
		
		g[x].pb(y);
		g[y].pb(x);
		w[x][y] = w[y][x] = 1;
	}
	
	return true;
}

inline bool check(int x, int y, int a, int b)
{
	if (w[a][b] == w[a][x] + 1 + w[y][b]) return false;
	if (w[a][b] == w[a][y] + 1 + w[x][b]) return false;
	return true;
}

inline int calc(int x, int a, int b, int c, int d)
{
	if (w[a][x] + w[x][b] == w[a][b]) return 0;
	if (w[c][x] + w[x][d] == w[c][d]) return 0;
	return ::c[x];
}

int z[N][N][N][N][2][2];

int solve(int a, int b, int c, int d, int who, int prev)
{
	//cerr << a << ' ' << b << ' ' << c << ' ' << d << endl;
	int& ans = z[a][b][c][d][who][prev];
	if (ans != -1) return ans;
	
	int v = who == 0 ? b : d;
	
	bool can = false;
	
	int cur = -INF;
	
	forn(i, sz(g[v]))
	{
		int to = g[v][i];
		if (!check(v, to, a, b) || !check(v, to, c, d)) continue;
		
		int na = a, nb = b, nc = c, nd = d;
		
		if (who == 0) nb = to;
		else nd = to;

		can = true;
		cur = max(cur, calc(to, a, b, c, d) - solve(na, nb, nc, nd, who ^ 1, 1));
	}
	
	//cerr << cur << endl;
	
	if (!can && !prev) return ans = 0;
	if (!can) return ans = -solve(a, b, c, d, who ^ 1, 0);
	return ans = cur;
}

inline void solve(int test)
{
	printf("Case #%d: ", test + 1);
	
	forn(k, n)
		forn(i, n)
			forn(j, n)
				w[i][j] = min(w[i][j], w[i][k] + w[k][j]);
				
	int ans = -INF;
	
	memset(z, -1, sizeof z);

	forn(i, n)
	{
		int cur = INF;
		forn(j, n)
		{
			cur = min(cur, c[i] - (i == j ? 0 : c[j]) + solve(i, i, j, j, 0, 1));
		}
		
		ans = max(ans, cur);
	}
			
	cout << ans << endl;
}

int main()
{
#ifdef SU2_PROJ
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif
    
    cout << setprecision(10) << fixed;
    cerr << setprecision(5) << fixed;
    
    int testCount;
    cin >> testCount;
    
    forn(test, testCount)
    {
    	cerr << test << endl;
	    assert(read());
    	solve(test);
    }
    
#ifdef SU2_PROJ
    cerr << "== TIME: " << clock() << " ==" << endl;
#endif

    return 0;
}
