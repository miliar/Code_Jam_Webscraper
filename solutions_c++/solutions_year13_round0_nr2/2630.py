#include <iostream>
#include <stdio.h>
using namespace std;
#define SIZE 105
int a[SIZE][SIZE];
int b[SIZE][SIZE];
int n, m;
void input()
{
	for (int i = 0; i < n; ++i) {
		for (int j =  0; j < m; ++j) {
			scanf("%d", &a[i][j]);
		}
	}
}
int ok(int x, int y)
{
	int ans = 0;
	int flg = 1;
	for (int i = 0; i < m; i++) {
		if (a[x][i] != 1) {
			flg = 0;
			break;
		}
	}
	if (flg) {
		for (int i = 0; i < m; ++i) {
			b[x][i] = 1;
		}
	}
	ans += flg;
	flg = 1;
	for (int i = 0; i < n; ++i) {
		if (a[i][y] != 1) {
			flg = 0;
			break;
		}
	}
	if (flg) {
		for (int i = 0; i < n; ++i) {
			b[i][y] = 1;
		}
	}
	ans += flg;
	return ans;
}
int solve()
{
	for (int i = 0; i < n; ++i) {
		if (a[i][0] == 1) {
			if (!ok(i, 0)) {
				return 0;
			}
		}
	}
	for (int i = 0; i < m; ++i) {
		if (a[0][i] == 1) {
			if (!ok(0, i)) {
				return 0;
			}
		}
	}
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			if (a[i][j] == 1 && b[i][j] != 1) {
				return 0;
			} 
		}
	}
	return 1;
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		memset(b, 0, sizeof(b));
		scanf("%d %d", &n, &m);
		input();
		int ans = solve();
		if (ans) {
			printf("Case #%d: YES\n", i);
		} else {
			printf("Case #%d: NO\n", i);
		}
	}
	return 0;
}