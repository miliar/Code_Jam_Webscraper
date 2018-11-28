#include <iostream> 
#include <cstdio> 
#include <set> 
#include <map> 
#include <vector> 
#include <queue> 
#include <stack> 
#include <cmath> 
#include <algorithm> 
#include <cstring> 
#include <bitset> 
#include <ctime> 
#include <sstream>
#include <stack> 
#include <cassert> 
#include <list> 
#include <deque>
//#include <unordered_set> 
using namespace std;
typedef long long li;
typedef long double ld;
typedef vector<int> vi;
typedef pair<int, int> pi;

#define mp make_pair 
#define pb push_back 
#define y1 botva
#define all(s) s.begin(), s.end() 
void solve();

#define NAME "changemeplease"
int main() {
#ifdef YA 
	//cerr << NAME << endl;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout); 
	clock_t start = clock();
#else 
	freopen("input.txt", "r", stdin); 
	freopen("output.txt", "w", stdout); 
#endif 
	ios_base::sync_with_stdio(false);
	cout << fixed;
	cout.precision(10);
	int t = 1;
	cin >> t;	 
	for (int i = 1; i <= t; ++i) {
		cerr << i << endl;
		cout << "Case #" << i << ": ";
		solve();
	}
#ifdef YA 
	//cout << "\n\n\nTime:" << ((clock() - start) / 1.0 / CLOCKS_PER_SEC);
#endif 
	return 0;
}

struct edge {
	int flow;
	int cap;
	int id;
	int to;
	edge(int cap, int id, int to):flow(0), cap(cap), id(id), to(to){}
};

vector <vector <bool> > good;

vector <vector <edge> > g;
const int dx[4] = {0,0,1,-1};
const int dy[4] = {1,-1,0,0};

void add(int from, int to, int cap) {
	g[from].push_back(edge(cap, g[to].size(), to));
	g[to].push_back(edge(0, g[from].size() - 1, from));
}

int s, t;

bool is_good(const edge& a) {
	return a.cap - a.flow > 0;	
}

vector < pair <int, int> > from;
vector <bool> vis;

void dfs(int v) {
	if (vis[t])
		return;
	vis[v] = true;
	for (int i = 0; i < g[v].size(); ++i) {
		if (is_good(g[v][i])) {
			int to = g[v][i].to;
			if (!vis[to]) {
				from[to] = mp(v, i);
				dfs(to);
			}
		}
	}
}

bool trygo() {
	from.resize(g.size());
	vis.clear();
	vis.assign(g.size(), 0);
	dfs(s);
	if (!vis[t])
		return false;
	
	int cur = t;
	while (cur != s) {
		int fr = from[cur].first;
		int id = from[cur].second;
		++g[fr][id].flow;
		--g[cur][g[fr][id].id].flow;
		cur = fr;
	}
	return true;
}

bool bfs() {
	vector < pair <int, int> > from(g.size());
	vector <bool> vis(g.size(), 0);
	queue <int> q;
	q.push(s);
	vis[s] = true;
	while (!q.empty() && !vis[t]) {
		int cur = q.front();
		q.pop();
		for (int i = 0; i < g[cur].size(); ++i) {
			if (!is_good(g[cur][i]))
				continue;
			int to = g[cur][i].to;
			if (vis[to])
				continue;
			vis[to] = true;
			from[to] = mp(cur, i);
			q.push(to);
		}
	}
	if (!vis[t])
		return false;

	int cur = t;
	while (cur != s) {
		int fr = from[cur].first;
		int id = from[cur].second;
		++g[fr][id].flow;
		--g[cur][g[fr][id].id].flow;
		cur = fr;
	}
	return true;
}

void solve() {
	int w, h, b;
	cin >> w >> h >> b;
	g.clear();
	good.clear();

	good.assign(w, vector <bool> (h, 1));
	for (int z = 0; z < b; ++z) {
		int x0, x1, y0, y1;
		cin >> x0 >> y0 >> x1 >> y1;
		if (x0 > x1)
			swap(x0, x1);
		if (y0 > y1)
			swap(y0, y1);
		for (int i = x0; i <= x1; ++i)
			for (int j = y0; j <= y1; ++j)
				good[i][j] = false;
	}
	
	s = 2 * w * h;
	t = 2 * w * h + 1;
	g.resize(t + 1);
	
	for (int x = 0; x < w; ++x) {
		int tmp = x * h;
		add(s, 2 * tmp, 1);	
		add(2 * (tmp + h - 1) + 1, t, 1);
	}
	for (int i = 0; i < w; ++i)
		for (int j = 0; j < h; ++j) {
			if (!good[i][j])
				continue;
			add(2 * (i * h + j), 2 * (i * h + j) + 1, 1);

			for (int t = 0; t < 4; ++t) {
				pair <int, int> cur = mp(i + dx[t], j + dy[t]);
				if (cur.first >= 0 && cur.second >= 0 && cur.first < w && cur.second < h) {
					add(2 * (i * h + j) + 1, 2 * (cur.first * h + cur.second), 1);
				}
			}
		}
	int ans = 0;
	while (bfs()) {
		++ans;
	}
	cout << ans << endl;
}