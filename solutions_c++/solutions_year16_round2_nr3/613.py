#include <algorithm>
#include <iostream>
#include <map>
#include <utility>

using namespace std;

map<string, int> fst, snd;
int f(string& s) {
	if (!fst.count(s)) {
		fst.insert(make_pair(s, fst.size()));
	}
	return fst[s];
}
int s(string& s) {
	if (!snd.count(s)) {
		snd.insert(make_pair(s, snd.size()));
	}
	return snd[s];
}

typedef int flow_type;

const int MAXV = 50 * 50 * 50;
const int MAXE = 2 * 50 * 50 * 50 * 3;
const int MAX_DIST = numeric_limits<int>::max();
const flow_type MAX_FLOW = numeric_limits<flow_type>::max();

typedef struct struct_edge* edge;
struct struct_edge {
	int v;
	flow_type c;
	edge n, b;
} pool[MAXE];
edge top;
int S, T;
edge adj[MAXV];
void build_graph(int s, int t) {
	top = pool;
	fill(adj, adj + MAXV, nullptr);
	S = s, T = t;
}
void add_edge(int u, int v, flow_type c, flow_type bc = 0) {
	top->v = v, top->c = c, top->n = adj[u], adj[u] = top++;
	top->v = u, top->c = bc, top->n = adj[v], adj[v] = top++;
	adj[u]->b = adj[v], adj[v]->b = adj[u];
	if (u == v)
		adj[u]->n->b = adj[u], adj[v]->b = adj[v]->n;
}
int d[MAXV];
int q[MAXV];
int qh, qt;
bool relabel() {
	fill(d, d + MAXV, MAX_DIST), d[q[qh = qt = 0] = T] = 0;
	while (qh <= qt) {
		int u = q[qh++];
		for (edge i = adj[u]; i; i = i->n)
			if (i->b->c && d[i->v] > d[u] + 1) {
				d[i->v] = d[u] + 1;
				if ((q[++qt] = i->v) == S)
					return true;
			}
	}
	return false;
}
edge cur[MAXV];
flow_type augment(int u, flow_type e) {
	if (u == T)
		return e;
	flow_type f = 0;
	for (edge& i = cur[u]; i; i = i->n) {
		if (i->c > 0 && d[u] == d[i->v] + 1) {
			flow_type df = augment(i->v, min(e, i->c));
			if (df > 0)
				i->c -= df, i->b->c += df, e -= df, f += df;
		}
		if (!(e > 0))
			break;
	}
	return f;
}
flow_type dinic() {
	flow_type f = 0;
	while (relabel())
		copy(adj, adj + MAXV, cur), f += augment(S, MAX_FLOW);
	return f;
}

void solve() {
	int n;
	cin >> n;
	vector<pair<int, int> > e(n);
	for (int i = 0; i < n; ++i) {
		string x, y;
		cin >> x >> y;
		e[i].first = f(x);
		e[i].second = s(y);
	}
	build_graph(fst.size() + snd.size(), fst.size() + snd.size() + 1);
	for (int i = 0; i < fst.size(); ++i) {
		add_edge(S, i, 1);
	}
	for (int i = 0; i < snd.size(); ++i) {
		add_edge(fst.size() + i, T, 1);
	}
	for (int i = 0; i < n; ++i) {
		add_edge(e[i].first, fst.size() + e[i].second, 1);
	}
	int f = dinic();
	int ans = n - (fst.size() + snd.size() - f);
	cout << " " << ans;
	fst.clear();
	snd.clear();
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ":";
		solve();
		cout << endl;
	}
}
