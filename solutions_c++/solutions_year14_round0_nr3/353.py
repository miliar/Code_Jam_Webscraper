#include <cstdio>
#include <cstring>
int r, c, m;
char ans[50][50];
void solve() {
	scanf("%d%d%d", &r, &c, &m);
	int sw = 0;
	if (r > c) r ^= c, c ^= r, r ^= c, sw = 1;
	m = r * c - m;
	memset(ans, '*', sizeof ans);
	if (r == 1) {
		for (int i = 1; i < m; i++) ans[0][i] = '.';
		ans[0][0] = 'c';
	} else if (m == 1) {
		ans[0][0] = 'c';
	} else if (m == 2 || m == 3 || m == 5 || m == 7 || r == 2 && m & 1) {
		puts("Impossible");
		return;
	} else if (!(m & 1) && m <= 2 * r) {
		for (int i = 0; i < m/2; i++)
			ans[i][0] = ans[i][1] = '.';
		ans[0][0] = 'c';
	} else if (m & 1 && m <= 2 * r + 3) {
		for (int i = 0; i < (m-3)/2; i++)
			ans[i][0] = ans[i][1] = '.';
		ans[0][2] = ans[1][2] = ans[2][2] = '.';
		ans[0][0] = 'c';
	} else {
		for (int i = 0; i < r; i++)
			for (int j = 0; j < m/r; j++)
				ans[i][j] = '.';
		if (m % r == 1) ans[0][m/r] = ans[1][m/r] = '.', ans[r-1][m/r-1] = '*';
		else
			for (int i = 0; i < m%r; i++)
				ans[i][m/r] = '.';
		ans[0][0] = 'c';
	}
	if (sw) {
		for (int i = 0; i < c; puts(""), i++)
			for (int j = 0; j < r; j++) putchar(ans[j][i]);
	} else {
		for (int i = 0; i < r; puts(""), i++)
			for (int j = 0; j < c; j++) putchar(ans[i][j]);
	}
}
int main() {
	int T; scanf("%d", &T);
	for (int _ = 1; _ <= T; _++)
		printf("Case #%d:\n", _), solve();
	return 0;
}
