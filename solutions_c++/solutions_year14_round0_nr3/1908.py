#include <iostream>
#include <stdio.h>
using namespace std;
double eps = 1e-8;
int a[10][10];
int n, m, r;
bool visited[6][6];
int dir[8][2] = { 0, 1, 1, 0, 0, -1, -1, 0, 1, 1, 1, -1, -1, 1, -1, -1 };
int dfs(int i, int j) {
	int k;
	if (i < 0 || j < 0 || i >= n || j >= m)
		return 0;
	if (a[i][j] == -1)
		return 0;
	if (visited[i][j])
		return 0;
	visited[i][j] = 1;
	if (a[i][j] != 0)
		return 1;
	int ret = 1;
	for (k = 0; k < 8; ++k) {
		ret += dfs(i + dir[k][0], j + dir[k][1]);
	}
	return ret;
}
bool check() {
	int i, j, k, ii, jj;
	memset(visited, false, sizeof(visited));
	for (i = 0; i < n; ++i) {
		for (j = 0; j < m; ++j) {
			if (a[i][j] == 0) {
				for (k = 0; k < 8; ++k) {
					ii = i + dir[k][0];
					jj = j + dir[k][1];
					if (ii < 0 || jj < 0 || ii >= n || jj >= m)
						continue;
					if (a[ii][jj] == -1)
						a[i][j]++;
				}
			}
		}
	}
	for (i = 0; i < n; ++i) {
		for (j = 0; j < m; ++j) {
			if (a[i][j] == 0) {
				int cn = dfs(i, j);
				a[i][j] = -2;
				if (cn == n * m - r)
					return true;
				return false;
			}
		}
	}
	for (i = 0; i < n; ++i) {
		for (j = 0; j < m; ++j) {
			if (a[i][j] != -1) {
				int cn = dfs(i, j);
				a[i][j] = -2;
				if (cn == n * m - r)
					return true;
				return false;
			}
		}
	}
	return false;
}
int main() {
	int t, cas = 0;
	int i, j, k;
	scanf("%d", &t);
	while (t--) {
		cas++;
		scanf("%d%d%d", &n, &m, &r);
		bool flag = false;
		for (i = 0; i < (1 << (n * m)); ++i) {
			k = 0;
			for (j = 0; j < (n * m); ++j) {
				if (i & (1 << j))
					k++;
			}
			if (k == r) {
				for (j = 0; j < (n * m); ++j) {
					a[j / m][j % m] = -((i >> j) & 1);
				}
				if (check()) {
					flag = true;
					break;
				}
			}
		}
		printf("Case #%d:\n", cas);
		if (flag == false) {
			puts("Impossible");
			continue;
		}
		for (i = 0; i < n; ++i) {
			for (j = 0; j < m; ++j) {
				if (a[i][j] == -1) {
					printf("*");

				} else if (a[i][j] == -2)
					printf("c");
				else
					printf(".");
			}
			puts("");
		}
	}
}
