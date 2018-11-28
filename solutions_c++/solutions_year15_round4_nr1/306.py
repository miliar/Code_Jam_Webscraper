#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <string>
#include <set>
#include <map>
using namespace std;
#define rep(i, n) for (int i = 0; i < n; i++)
#define kep(i, n) for (int i = 1; i <=n; i++)

int T;

int n, m;
char a[111][111];
const int dx[] = {-1, 0, 1, 0};
const int dy[] = { 0, 1, 0,-1};

int solve() {
	scanf("%d%d\n", &n, &m);
	rep(i, n) {
		scanf("%s", a[i]);
		rep(j, m)
			if (a[i][j] == '^') a[i][j] = 0; else
			if (a[i][j] == '>') a[i][j] = 1; else
			if (a[i][j] == 'v') a[i][j] = 2; else
			if (a[i][j] == '<') a[i][j] = 3; else
				a[i][j] = 4;
	}
	int x, y, count, ans = 0;
	rep(i, n) rep(j, m) if (a[i][j] != 4) {
		count = 0;
		rep(k, 4) {
			x = i+dx[k]; y = j+dy[k];
			while (x >= 0 && y >= 0 && x < n && y < m && a[x][y] == 4) {
				x += dx[k]; y += dy[k];
			}
			if (x >= 0 && y >= 0 && x < n && y < m) {
				count++;
			} else {
				if (k == a[i][j]) {
					ans++;
				}
			}
		}
		if (count == 0) return -1;
	}
	return ans;
}

int main() {
	scanf("%d", &T);
	kep(_, T) {
		printf("Case #%d: ", _);
		int ans = solve();
		if (ans == -1) {
			puts("IMPOSSIBLE");
		} else printf("%d\n", ans);
	}
}
