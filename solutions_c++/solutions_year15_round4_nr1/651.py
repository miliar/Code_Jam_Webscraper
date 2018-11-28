#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int MAXN = 100+5, MAXM = 10000+5;
const int INF = 0x3f3f3f3f;
int T, R, C, map[MAXN][MAXN];
int e, head[MAXM], next[MAXM], v[MAXM];
char mat[MAXN][MAXN];
struct Arrow {
	int x, y, dx, dy;
} arr[MAXM];
void addedge(int x, int y) {
	v[e] = y;
	next[e] = head[x]; head[x] = e++;
}
bool check(int k) {
	for (int i = 1; i <= R; i++) if (i != arr[k].x) {
		if (mat[i][arr[k].y] != '.')
			return true;
	}
	for (int j = 1; j <= C; j++) if (j != arr[k].y) {
		if (mat[arr[k].x][j] != '.')
			return true;
	}
	return false;
}
int main() {
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		// e = 0;
		// memset(head, -1, sizeof(head));
		printf("Case #%d: ", cas);
		scanf("%d%d", &R, &C);
		// int n = 0;
		for (int i = 1; i <= R; i++) {
			scanf("%s", mat[i]+1);
			// for (int j = 1; j <= C; j++) if (mat[i][j] != '.') {
			// 	map[i][j] = ++n;
			// 	arr[n].x = i, arr[n].y = j;
			// 	if (mat[i][j] == '^') {
			// 		arr[n].dx = -1, arr[n].dy = 0;
			// 	} else if (mat[i][j] == '>') {
			// 		arr[n].dx = 0, arr[n].dy = 1;
			// 	} else if (mat[i][j] == 'v') {
			// 		arr[n].dx = 1, arr[n].dy = 0;
			// 	} else if (mat[i][j] == '<') {
			// 		arr[n].dx = 0, arr[n].dy = -1;
			// 	}
			// }
		}
		bool imp = false;
		int ans = 0;
		for (int i = 1; i <= R; i++)
			for (int j = 1; j <= C; j++) if (mat[i][j] != '.' && !imp) {
				bool flag = false;
				if (mat[i][j] == '^') {
					for (int p = 1; p < i && !flag; p++) if (mat[p][j] != '.')
						flag = true;
				} else if (mat[i][j] == '>') {
					for (int p = j+1; p <= C && !flag; p++) if (mat[i][p] != '.')
						flag = true;
				} else if (mat[i][j] == 'v') {
					for (int p = i+1; p <= R && !flag; p++) if (mat[p][j] != '.')
						flag = true;
				} else if (mat[i][j] == '<') {
					for (int p = 1; p < j && !flag; p++) if (mat[i][p] != '.')
						flag = true;
				}
				if (!flag) {
					for (int p = 1; p <= R && !flag; p++) if (p != i && mat[p][j] != '.')
						flag = true;
					for (int q = 1; q <= C && !flag; q++) if (q != j && mat[i][q] != '.')
						flag = true;
					if (flag)
						ans++;
					else
						imp = true;
				}
			}
		if (imp) {
			printf("IMPOSSIBLE\n");
		} else {
			printf("%d\n", ans);
		}
		// bool flag = true;
		// for (int i = 1; i <= n; i++) {
		// 	flag = flag && check(i);
		// }
		// if (!flag) {
		// 	printf("IMPOSSIBLE\n");
		// } else {
		// 	for (int i = 1; i <= n; i++) {
		// 		int x = arr[i].x+arr[i].dx, y = arr[i].y+arr[i].dy;
		// 		while (1 <= x && x <= R && 1 <= y && y <= C) {
		// 			if (mat[x][y] != '.') {
		// 				addedge(i, map[x][y]);
		// 				break;
		// 			}
		// 			x += arr[i].dx, y += arr[i].dy;
		// 		}
		// 	}
		// 	int ans = 0;
		// 	for (int i = 1; i <= n; i++) {
		// 		if (head[i] == -1)
		// 			ans++;
		// 	}
		// 	printf("%d\n", ans);
		// }
	}
	return 0;
}