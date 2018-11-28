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
#include <unordered_map>
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
bool need_to_run(int test) { return _test_start == -1 || (_test_start <= test && test <= _test_end); }

// max flow algorithm based on dfs (ford-fulkerson)
// complexity: O(Flow * M)
// tested: wf2007 containers (uva1062)
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

struct common_words_t {
	void add_word(const string& s, int lang) {
		auto it = cnt.find(s);
		if (it == cnt.end()) {
			cnt.emplace(s, pii());
			it = cnt.find(s);
		}
		pii before = it->Y;
		if (lang == 0) {
			it->Y.X++;
		} else {
			it->Y.Y++;
		}

		if (it->Y.X > 0 && it->Y.Y > 0 && (before.X == 0 || before.Y == 0)) {
			++common;
		}
	}

	void remove_word(const string& s, int lang) {
		auto it = cnt.find(s);
		assert(it != cnt.end());

		pii before = it->Y;
		if (lang == 0) {
			it->Y.X--;
		} else {
			it->Y.Y--;
		}

		if ((it->Y.X == 0 || it->Y.Y == 0) && (before.X > 0 && before.Y > 0)) {
			--common;
		}
	}
	
	int get_common() const {
		return common;
	}

	int common = 0;
	unordered_map<string, pii> cnt;
};

void solve(int test) {
	// read
	int n;
	cin >> n;
	vector<vector<string> > a(n);
	string tmp;
	getline(cin, tmp);
	for (int i = 0; i < n; ++i) {
		getline(cin, tmp);
		iss is(tmp);
		while (is >> tmp) {
			a[i].pb(tmp);
		}
		sort(a[i].begin(), a[i].end());
	}

	if (!need_to_run(test)) return;
	// solve
	// max_flow_ford_t mf;
	// mf.init(n);
	// mf.source = 0;
	// mf.tink = 1;

	// for (int i = 1; i < n; ++i) {
		
	// }
	
	common_words_t cw;
	for (int i = 0; i < 2; ++i) {
		for (int j = 0; j < a[i].size(); ++j) {
			cw.add_word(a[i][j], i);
		}
	}
	dbg(cw.get_common());

	int best = inf;
	for (int mask = 0; mask < 1 << (n - 2); ++mask) {
		for (int i = 2; i < n; ++i) {
			int lang = (mask >> (i - 2)) & 1;
			for (int j = 0; j < a[i].size(); ++j) {
				cw.add_word(a[i][j], lang);
			}
		}

		best = min(best, cw.get_common());

		for (int i = 2; i < n; ++i) {
			int lang = (mask >> (i - 2)) & 1;
			for (int j = 0; j < a[i].size(); ++j) {
				cw.remove_word(a[i][j], lang);
			}
		}

	}
	
	// write
	cout << T(test) << " " << best << endl;

}

int main(int argc, char *argv[]) {
	//freopen("input.txt", "r", stdin); //freopen("output.txt", "w", stdout);
	//freopen(NAME ".in","r",stdin); freopen(NAME ".out","w",stdout);
	if (argc == 2) { _test_start = _test_end = from_str<int>(argv[1]); }
	if (argc == 3) { _test_start = from_str<int>(argv[1]); _test_end = from_str<int>(argv[2]); }

	clock_t tstart = clock();
	
	int tests;
	scanf("%d", &tests);
	for(int test = 1; test <= tests; ++test) {
		clock_t tprev = clock();
		solve(test);
		if (need_to_run(test)) {
		//	dbg("elapsed for #" << test << ": " << (clock() - tprev) / LD(CLOCKS_PER_SEC));
		}
	}

	dbg("elapsed: " << (clock() - tstart) / LD(CLOCKS_PER_SEC));
	return 0;
}
/*************************
*************************/
#endif
