#pragma comment(linker, "/STACK:1000000000")
#include <cstdio>
#include <iostream>
#include <ctime>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <set>
#include <map>
#include <queue>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <bitset>
#include <deque>
#include <stack>
#include <climits>
#include <string>
#include <numeric>
#include <memory.h>
#define mp make_pair
#define pii pair <int, int>
#define ll long long
#define ui unsigned int
#define ld double
#define pll pair <ll, ll> 
 
using namespace std;

const int maxn = 100;

int v[maxn];

int n, m;

char c[maxn][maxn];

int getr(int x, int y) {
	if (x < 0) {
		return y + 1;
	}

	if (y == m) {
		return x + 1 + m;
	}

	if (x == n) {
		return n + m + (m - y);
	}

	return n + m + m + (n - x);
}

int dfs(int x, int y, int tp) {
	//cout << x << ' ' << y << ' ' << tp << endl;
	if (x < 0 || x == n || y < 0 || y == m) {
		return getr(x, y);
	}

	if (tp == 0) {
		if (c[x][y] == '/') {
			y--;
			tp = 3;
		} else {
			y++;
			tp = 1;
		}
	} else if (tp == 1) {
		if (c[x][y] == '/') {
			tp = 2;
			x--;
		} else {
			tp = 0;
			x++;
		}
	} else if (tp == 2) {
		if (c[x][y] == '/') {
			tp = 1;
			y++;
		} else {
			tp = 3;
			y--;
		}
	} else {
		if (c[x][y] == '/') {
			tp = 0;
			x++;
		} else {
			tp = 2;
			x--;
		}
	}

	return dfs(x, y, tp);
}

int now[maxn];

bool correct() {
	for (int i = 1; i <= m; i++) {
		now[i] = dfs(0, i - 1, 0);
	}

	for (int i = m + 1; i <= n + m; i++) {
		now[i] = dfs(i - m - 1, m - 1, 3);
	}

	for (int i = n + m + 1; i <= n + m + m; i++) {
		now[i] = dfs(n - 1, n + 2 * m - i, 2);
	}

	for (int i = n + 2 * m + 1; i <= 2 * m + 2 * n; i++) {
		now[i] = dfs(2 * n + 2 * m - i, 0, 1);
	}
	/*
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cout << c[i][j];
		}
		cout << endl;
	}

	for (int i = 1; i <= 2 * (n + m); i++) {
		cout << now[i] << ' ';
	}

	cout << endl;
	*/
	for (int i = 1; i <= 2 * (n + m); i++) {
		if (v[i] != now[i]) {
			return false;
		}
	}

	return true;
}

bool gen(int x, int y) {
	if (x == n) {
		x = 0;
		y++;
	}

	if (y == m) {
		if (correct()) {
			return true;
		}

		return false;
	}

	c[x][y] = '/';

	if (gen(x + 1, y)) {
		return true;
	}

	c[x][y] = '\\';

	return gen(x + 1, y);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;

	cin >> t;

	int ts = 0;

	while (t--) {
		ts++;

		scanf("%d %d", &n, &m);

		for (int i = 0; i < 2 * (n + m); i += 2) {
			int a, b;

			scanf("%d %d", &a, &b);

			v[a] = b;
			v[b] = a;
		}

		printf("Case #%d:\n", ts);

		if (gen(0, 0)) {
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					printf("%c", c[i][j]);
				}
				printf("\n");
			}
		} else {
			printf("IMPOSSIBLE\n");
		}
	}

	return 0;
}
