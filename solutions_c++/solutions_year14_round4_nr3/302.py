#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tag_and_trait.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <functional>
#include <iostream>
#include <iterator>
#include <vector>

template<typename key, typename value> class ext_map: public __gnu_pbds::tree<
		key, value, std::less<key>, __gnu_pbds ::rb_tree_tag,
		__gnu_pbds ::tree_order_statistics_node_update> {
};
using namespace std;

const int MAX_DIST = 0x7f7f7f7f;
const int MAXV = 1000000;
const int MAXE = 2000000;
typedef int flow_type;
const int MAX_FLOW = 19930309;
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
	top = pool, memset(adj, 0, sizeof adj);
	S = s, T = t;
}
void add_edge(int u, int v, flow_type c, flow_type bc = 0) {
//	cout << u << "," << v << endl;
	top->v = v, top->c = c, top->n = adj[u], adj[u] = top++;
	top->v = u, top->c = bc, top->n = adj[v], adj[v] = top++;
	adj[u]->b = adj[v], adj[v]->b = adj[u];
}
int d[MAXV];
int q[MAXV];
int qh, qt;
bool relabel() {
	memset(d, MAX_DIST, sizeof d), d[q[qh = qt = 0] = T] = 0;
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
		if (i->c && d[u] == d[i->v] + 1)
			if (flow_type df = augment(i->v, min(e, i->c)))
				i->c -= df, i->b->c += df, e -= df, f += df;
		if (!e)
			break;
	}
	return f;
}
flow_type dinic() {
	flow_type f = 0;
	while (relabel())
		memcpy(cur, adj, sizeof cur), f += augment(S, MAX_FLOW);
	return f;
}

int dx[] = { -1, 1, 0, 0 };
int dy[] = { 0, 0, -1, 1 };
int x0[10000], y0[10000], x1[10000], y1[10000];
int g[1000][4000];

int main() {
	freopen("src/out.txt", "w", stdout);
	int TC;
	scanf("%d", &TC);
	for (int t = 1; t <= TC; t++) {
		printf("Case #%d: ", t);
		int W, H, B;
		scanf("%d%d%d", &W, &H, &B);
		for (int i = 0; i < B; i++) {
			scanf("%d%d%d%d", x0 + i, y0 + i, x1 + i, y1 + i);
		}

//		vector<int> ys;
//		for (int i = 0; i < B; i++) {
//			if (y0[i] - 1 >= 0)
//				ys.push_back(y0[i] - 1);
//			ys.push_back(y0[i]);
//			ys.push_back(y1[i]);
//			if (y1[i] + 1 < H)
//				ys.push_back(y1[i] + 1);
//		}
//		sort(ys.begin(), ys.end());
//		ys.erase(unique(ys.begin(), ys.end()), ys.end());
//		for (int i = 0; i < B; i++) {
//			y0[i] = lower_bound(ys.begin(), ys.end(), y0[i]) - ys.begin();
//			y1[i] = lower_bound(ys.begin(), ys.end(), y1[i]) - ys.begin();
//		}
//		H = ys.size();

//		for (int i = 0; i < B; i++) {
//			cout << x0[i] << "," << y0[i] << "," << x1[i] << "," << y1[i]
//					<< endl;
//		}
		memset(g, 0, sizeof g);
		for (int i = 0; i < B; i++) {
			for (int x = x0[i]; x <= x1[i]; x++) {
				for (int y = y0[i]; y <= y1[i]; y++) {
					g[x][y] = 1;
				}
			}
		}
//		cout << W << "<>" << H << endl;
//		for (int i = 0; i < W; i++) {
//			for (int j = 0; j < H; j++)
//				cout << g[i][j];
//			cout << endl;
//		}
		build_graph(H * W * 2, H * W * 2 + 1);
//		cout << S << ":" << T << endl;
		for (int i = 0; i < W; i++) {
			for (int j = 0; j < H; j++)
				if (!g[i][j]) {
					add_edge(i * H + j, H * W + i * H + j, 1);
					for (int d = 0; d < 4; d++) {
						int ni = i + dx[d];
						int nj = j + dy[d];
						if (ni >= 0 && nj >= 0 && ni < W && nj < H) {
							if (!g[ni][nj]) {
								add_edge(H * W + i * H + j, ni * H + nj,
										19930309);
							}
						}
					}
					if (j == 0) {
						add_edge(S, i * H + j, 1);
					}
					if (j == H - 1) {
						add_edge(H * W + i * H + j, T, 1);
					}
				}
		}
		printf("%d\n", dinic());
	}
}
