#include <cstdio>
#include <string>
#include <algorithm>

using namespace std;

int a[16][4][4];
string r[16][4];

void print(int n, int i) {
	if (!n) {
		putchar(i == 0 ? 'R' : i == 1 ? 'P' : 'S');
		return;
	}
	print(n - 1, i);
	print(n - 1, i + 2);
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int i, j, k, tc, tcn;
	scanf("%d", &tcn);
	for (i = 0; i < 3; i++) a[0][i][i] = 1;
	r[0][0] = "R";
	r[0][1] = "P";
	r[0][2] = "S";
	for (i = 1; i <= 12; i++) for (j = 0; j < 3; j++) {
		for (k = 0; k < 3; k++) a[i][j][k] = a[i - 1][j][k] + a[i - 1][(j + 2) % 3][k];
		r[i][j] = min(r[i - 1][j] + r[i - 1][(j + 2) % 3], r[i - 1][(j + 2) % 3] + r[i - 1][j]);
	}
	for (tc = 1; tc <= tcn; tc++) {
		int n, x, y, z;
		scanf("%d%d%d%d", &n, &x, &y, &z);
		for (i = 0; i < 3; i++) if (a[n][i][0] == x && a[n][i][1] == y && a[n][i][2] == z) break;
		if (i == 3) {
			printf("Case #%d: IMPOSSIBLE\n", tc);
			continue;
		}
		printf("Case #%d: %s\n", tc, r[n][i].c_str());
	}
}