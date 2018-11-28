#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <cmath>
#include <algorithm>

using namespace std;
const int N = 110;
char a[N][N];
int l[N][N], r[N][N], d[N][N], u[N][N];

int main() {
    int cas = 0, n, m, x;
	scanf("%d", &x);
	while (x--) {
		scanf("%d%d", &n, &m);
		for (int i = 1; i <= n; i++)
			scanf("%s", a[i] + 1);
		memset(l, 0, sizeof(l));
		memset(r, 0, sizeof(r));
		memset(u, 0, sizeof(u));
		memset(d, 0, sizeof(d));
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++) {
				l[i][j] = l[i][j - 1];
				u[i][j] = u[i - 1][j];
				if (a[i][j] != '.') {
					l[i][j] ++;
					u[i][j]++;
				}
			}
		for (int i = n; i >= 1; i--)
			for (int j = m; j >= 1; j--) {
				r[i][j] = r[i][j + 1];
				d[i][j] = d[i + 1][j];
				if (a[i][j] != '.') {
					r[i][j] ++;
					d[i][j]++;
				}
			}
		int ans = 0;
		bool flag = true;
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++)
				if (a[i][j] != '.') {
					if (u[i][j] == 1 && l[i][j] == 1 && r[i][j] == 1 && d[i][j] == 1)
					{
						flag = false;
						break;
					}
					if (a[i][j] == '<' && l[i][j] == 1) ans++;
					if (a[i][j] == '>' && r[i][j] == 1) ans++;
					if (a[i][j] == 'v' && d[i][j] == 1) ans++;
					if (a[i][j] == '^' && u[i][j] == 1) ans++;
				}
		printf("Case #%d: ", ++cas);
		if (!flag) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
		
    }
    return 0;
}
