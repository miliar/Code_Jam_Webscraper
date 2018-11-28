#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <deque>
#include <cmath>
#include <ctime>
#include <stack>
#include <set>
#include <map>
#include <cassert>
#include <memory.h>

using namespace std;

#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()

typedef long long li;
typedef long double ld;
typedef vector<int> vi;
typedef pair <int, int> pi;

void solve();

#define FILENAME "souvenir"

int main(){
    string s = FILENAME;
#ifdef RIAD
    freopen("input", "r", stdin);
#ifndef DEBUG
    freopen("output", "w", stdout);
#endif
    //cout<<FILENAME<<endl;
    //assert (s != "change me please");
    clock_t start = clock(); 
#else
    //freopen(FILENAME ".in", "r", stdin);
    //freopen(FILENAME ".out", "w", stdout);
#endif
    cout.sync_with_stdio(0); 
    cout.precision(10);
    cout << fixed;
    int t = 1;
    cin >> t;
	for(int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		solve();
	}
#ifdef DEBUG
    cerr<<"\n\n"<<(clock() - start) / 1.0 / CLOCKS_PER_SEC<<"\n\n\n";
#endif
    return 0;
}


const li INF = 2000000000; // greater than max capacity
const int maxn =50000 * 2 + 100;

struct edge {
	int from, to, cap, flow;
};

vector<edge> edges;
vector<int> g[maxn];

int q[maxn];
int d[maxn];

bool bfs(int s, int t) {
	memset(d, -1, sizeof d);
	int qh = 0, qt = 0;
	q[qt++] = s;
	d[s] = 0;
	while(qh != qt) {
		int cur = q[qh++];
		for(int i = 0; i < (int)g[cur].size(); ++i) {
			edge& e = edges[g[cur][i]];
			if(e.flow != e.cap && d[e.to] == -1) {
				q[qt++] = e.to;
				d[e.to] = d[cur] + 1;
			}
		}
	}
	return d[t] != -1;
}

int ptr[maxn];

int dfs(int v, int t, int mx) {
	if(!mx)
		return mx;

	if(v == t)
		return mx;

	for(int& i = ptr[v]; i < (int)g[v].size(); ++i) {
		int id = g[v][i];
		edge& e = edges[id];
		if(d[e.to] == d[v] + 1) {
			if(int pushed = dfs(e.to, t, min(mx, int(e.cap - e.flow)))) {
				e.flow += pushed;
				edges[id ^ 1].flow -= pushed;
				return pushed;
			}
		}
	}
	return 0;
}

li dinic(int s, int t) {
	li res = 0;
	while(bfs(s, t)) {
		memset(ptr, 0, sizeof ptr);

		while(int pushed = dfs(s, t, INF)) {
			res += pushed;
		}
	}
	return res;
}

void add_edge(int from, int to, int cap = 1) {
	edge e1 = {from, to, cap, 0};
	edge e2 = {to, from, 0,0};
	g[from].push_back(edges.size());
	edges.push_back(e1);
	g[to].push_back(edges.size());
	edges.push_back(e2);
}



vector<vector<int>> mapa;


int w, h, b;
	
int go(int i, int j) {
	return i * h + j;
}

void solve() {
	cin >> w >> h >> b;
	mapa = vector<vi>(w, vi(h, 1));
	for(int i = 0; i < b; ++i) {
		int x0, y0, x1, y1;
		cin >>x0>>y0>>x1>>y1;
		for(int j = x0; j <= x1; ++j) {
			for(int k = y0; k <= y1; ++k) {	
				mapa[j][k] = 0;
			}
		}
	}
	for(int i = 0; i < maxn; ++i) {
		g[i].clear();
	}
	
	edges.clear();
	
	int s = 2 * w * h;
	int t = s + 1;
	
	for(int i = 0; i < w; ++i) {
		for(int j = 0; j < h; ++j) {
			if(mapa[i][j]) {
				add_edge(go(i, j), go(i, j) + w * h);
			}
		}
	}
	
	for(int i = 0; i + 1 < w; ++i) {
		for(int j = 0; j < h; ++j) {
			add_edge(go(i, j) + w * h, go(i + 1, j));
			add_edge(go(i + 1,j) + w * h, go(i, j));
		}
	}
	
	for(int i = 0; i < w; ++i) {
		for(int j = 0; j + 1 < h; ++j) {
			add_edge(go(i, j + 1) + w * h, go(i, j));
			add_edge(go(i, j) + w * h, go(i, j + 1));
		}
	}
	
	
	for(int i = 0; i < w; ++i) {
		add_edge(s, go(i, 0));
		add_edge(go(i, h - 1) + w * h, t);
	}
	
	cout << dinic(s, t) << "\n";
}
