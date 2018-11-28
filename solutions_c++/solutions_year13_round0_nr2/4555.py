#include <map>
#include <set>
#include <list>
#include <cmath>
#include <queue>
#include <stack>
#include <bitset>
#include <vector>
#include <cstdio>
#include <string>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
#define PB push_back
#define MP make_pair
#define SZ(v) ((int)(v).size())
#define abs(x) ((x) > 0 ? (x) : -(x))
typedef long long LL;

#define MAXN 20005
struct Graph {
	int n, depth, size;
	int dfn[MAXN], low[MAXN], id[MAXN];
	bool vis[MAXN];
	vector<int> adj[MAXN];
	stack<int> S;

	void init(int n) {
		this->n = n;
		for (int i = 0; i <= 2 * n; i++)
			adj[i].clear();
		memset(dfn, -1, sizeof(dfn));
		memset(low, 0, sizeof(low));
		memset(vis, false, sizeof(vis));
		memset(id, 0, sizeof(id));
		while (!S.empty()) S.pop();
	}

	void addEdge(int a, int b) {
		//cout << a << " " << b << endl;
		adj[a].PB(b);
	}

	void Tarjan(int u) {
		dfn[u] = low[u] = depth++;
		S.push(u);
		vis[u] = true;
		for (int i = 0; i < adj[u].size(); i++) {
			int v = adj[u][i];
			if (dfn[v] == -1) {
				Tarjan(v);
				low[u] = min(low[u], low[v]);
			} else if (vis[v]) {
				low[u] = min(low[u], dfn[v]);
			}
		}
		if (low[u] == dfn[u]) {
			size++;
			int v;
			do {
				v = S.top();
				S.pop();
				id[v] = size;
				vis[v] = false;
			} while (u != v);
		}
	}

	bool twosat() {
		depth = 1; size = 0;
		for (int i = 0; i < 2 * n; i++)
			if (dfn[i] == -1) Tarjan(i);
		for (int i = 0; i < n; i++)
			if (id[i] == id[i + n]) return false;
		return true;
	}

}g;

int n, m;
int mat[111][111];

int getID(int x, int y) {
	return x * m + y;
}

int main(int argc, char const *argv[])
{
	int Test;
	cin >> Test;
	for (int cas = 1; cas <= Test; cas++) {
		printf("Case #%d: ", cas);
		cin >> n >> m;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				cin >> mat[i][j];
			}
		}
		g.init(n * m);
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				int x = mat[i][j];
				for (int k = 0; k < m; k++) {
					if (mat[i][k] > x) {
						g.addEdge(getID(i, k), getID(i, j) + n * m);
						g.addEdge(getID(i, j), getID(i, j) + n * m);
					}
				}
			}
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				int x = mat[i][j];
				for (int k = 0; k < n; k++) {
					if (mat[k][j] > x) {
						g.addEdge(getID(k, j) + n * m, getID(i, j));
						g.addEdge(getID(i, j) + n * m, getID(i, j));
					}
				}
			}
		}
		printf("%s\n", g.twosat() ? "YES" : "NO");
	}
	return 0;
}