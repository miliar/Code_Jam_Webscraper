#include <iostream>
#include <cstdio>
using namespace std;
int t, r, c;
int a[100], b[100];
char s[100][100];
int f[10000];
int F(int x) {
	return f[x] != x ? f[x] = F(f[x]) : x;
}
void U(int x, int y) {
	x = F(x);
	y = F(y);
	f[x] = y;
}
int pot(int x, int y, int z) {
	return x * (c + 1) + y + z * (c + 1) * (r + 1);
}

int conv(int t) {
	if (1 <= t && t <= c) {
		return pot(0, t - 1, 0);
	} else if (c < t && t <= c + r) {
		return pot(t - c - 1, c + 1, 1);
	} else if (c + r < t && t <= c + r + c) {
		return pot(r + 1, c - 1 - (t - c - r - 1), 0);
	} else {
		return pot(r - 1 - (t - c - r - c - 1), 0, 1);
	}
}
bool check() {
	for (int i = 0; i < 2 * (r + 1) * (c + 1); i++) {
		f[i] = i;
	} 
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			if (s[i][j] == '/') {
				U(pot(i, j, 0), pot(i, j, 1));
				U(pot(i + 1, j, 0), pot(i, j + 1, 1));
			} else {
				U(pot(i, j, 1), pot(i + 1, j, 0));
				U(pot(i, j, 0), pot(i, j + 1, 1));
			}
		}
	}
	for (int i = 0; i < r + c; i++) {
		printf("%d %d\n", conv(a[i]), conv(b[i]));
		if (F(conv(a[i])) != F(conv(b[i]))) {
			return false;
		}
	}
	return true;
}
bool dfs(int x, int y) {
	if (x == r && y == 0) {
		if (check()) {
			return true;
		}
		return false;
	}
	int nx = x;
	int ny = y + 1;
	if (ny == c) {
		nx++;
		ny = 0;
	}
	s[x][y] = '/';
	if (dfs(nx, ny)){
		return true;
	}
	s[x][y] = '\\';
	if (dfs(nx, ny)) {
		return true;
	}
	return false;
}

int main() {
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++) {
		scanf("%d%d", &r, &c);
		memset(s, 0, sizeof s);
		for (int i = 0; i < r + c; i++) {
			scanf("%d%d", &a[i], &b[i]);
		}
		printf("Case #%d:\n", tt);
		if (dfs(0, 0)) {
			for (int i = 0; i < r; i++) {
				printf("%s\n", s[i]);
			}
		} else {
			printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}