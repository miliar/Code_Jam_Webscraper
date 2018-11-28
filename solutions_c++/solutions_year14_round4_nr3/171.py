#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>

using namespace std;

const int maxn = 1005;

int dis[maxn];
bool vis[maxn];
int g[maxn][maxn];

struct rect {
	int x, y, X, Y;

	void init() {
		scanf("%d%d%d%d", &x, &y, &X, &Y); X++; Y++;
	}

	int dist(const rect& a) const {
		int dx, dy;
		if (a.x > X) dx = a.x - X;
		else if (a.X < x) dx = x - a.X;
		else dx = 0;
		if (a.y > Y) dy = a.y - Y;
		else if (a.Y < y) dy = y - a.Y;
		else dy = 0;
		return max(dx, dy);
	}
} r[maxn];

void work() {
    int w, h, n; scanf("%d%d%d", &w, &h, &n);
    r[0].x = 0; r[0].y = 0; r[0].X = 0; r[0].Y = h;
    for (int i = 1; i <= n; ++i) r[i].init();
    n++; r[n].x = w; r[n].y = 0; r[n].X = w; r[n].Y = h;

    memset(vis, 0, sizeof(vis));
    int k = 0; dis[k] = 0; vis[k] = true;

    for (int i = 0; i <= n; ++i)
		for (int j = 0; j <= n; ++j)
			g[i][j] = r[i].dist(r[j])/*, printf("%d, %d -> %d\n", i, j, g[i][j])*/;
	for (int i = 1; i <= n; ++i) dis[i] = g[k][i];

    while (true) {
		if (k == n) break;
		for (int i = 1; i <= n; ++i) if (!vis[i])
			if (vis[k] || dis[i] < dis[k]) k = i;
		vis[k] = true; //printf("dis[%d] = %d\n", k, dis[k]);
		for (int i = 1; i <= n; ++i) if (!vis[i])
			dis[i] = min(dis[i], dis[k] + g[k][i]);
    }

	printf("%d\n", dis[n]);
}

int main() {
	int T; scanf("%d", &T);

	for (int t = 1; t <= T; ++t) {
		printf("Case #%d: ", t);
		work();
	}

	return 0;
}
