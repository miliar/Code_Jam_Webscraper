#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int dx[4] = {0, 0, 1, -1}, dy[4] = {1, -1, 0, 0};
const int maxn = 111;

int g[maxn][maxn];
int cl[maxn], cr[maxn];
char buf[maxn];

int dir(char x) {
	if (x == '^') return 3;
	if (x == '<') return 1;
	if (x == '>') return 0;
	if (x == 'v') return 2;
}

void work() {
	int m, n;  scanf("%d%d", &m, &n);

	memset(cl, 0, sizeof(cl));
	memset(cr, 0, sizeof(cr));
	for (int i = 0; i < m; ++i) {
		scanf("%s", buf);
		for (int j = 0; j < n; ++j) {
			if (buf[j] == '.') g[i][j] = -1;
			else {
				g[i][j] = dir(buf[j]);
				cl[i]++; cr[j]++;
			}
		}
	}

	for (int i = 0; i < m; ++i)
		for (int j = 0; j < n; ++j)
			if (cl[i] == 1 && cr[j] == 1 && g[i][j] != -1) {
				puts("IMPOSSIBLE"); return ;
			}

	int ans = 0;
	for (int i = 0; i < m; ++i)
		for (int j = 0; j < n; ++j) if (g[i][j] != -1) {
			int d = g[i][j]; int x = i + dx[d], y = j + dy[d];
			bool flag = false;
			while (x >= 0 && x < m && y >= 0 && y < n) {
				if (g[x][y] != -1) {
					flag = true; break;
				}
				x += dx[d]; y += dy[d];
			}

			if (!flag) ans++;
		}

	printf("%d\n", ans);
}

int main() {
	int T; scanf("%d", &T);

	for (int i = 1; i <= T; ++i) {
		printf("Case #%d: ", i);
		work();
	}

	return 0;
}
