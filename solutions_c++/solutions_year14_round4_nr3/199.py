#include <iostream>
#include <cstdio>
#include <vector>
#include <limits>
#include <queue>
using namespace std;

struct Edge {
	int from, to, cap, flow;

	Edge(int from, int to, int cap, int flow):
		from (from), to (to), cap (cap), flow (flow) {}

	int residual() const {
		return cap - flow;
	}
};

struct Dinic {
	int n;
	vector<Edge> edge;
	vector<vector<int> > graph;
	vector<vector<int>::iterator> work;
	vector<int> dist;

	Dinic(int n): n (n) {
		edge.clear();
		graph.assign(n, vector<int>());
		work.assign(n, vector<int>::iterator());
		dist.resize(n);
	}

	void addEdge(int u, int v, int cap, bool twoway) {
		graph[u].push_back(edge.size());
		edge.push_back(Edge(u, v, cap, 0));
		graph[v].push_back(edge.size());
		edge.push_back(Edge(v, u, twoway ? cap : 0, 0));
	}

	void resetNetwork() {
		for(unsigned i = 0; i < edge.size(); ++i) edge[i].flow = 0;
	}

	int dfs(int s, int t, int f) {
		if(s == t) return f;
		for(vector<int>::iterator &x = work[s]; x != graph[s].end(); ++x) {
			int v = edge[*x].to;
			if(dist[s] + 1 == dist[v] && edge[*x].residual() > 0) {
				int d = dfs(v, t, min(f, edge[*x].residual()));
				if(d > 0) return edge[*x].flow += d, edge[*x ^ 1].flow -= d, d;
			}
		}
		return 0;
	}

	bool bfs(int s, int t) {
		queue<int> q; q.push(s);
		fill(dist.begin(), dist.end(), -1); dist[s] = 0;
		while(!q.empty()) {
			int u = q.front(); q.pop();
			for(unsigned i = 0; i < graph[u].size(); ++i) {
				int x = graph[u][i];
				int v = edge[x].to;
				if(dist[v] == -1 && edge[x].residual() > 0) {
					dist[v] = dist[u] + 1;
					q.push(v);
				}
			}
		}
		return dist[t] != -1;
	}

	long long getFlow(int s, int t) {
		long long totFlow = 0;
		while(bfs(s, t)) {
			for(int i = 0; i < n; ++i) work[i] = graph[i].begin();
			for(int d; (d = dfs(s, t, numeric_limits<int>::max())) != 0; totFlow += d);
		}
		return totFlow;
	}
};

const int DELTA[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

int main() {
	int nTest; cin >> nTest;
	for(int test = 0; test < nTest; ++test) {
		int w, h, b; cin >> w >> h >> b;
		vector<vector<bool> > mark (w, vector<bool>(h, false));
		for(int i = 0; i < b; ++i) {
			int x0, y0, x1, y1; cin >> x0 >> y0 >> x1 >> y1;
			for(int x = x0; x <= x1; ++x)
				for(int y = y0; y <= y1; ++y)
					mark[x][y] = true;
		}
		Dinic net (2 * w * h + 2);
		int source = net.n - 2, sink = net.n - 1;
		for(int x = 0; x < w; ++x)
			for(int y = 0; y < h; ++y) if(!mark[x][y]) {
				for(int dir = 0; dir < 4; ++dir) {
					int xx = x + DELTA[dir][0], yy = y + DELTA[dir][1];
					if(xx >= 0 && xx < w && yy >= 0 && yy < h && !mark[xx][yy])
						net.addEdge(w * h + x * h + y, xx * h + yy, 1, false);
				}
				net.addEdge(x * h + y, w * h + x * h + y, 1, false);
			}
		for(int x = 0; x < w; ++x) {
			if(!mark[x][0]) net.addEdge(source, x * h + 0, 1, false);
			if(!mark[x][h - 1]) net.addEdge(w * h + x * h + (h - 1), sink, 1, false);
		}
		printf("Case #%d: %lld\n", test + 1, net.getFlow(source, sink));
	}
	return 0;
}
