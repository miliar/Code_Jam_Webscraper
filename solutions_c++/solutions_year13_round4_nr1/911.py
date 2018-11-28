#if 1
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <functional>
#include <cstring>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <ctime>
#include <cassert>
#include <sstream>
#include <iostream>
#include <bitset>
#include <numeric>
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

string scase(int test)
{
	oss os;
	os << "Case #" << test << ":";
	return os.str();
}

template<class Flow, class Cost> struct mcmf_t {
        typedef pair<Flow, Cost> res_t;
        Cost inf; 
        struct edge_t {
                int u, v;
                Flow f, cap; Cost cost;
                edge_t() {}
                edge_t(int u, int v, Flow cap, Cost cost)
                        : u(u), v(v), cap(cap), cost(cost), f(cap) {}
        };
        vector< edge_t > edges;
        vector< vector<int> > g;
        int n;
        // SET PROPER INFINITY VALUE!
        mcmf_t() { inf = std::numeric_limits<Cost>::max(); }
        void init(int n) {
                edges.clear(); g.clear();
                g.resize(n); this->n = n;
        }
        int add_edge(int u, int v, Flow cap, Cost cost) {
                edges.push_back(edge_t(u, v, cap, cost));
                edges.push_back(edge_t(v, u, 0, -cost));
                g[u].push_back(edges.size() - 2);
                g[v].push_back(edges.size() - 1);
                return g[u].back();
        }
        void reinit() {
                for(int i = 0; i < edges.size(); ++i)
                        edges[i].f = edges[i].cap;
        }
        vector<Cost> phi, d;
        vector<int> pred;
        void ford_bellman(int source) {
                phi.assign(n, inf); phi[source] = 0;
                for(int it = 0; it < n - 1; ++it)
                        for(int i = 0; i < edges.size(); ++i)
                                if(edges[i].f > 0 && phi[edges[i].u] < inf)
                                        phi[edges[i].v] = min(phi[edges[i].v], phi[edges[i].u] + edges[i].cost);
        }
        bool dijkstra(int source, int tink) {
                d.assign(n, inf); pred.assign(n, -1);
                typedef pair<Cost, int> item;
                priority_queue< item, vector<item>, greater<item> > q;
                for(q.push(mp(d[source] = 0, source)); q.size(); ) {
                        item cur = q.top(); q.pop();
                        int u = cur.second;
                        Cost dst = cur.first;
                        if(dst != d[u]) continue;
                        for(int i = 0; i < g[u].size(); ++i) {
                                int id = g[u][i];
                                if(edges[id].f == 0) continue;
                                int v = edges[id].v;
                                Cost ncost = d[u] + edges[id].cost + phi[u] - phi[v];
                                if(d[v] > ncost)
                                { q.push(mp(d[v] = ncost, v)); pred[v] = id; }
                        }
                }
                for(int i = 0; i < n; ++i)
                        phi[i] = min(inf, phi[i] + d[i]);
                return d[tink] < inf;
        }

        res_t find(int source, int tink, bool must_max = true) {
                ford_bellman(source);
                res_t res(Flow(0), Cost(0));
                while(dijkstra(source, tink)) {
                        Cost cost = 0;
                        Flow flow = edges[pred[tink]].f;
                        int cur = tink;
                        while(cur != source) {
                                int id = pred[cur];
                                flow = min(flow, edges[id].f);
                                cost += edges[id].cost;
                                cur = edges[id].u;
                        }
                        if(!must_max && cost > 0) break;
                        cur = tink;
                        while(cur != source) {
                                int id = pred[cur];
                                edges[id].f -= flow; edges[id ^ 1].f += flow;
                                cur = edges[id].u;
                        }
                        res.first += flow; res.second += Cost(flow) * cost;
                }
                return res;
        }
};

typedef mcmf_t<int, LL> mcmf;

LL calc(int n, int st, int en)
{
	LL k = en - st;
	return k * n + k - (1 + k) * k / 2;
}

const int mod = 1000002013;

void solve(int test)
{
	int n, m;
	cin >> n >> m;

	vector<int> st(m);
	vector<int> en(m);
	vector<int> c(m);
	LL cur = 0;
	for(int i = 0; i < m; ++i)
	{
		cin >> st[i] >> en[i] >> c[i];
		cur += calc(n, st[i], en[i]) * c[i] % mod;
	}
	//dbg(cur);

	//sort(st.begin(), st.end());
	//sort(en.begin(), en.end());

	mcmf mc;
	mc.init(2 + 2 * m);
	int source = mc.g.size() - 2;
	int tink = mc.g.size() - 1;
	for(int i = 0; i < m; ++i)
	{
		mc.add_edge(source, i, c[i], 0);
		mc.add_edge(i + m, tink, c[i], 0);
	}

	for(int i = 0; i < m; ++i)
		for(int j = 0; j < m; ++j)
			if(st[i] <= en[j])
				mc.add_edge(i, j + m, max(c[i], c[j]), calc(n, st[i], en[j]));

	mcmf::res_t res = mc.find(source, tink, true);
	LL ans = cur - res.Y;
	ans %= mod;
	if(ans < 0)
		ans += mod;
	cout << scase(test) << " " << ans << endl;

}

int main()
{
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    //freopen(NAME ".in","r",stdin);freopen(NAME ".out","w",stdout);

	int tests;
	cin >> tests;
	for(int test = 1; test <= tests; ++test)
		solve(test);

    return 0;
}
/*************************
*************************/
#endif