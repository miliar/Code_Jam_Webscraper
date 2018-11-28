#include "bits/stdc++.h"
 
using namespace std;
 
#define debug(x) cerr << "DEBUG: " << #x << " = " << x << endl
#define forn(i, n) for(int i = 0; i < (n); ++i)
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
#define mp make_pair
#define pb push_back
#define PATH "C:\\Users\\ValenKof\\Desktop\\"
 
template<typename T> inline void mn(T& x, const T& y) { if (y < x) x = y; }
template<typename T> inline void mx(T& x, const T& y) { if (x < y) x = y; }
template<typename T> inline int sz(const T& x) { return x.size(); }
 
typedef unsigned char uchar;
 
// SOLUTIONS BEGINS HERE

struct DSU {
	vector<int> p;
	vector<int> w;
	
	void init(int n) {
		p.resize(n);
		w.resize(n);
		forn (i, n) {
			w[i] = 0;
			p[i] = i;
		}
	}
	
	inline int find(int v) {
		if (p[v] == v) {
			return v;
		}
		return p[v] = find(p[v]);
	}
	
	inline void unite(int u, int v) {
		u = find(u);
		v = find(v);
		if (u == v) {
			return;
		}
		if (rand() & 1) {
			swap(u, v);
		}
		w[v] += w[u];
		p[u] = v;
	}
	
	inline int getw(int v) {
		return w[find(v)];
	}
};

void gen(vector<int>& x, long long a, long long c, long long r) {
	for (int i = 1; i < sz(x); ++i) {
		x[i] = (x[i - 1] * a + c) % r;
 	}
}

const int BLACK = 0;
const int GRAY = 1;
const int WHITE = 2;

void dfs(vector<vector<int>>& g, vector<int>& color, DSU& dsu, int u) {
	if (color[u] == GRAY) {
		dsu.w[dsu.find(u)]--;		
	}
	color[u] = WHITE;
	for (int v : g[u]) {
		if (color[v] != WHITE) {
			dfs(g, color, dsu, v);
		}
	}
}

void solve() {
	int n, d;
	cin >> n >> d;
	
	vector<int> s(n);
	long long as, cs, rs;
	cin >> s[0] >> as >> cs >> rs;
	gen(s, as, cs, rs);

	vector<int> m(n);
	long long am, cm, rm;
	cin >> m[0] >> am >> cm >> rm;
	gen(m, am, cm, rm);
	
	int ans = 1;
	vector<int> color(n, BLACK);
	
	vector<vector<int>> g(n);
	for (int i = 1; i < n; ++i) {
		m[i] %= i;
		g[m[i]].pb(i);		
	}
	
	DSU dsu;
	dsu.init(n);
	
	vector<int> order(n);
	forn (i, n) {
		order[i] = i;
	}
	sort(all(order), [&](int i, int j) { return s[i] < s[j]; });

	auto add = [&](int i) {
		if (color[i] == WHITE) {
			return;
		}
		color[i] = GRAY;
		if (i != 0 && color[m[i]] == GRAY) {
			dsu.unite(i, m[i]);
		}
		for (int v : g[i]) {
			if (color[v] == GRAY) {
				dsu.unite(i, v);
			}
		}
		dsu.w[dsu.find(i)]++;
	};
	
	
	int l = 0;
	int r = 0;
	while (r < n) {
		int remove = s[order[l]];
		while (l < r && s[order[l]] == remove) {
			dfs(g, color, dsu, order[l]);
			// cout << "remove " << order[l] << endl; 
			l++;
		}
		while (r < n && abs(s[order[r]] - s[order[l]]) <= d) {
			add(order[r]);
			// cout << "add " << order[r] << endl; 
			r++;
		}
		mx(ans, dsu.getw(0));
	}
	
	cout << ans;
	// for (int i = 0; i < n; ) {
		// int
	// }
	
	
}

int main() {
	// freopen(PATH"in.txt", "r", stdin);
	freopen(PATH"A-small-attempt0.in", "r", stdin);	
	freopen(PATH"out.txt", "w", stdout);
	int nTests;
	cin >> nTests;
	forn (iTest, nTests) {
		cout << "Case #" << (iTest + 1) << ": ";
		solve();
		cout << endl;
	}
	return 0;
}