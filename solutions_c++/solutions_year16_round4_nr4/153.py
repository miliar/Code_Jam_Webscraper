#include <iostream>
#include <cstdio>
using namespace std;
int n, ans, t;
char s[30][30];
int f[100];
int F(int x) {
	return f[x] != x ? f[x] = F(f[x]) : x;
}

void U(int x, int y) {
	x = F(x);
	y = F(y);
	f[x] = y;
}
bool check() {
	for (int i = 0; i < 2 * n; i++) {
		f[i] = i;
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (s[i][j] == '1') {
				U(i, j + n);
			}
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (F(i) == F(j + n) && s[i][j] == '0') {
				return false;
			}
		}
	}
	int a[100] = {}, b[100] = {};
	for (int i = 0; i < n; i++) {
		a[F(i)]++;
	}
	for (int i = n; i < 2 * n; i++) {
		b[F(i)]++;
	}
	for (int i = 0; i < 2 * n; i++) {
		if (a[i] != b[i]) {
			return false;
		}
	}
	return true;
}

void dfs(int x, int y, int c) {
	if (x == n && y == 0) {
		if (check()) {
//			for (int i = 0; i < n; i++) {
//				printf("%s\n", s[i]);
//			}
			ans = min(ans, c);
		}
		return;
	}
	int nx = x;
	int ny = y + 1;
	if (ny == n) {
		nx++;
		ny = 0;
	}
	dfs(nx, ny, c);
	if (s[x][y] == '0') {
		s[x][y] = '1';
		dfs(nx, ny, c + 1);
		s[x][y] = '0';
	}
}


int main() {
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++) {
		scanf("%d", &n);
		ans = n * n;
		for (int i = 0; i < n; i++) {
			scanf("%s", s[i]);
		}
		dfs(0, 0, 0);
		printf("Case #%d: %d\n", tt, ans);
	}
}