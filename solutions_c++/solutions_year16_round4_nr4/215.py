#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;
typedef long long ll;

char buf[32];
int mat[32][32], fa[64], G[32][32];
vector<int> uni[64][2];
void init(int n) {
	memset(G, 0, sizeof(G));
	int m = 2 * n;
	for (int i = 0; i < m; ++i) {
		fa[i] = i;
	}
	for (int i = 0; i < m; ++i) {
		for (int d = 0; d < 2; ++d) {
			uni[i][d].clear();
		}
	}
}

int findPr(int x) {
	return fa[x] == x ? x : (fa[x] = findPr(fa[x]));
}

void link(int u, int v) {
	G[u][v] = G[v][u] = 1;
	int fu = findPr(u);
	int fv = findPr(v);
	if (fu != fv) {
		fa[fu] = fv;
	}
}

int main() {
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D.out", "w", stdout);
	int _, cas = 1;
	scanf("%d", &_);
	while (_--) {
		printf("Case #%d: ", cas);
		++cas;

		int n;
		int curs = 0;
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			scanf("%s", buf);
			for (int j = 0; j < n; ++j) {
				if (buf[j] == '0') {
					mat[i][j] = 0;
				} else {
					mat[i][j] = 1;
					curs |= (1 << (i * n + j));
				}
			}
		}
		int edges = n * n;
		int m = 2 * n;
		int maxs = (1 << edges), adds;
		int ans = edges + 10;
		for (int s = 0; s < maxs; ++s) {
			if ((s & curs) != curs) continue;
			adds = s ^ curs;
			int cnt = 0;
			init(n);
			for (int i = 0; i < n; ++i) {
				for (int j = 0; j < n; ++j) {
					int e = i * n + j;
					if (s & (1 << e)) link(i, j + n);
					if (adds & (1 << e)) ++cnt;
				}
			}
			for (int i = 0; i < n; ++i) {
				int fi = findPr(i);
				uni[fi][0].push_back(i);
			}
			for (int i = n; i < m; ++i) {
				int fi = findPr(i);
				uni[fi][1].push_back(i);
			}
			bool flag = true;
			for (int i = 0; i < m && flag; ++i) {
				if (uni[i][0].size() == 0 && uni[i][1].size() == 0) continue;
				if (uni[i][0].size() != uni[i][1].size()) {
					flag = false;
					break;
				}
				int nn = uni[i][0].size();
				for (int k0 = 0; k0 < nn && flag; ++k0) {
					for (int k1 = 0; k1 < nn && flag; ++k1) {
						if (G[uni[i][0][k0]][uni[i][1][k1]] == 0) {
							flag = false;
							break;
						}
					}
				}
			}
			if (flag) {
				ans = min(ans, cnt);
			}
		}
		printf("%d\n", ans);
	}
	return 0;
}