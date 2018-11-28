#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 1005;

struct edge {
	int v, next;
}G[N << 1];

int a[N], link[N], visit[N], mcnt;

void addedge(int x, int y) {
	G[mcnt].v = y; G[mcnt].next = link[x]; link[x] = mcnt++;
}

int dfs(int x, int y, int d) {
	int h = d;
	visit[x] = 1;
	for (int i = link[x]; i != -1; i = G[i].next) {
		if (G[i].v == y) continue;
		if (visit[G[i].v]) continue;
		h = max(h, dfs(G[i].v, y, d + 1));
	}
	return h;
}

int main() {
	freopen("1.txt", "r", stdin);
	freopen("2.txt", "w", stdout);
	int T, ca = 0;
	scanf("%d", &T);
	while (T--) {
		memset(link, -1, sizeof(link));
		mcnt = 0;
		int n;
		scanf("%d", &n);
		for (int i = 1; i <= n; ++i) {
			scanf("%d", &a[i]);
			addedge(a[i], i);
		}
		int ans = 0, res = 0;
		for (int i = 1; i <= n; ++i) {
			int tmp = i;
			memset(visit, 0, sizeof(visit));
			visit[tmp] = 1;
			while (!visit[a[tmp]]) {
				visit[a[tmp]] = visit[tmp] + 1;
				tmp = a[tmp];
			}
			if (a[tmp] != i) continue;
			int len = visit[tmp] - visit[a[tmp]] + 1;
			ans = max(ans, len);
			if (len == 2 && i < a[i]) {
				memset(visit, 0, sizeof(visit));
				res += 2 + dfs(tmp, a[tmp], 0);
				memset(visit, 0, sizeof(visit));
				res += dfs(a[tmp], tmp, 0);
			}
		}
		ans = max(ans, res);
		printf("Case #%d: %d\n", ++ca, ans);
	}
	return 0;
}

