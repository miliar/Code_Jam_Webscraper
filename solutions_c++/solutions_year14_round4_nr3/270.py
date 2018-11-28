#if 1
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
using namespace std;

typedef long long LL;
typedef long double LD;
typedef pair<int , int> pii;
typedef vector <int> veci;
typedef vector <veci> graph;
const LD eps = 1e-9;
const LD pi = acos(-1.0);
const int inf = 1000 * 1000 * 1000;
const LL inf64 = LL(inf) * inf;

#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define iss istringstream
#define oss ostringstream
#define dbg(x) {cerr << #x << " = " << x << endl;}
#define dbgv(x) {cerr << #x << " ={"; for (int _i = 0; _i < x.size(); _i++) {if (_i) cerr << ", "; cerr << x[_i];} cerr << "}" << endl;}
#define NAME "problem"

template<class T> string to_str(const T &a) { oss os; os << a; return os.str(); }
template<> string to_str<LD>(const LD& a) { oss os; os.precision(10); os.setf(ios::fixed); os << a; return os.str(); }
template<class T> T from_str(const string &s) { iss is; T val; is >> val; return val; }
string T(int test) { ostringstream os; os << "Case #" << test << ":"; return os.str(); }
int _test_start = -1, _test_end = -1;
bool need_to_run(int test) { return _test_start == -1 || _test_start <= test && test <= _test_end; }

struct max_flow_ford_t
{
	struct edge_t
	{
		int u, v, f, cap;
		edge_t() { }
		edge_t(int u, int v, int f) : u(u), v(v), f(f), cap(f) {}
	};

	max_flow_ford_t()
	{
		g.clear();
		edges.clear();
		passed.clear();
	}
	
	vector< edge_t > edges;
	vector< vector< int > > g;
	vector<int> passed;
	int it;
	int source, tink;
	
	void init(int n)
	{
		g.clear();
		edges.clear();
		g.resize(n);
		source = n - 2;
		tink = n - 1;
	}

	void reinit()
	{
		for(int i = 0; i < edges.size(); ++i)
			edges[i].f = edges[i].cap;
	}
	
	int add_edge(int u, int v, int cap, int icap = 0)
	{
		int sz = edges.size();
		edges.pb(edge_t(u, v, cap));
		edges.pb(edge_t(v, u, icap));
		g[u].pb(sz);
		g[v].pb(sz + 1);
		return g[u].back();
	}

	int dfs(int u, int mine)
	{
		if(u == tink || !mine) return mine;
		if(passed[u] == it) return 0;
		passed[u] = it;
		for(int i = 0; i < g[u].size(); ++i)
		{
			int id = g[u][i];
			if(int r = dfs(edges[id].v, min(mine, edges[id].f)))
			{
				edges[id].f -= r;
				edges[id ^ 1].f += r;
				return r;
			}
		}
		return 0;
	}

	
	int find()
	{
		passed.assign(g.size(), -1);
		int flow = it = 0;
		while(int add = dfs(source, inf))
		{
			flow += add;
			++it;
		}
		return flow;		
	}	
};
bool bad[3001][3001];
bool contains(int x1, int x2, int x3, int x4)
{
	return x1 <= x3 && x4 <= x2;
}
bool contains(int x1, int y1, int x2, int y2,
			  int x3, int y3, int x4, int y4)
{
	return contains(x1, x2, x3, x4) && contains(y1, y2, y3, y4);
}

void solve(int test)
{
	// read
	int w, h, b;
	cin >> w >> h >> b;
	vector< pair< pii, pii > > a(b);
	for (int i = 0; i < b; ++i)
		cin >> a[i].X.X >> a[i].X.Y >> a[i].Y.X >> a[i].Y.Y;
	
	if (!need_to_run(test)) return;
	// solve
	vector<int> sx, sy;
	sx.pb(0);
	sx.pb(w);
	sy.pb(0);
	sy.pb(h);
	for (int i = 0; i < b; ++i)
	{
		sx.pb(a[i].X.X);
		sx.pb(a[i].Y.X + 1);
		sy.pb(a[i].X.Y);
		sy.pb(a[i].Y.Y + 1);
	}
	sort(sx.begin(), sx.end());
	sort(sy.begin(), sy.end());
	sx.erase(unique(sx.begin(), sx.end()), sx.end());
	sy.erase(unique(sy.begin(), sy.end()), sy.end());
	memset(bad, 0, sizeof bad);
	int cnt = 0;
	int nx = sx.size() - 1;
	int ny = sy.size() - 1;
	for (int i = 0; i + 1 < sx.size(); ++i)
		for (int j = 0; j + 1 < sy.size(); ++j)
		{
			++cnt;
			bool fl = true;
			for (int k = 0; k < b; ++k)
				if (contains(a[i].X.X, a[i].X.Y, a[i].Y.X, a[i].Y.Y,
							 sx[i], sy[j], sx[i + 1], sy[j + 1]))
				{
					fl = false;
					break;
				}
			bad[i][j] = !fl;
		}

	assert(cnt == nx * ny);
	max_flow_ford_t flow;
	flow.init(cnt * 2 + 2);
	for (int i = 0; i < nx; ++i)
	{
		if (!bad[i][0])
			flow.add_edge(flow.source, 2 * (i * ny + 0) + 0, sx[i + 1] - sx[i]);
		if (!bad[i][ny - 1])
			flow.add_edge(2 * (i * ny + ny - 1) + 1, flow.tink, sx[i + 1] - sx[i]);
	}

	int dx[] = {-1, 1, 0, 0};
	int dy[] = {0, 0, -1, 1};
	for (int i = 0; i < nx; ++i)
		for (int j = 0; j < ny; ++j)
			if (!bad[i][j])
			{
				for (int k = 0; k < 4; ++k)
				{
					int ni = i + dx[k];
					int nj = j + dy[k];
					if (0 > ni || 0 > nj || ni >= nx || nj >= ny)
						continue;
					if (bad[ni][nj])
						continue;
					int mf = k < 2 ? sy[j + 1] - sy[j] : sx[i + 1] - sx[i];
					flow.add_edge(2 * (i * ny + j) + 1, 2 * (ni * ny + nj) + 0, mf);
				}
				flow.add_edge(2 * (i * ny + j) + 0, 2 * (i * ny + j) + 1, )
			}

			 
	
	// write
	
}

int main(int argc, char *argv[])
{
	//freopen("input.txt", "r", stdin); //freopen("output.txt", "w", stdout);
	//freopen(NAME ".in","r",stdin); freopen(NAME ".out","w",stdout);
	if (argc == 2) { _test_start = _test_end = from_str<int>(argv[1]); }
	if (argc == 3) { _test_start = from_str<int>(argv[1]); _test_end = from_str<int>(argv[2]); }

	clock_t tstart = clock();
	
	int tests;
	scanf("%d", &tests);
	for(int test = 1; test <= tests; ++test)
	{
		clock_t tprev = clock();
		solve(test);
		if (need_to_run(test))
			dbg("elapsed for #" << test << ": " << (clock() - tprev) / LD(CLOCKS_PER_SEC));
	}

	dbg("elapsed: " << (clock() - tstart) / LD(CLOCKS_PER_SEC));
	return 0;
}
/*************************
*************************/
#endif

