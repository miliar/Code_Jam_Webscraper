#include <bits/stdc++.h>

using namespace std;


#define FOR(i, n) for (int i = 0; i < (int)(n); i++)
#define REP(i, a, b) for (int i = (int)(a); i <= (int)(b); i++)
#define CIR(i, a, b) for (int i = (int)(b); i >= (int)(a); i--)
#define ADJ(i, u) for (int i = hd[u]; i != -1; i = edge[i].nxt)
#define ECH(i, v) for (__typeof((v).begin()) i = (v).begin(); i != (v).end(); ++ i)

#define PII pair<int, int>
#define FI first
#define SE second
#define MP make_pair
#define PB push_back
#define SZ(v) v.size()
#define ALL(v) v.begin(), v.end()
#define CLR(v, a) memset(v, a, sizeof(v))
#define IT iterator
#define LL long long
#define DB double
#define PI 3.1415926
#define INF 1000000000


#define N 100105
#define M (N * 40)

struct Dinic {

	struct Edge {
	        int cap, flow, nxt, to;

		void init(int a, int c, int d) {
			to = a, cap = c, flow = 0, nxt = d;
		}    
	};

	int hd[N], used[N];
	int it;
	int lev[N], que[N];
	Edge edge[M];
	int n, s, t;
	int maxFlow;

	void init(int n, int s, int t) {
		it = 0;
		this->n = n;
		this->s = s, this->t = t;
		FOR(i, n) {
			hd[i] = -1;
		}
	}

	void addEdge(int u, int v, int c) {
		edge[it].init(v, c, hd[u]);
		hd[u] = it++;
		edge[it].init(u, 0, hd[v]);
		hd[v] = it++;
	}

	bool bfs() {
		FOR(i, n) lev[i] = -1;
		lev[s] = 0;
		int st = 0, ed = 0;
		que[ed++] = s;
		while (st < ed) {
			int u = que[st++];
			ADJ(i, u) {
				int v = edge[i].to;	
				if (lev[v] == -1 && edge[i].cap > edge[i].flow) {
					lev[v] = lev[u] + 1;
					que[ed++] = v;
				}
			}
		}

		return lev[t] != -1;    
	}

	int dfs(int u, int f) {
		if (u == t) return f;

		for(int& i = used[u]; i != -1; i = edge[i].nxt) {
			int v = edge[i].to;
			if (edge[i].cap > edge[i].flow && lev[v] == lev[u] + 1) {
				int tmp = dfs(v, min(edge[i].cap - edge[i].flow, f));
				if (tmp > 0) {
					edge[i].flow += tmp;
					edge[i ^ 1].flow -= tmp;
					return tmp;
				}
			}
		}
		return 0;
	}

	void run() {
		maxFlow = 0;
		while (bfs()) {	
			FOR(i, n) used[i] = hd[i];
			int f = 1;
			while (f) {
				f = dfs(s, INF);
				maxFlow += f;
			}
		}
	}

}G;

struct Node {
	int x1, y1, x2, y2;

	void init(int a, int b, int c, int d) {
		x1 = a, y1 = b, x2 = c, y2 = d;
	}
}nodes[20];

int n, m;
int tot;

int mat[105][505];
int mat2[105][505];

bool ok(int x, int y) {
	bool tmp = x >= 0 && x < n && y >= 0 && y < m;

	if (tmp) {

		for (int i = 0; i < tot; i++) {
			if (x >= nodes[i].x1 && x <= nodes[i].x2 && y >= nodes[i].y1 && y <= nodes[i].y2) {
				return 0;	
			}
		}
		return 1;
	}
	else return 0;
}

int dx[] = {0, 0, -1, 1};
int dy[] = {-1, 1, 0, 0};

int main() {
	int test, a, b, c, d;
	scanf("%d", &test);

	for (int cas = 1; cas <= test; cas++) {
		scanf("%d%d%d", &n, &m, &tot);

		for (int i = 0; i < tot; i++) {
			scanf("%d%d%d%d", &a, &b, &c, &d);
			nodes[i].init(a, b, c, d);
		}		

		int id = 0;

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				mat[i][j] = id++;
				mat2[i][j] = id++;
			}
		}	

		int ss = id++, tt = id++;

		G.init(id, ss, tt);

		for (int i = 0; i < n; i++) {
			G.addEdge(ss, mat[i][0], 1);
			G.addEdge(mat2[i][m - 1], tt, 1);
		}		

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				G.addEdge(mat[i][j], mat2[i][j], 1);
			}
		}

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (ok(i, j)) {
					for (int k = 0; k < 4; k++) {
						int tx = i + dx[k], ty = j + dy[k];
						if (ok(tx, ty)) {
							G.addEdge(mat2[i][j], mat[tx][ty], 1);		
						}
					}					
				}			
			}
		}

		G.run();

		printf("Case #%d: %d\n", cas, G.maxFlow);	
	}
	return 0;
}
