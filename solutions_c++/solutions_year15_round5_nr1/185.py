#ifdef MG
//#define _GLIBCXX_DEBUG
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
#include <cassert>
#include <ctime>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>

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

template<typename X> inline X abs(const X &a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X &a) { return a * a; }
template<typename X, typename Y> inline ostream& operator<< (ostream& out, const pair <X, Y>& p) { return out << '(' << p.x << ", " << p.y << ')'; }
template<typename X> inline ostream& operator<< (ostream& out, const vector<X>& p) { forn(i, sz(p)) { if (i != 0) out << ' '; out << p[i]; } return out; }

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9, PI = acosl(ld(-1));

const int N = 1000 * 1000 + 13;

int n, d;

int s[N];
int m[N];

vector<int> g[N];

inline bool read()
{
	if (scanf("%d%d", &n, &d) != 2) return false;
	
	forn(i, n) g[i].clear();
	
	int as, cs, rs;
	assert(scanf("%d%d%d%d", &s[0], &as, &cs, &rs) == 4);
	forl(i, n - 1) s[i] = (int) (s[i - 1] * 1ll * as + cs) % rs;
	
	int am, cm, rm;
	assert(scanf("%d%d%d%d", &m[0], &am, &cm, &rm) == 4);
	forl(i, n - 1) m[i] = (int) (m[i - 1] * 1ll * am + cm) % rm;
	
	m[0] = -1;
	forl(i, n - 1) m[i] %= i;
	
	forn(i, n) if (m[i] != -1) g[m[i]].pb(i);
	
	return true;
}

int status[N];

void dfs2(int v, int &cnt) {
	cnt -= int(status[v] == 1);
	status[v] = -1;
	
	forn(i, sz(g[v]))
	{
		int to = g[v][i];
		if (status[to] != -1) {
			dfs2(to, cnt);
		}
	}
}

int root;

void dfs(int v, int &cnt) {
	status[v] = 1;
	cnt++;
	
	forn(i, sz(g[v])) {
		int to = g[v][i];
		if (status[to] == 0)
			dfs(to, cnt);
	}
}

inline void solve(int test)
{
	printf("Case #%d: ", test + 1);
	
	vector<pt> v(n);
	forn(i, n) v[i] = mp(s[i], i);
	
	sort(all(v));
	
	forn(i, n) status[i] = -1;
	
	int cnt = 0;
	int ans = 0;
	
	int p = 0;
	forn(i, n) {
		while (p < sz(v) && v[p].x - v[i].x <= d) {
			int u = v[p].y;
			
			assert(status[u] == -1);
			status[u] = 0;
			root = u;
			if (m[u] == -1 || status[m[u]] == 1) {
				dfs(u, cnt);
			}
			
			
			p++;
		}
		
		ans = max(ans, cnt);
		
		int u = v[i].y;
		//assert(status[u] != -1);
		dfs2(u, cnt);
	}
	
	cout << ans << endl;
}

int main()
{
#ifdef MG
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	
	cout << setprecision(10) << fixed;
	cerr << setprecision(5) << fixed;
	
	int T;
	cin >> T;
	
	forn(t, T)
	{
		assert(read());
		solve(t);
		cerr << t << endl;
	}
	
#ifdef MG
	cerr << "=== TIME: " << clock() << " ===" << endl;
#endif

	return 0;
}
