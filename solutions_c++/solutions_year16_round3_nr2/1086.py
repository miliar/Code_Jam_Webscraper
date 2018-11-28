#include <bits/stdc++.h>
using namespace std;

int B;
long long M;
int a[50][50];
long long memo[50];
bool f, ff;

void ok() {
	puts("POSSIBLE");
	for (int i = 0; i < B; ++i) {
		for (int j = 0; j < B; ++j) {
			printf("%d", a[i][j]);
		}
		puts("");
	}
}
void ng() {
	puts("IMPOSSIBLE");
}

void init() {
	f = false;
	for (int i = 0; i < B; ++i) memo[i] = 0;
}

long long dfs(int cur) {
	if (memo[cur]) return memo[cur];
	if (cur == B-1) return 1;
	long long &ret = memo[cur];
	for (int i = cur+1; i < B; ++i) {
		if (a[cur][i]) ret += dfs(i);
	}
	if (!ret) f = true;
	return ret;
}

void rec(int y, int x) {
	if (ff) return;
	if (y == B-1) {
		init();
		long long m = dfs(0);
		if (!f && m == M) {
			ff = true;
			ok();
		}
		return;
	}

	if (x == B-1) {
		rec(y+1, y+2);
	} else {
		rec(y, x+1);
	}

	a[y][x] = 1;

	if (x == B-1) {
		rec(y+1, y+2);
	} else {
		rec(y, x+1);
	}

	a[y][x] = 0;
}

void solve() {
	scanf("%d%lld", &B, &M);
	ff = false;
	rec(0, 1);
	if (!ff) ng();
}

int main() {
	int T; scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
