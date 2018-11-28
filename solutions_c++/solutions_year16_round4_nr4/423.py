#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>

using namespace std;

const int N = 4;

int a[N][N], b[N][N];
int p[N];
int used[N];
int testCases, n, ans;

bool check(int p[], int k) {
	if (k == n) {
		return true;
	}
	int flag = 0;
	for (int i = 0; i < n; ++i) {
		if (b[p[k]][i] && !used[i]) {
			flag = 1;
			used[i] = 1;
			if (!check(p, k + 1)) {
				return false;
			}
			used[i] = 0;
		}
	}
	return flag;
}

void update(int cnt) {
	for (int i = 0; i < n; ++i) {
		p[i] = i;
	}
	do {
		memset(used, 0, sizeof used);
		if (!check(p, 0)) {
			return;
		}
	} while (next_permutation(p, p + n));
/*
	cerr << cnt << endl;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			cerr << b[i][j];
		}
		cerr << endl;
	}
	cerr << endl;
*/
	ans = min(ans, cnt);
}

void dfs(int i, int j, int cnt) {
	if (i == n) {
		update(cnt);
		return;
	}
	if (j == n) {
		dfs(i + 1, 0, cnt);
		return;
	}
	if (a[i][j] == 1) {
		b[i][j] = 1;
		dfs(i, j + 1, cnt);
	} else {
		b[i][j] = 0;
		dfs(i, j + 1, cnt);
		b[i][j] = 1;
		dfs(i, j + 1, cnt + 1);
	}
}

int main() {
	scanf("%d", &testCases);
	for (int _ = 1; _ <= testCases; ++_) {
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			char s[N + 5];
			scanf("%s", s);
			for (int j = 0; j < n; ++j) {
				a[i][j] = s[j] == '1';
			}
		}
		ans = n * n;
		dfs(0, 0, 0);
		printf("Case #%d: %d\n", _, ans);
	}
	return 0;
}
