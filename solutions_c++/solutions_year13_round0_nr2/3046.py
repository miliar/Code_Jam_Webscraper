#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int num[11111], len;
int col[100], row[100];
int g[100][100];

int main() {
	int test; scanf("%d", &test);
	for (int cas = 1; cas <= test; ++cas) {
		int n, m; scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j) {
				scanf("%d", &g[i][j]);
				num[i * m + j] = g[i][j];
			}
		sort(num, num + n * m);
		len = unique(num, num + n * m) - num;
		for (int i = 0; i < len - 1; ++i) {
			for (int j = 0; j < n; ++j) row[j] = 0;
			for (int k = 0; k < m; ++k) col[k] = 0;
			for (int j = 0; j < n; ++j)
				for (int k = 0; k < m; ++k) {
					if (g[j][k] == num[i]) {
						row[j]++;
						col[k]++;
					}
				}
			for (int j = 0; j < n; ++j)
				if (row[j] == m)
					for (int h = 0; h < m; ++h)
						g[j][h] = num[i + 1];
			for (int k = 0; k < m; ++k)
				if (col[k] == n)
					for (int h = 0; h < n; ++h)
						g[h][k] = num[i + 1];
		}
		int fn = g[0][0]; bool fg = true;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				if (fg && g[i][j] != fn)
					fg = false;
		printf("Case #%d: %s\n", cas, fg ? "YES" : "NO");
	}
	return 0;
}
