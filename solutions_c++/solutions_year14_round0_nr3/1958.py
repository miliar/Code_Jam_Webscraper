//============================================================================
// Name        : codejam.cpp
// Author      : bryant
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>

using namespace std;
const int maxn = 8;
int R, C, M;
int ans = 0;
bool flag;
int Times;
bool g[maxn][maxn];
int gao(int x) {
	int c = 0;
	while (x) {
		x &= x - 1;
		++c;
	}
	return c;
}
int a[maxn][maxn];
bool vis[maxn][maxn];
void dfs(int x, int y) {
	if (x < 1 || x > R || y < 1 || y > C)
		return;
	if (g[x][y])
		return;
	if (vis[x][y] == true)
		return;
	vis[x][y] = true;
	if (a[x][y])
		return;
	dfs(x - 1, y);
	dfs(x + 1, y);
	dfs(x, y + 1);
	dfs(x, y - 1);
	dfs(x - 1, y - 1);
	dfs(x + 1, y + 1);
	dfs(x + 1, y - 1);
	dfs(x - 1, y + 1);
}
bool check() {
	for (int i = 1; i <= R; ++i) {
		for (int j = 1; j <= C; ++j) {
			if (g[i][j] == 0 && !vis[i][j]) {
				//cout << "asdf " << i << " " << j << endl;
				return false;
			}
		}
	}
	return true;
}
bool go() {
	memset(a, 0, sizeof(a));
	for (int i = 1; i <= R; ++i) {
		for (int j = 1; j <= C; ++j) {
			for (int k = -1; k <= 1; ++k) {
				a[i][j] += g[i + k][j - 1] + g[i + k][j] + g[i + k][j + 1];
			}
		}
	}
	memset(vis, false, sizeof(vis));
	for (int i = 1; i <= R; ++i) {
		for (int j = 1; j <= C; ++j) {
			if (a[i][j] == 0) {
				//cout << i << " " << j << endl;
				dfs(i, j);
				return check();
			}
		}
	}
	return false;
}
void print() {
	bool tag = true;
	for (int i = 1; i <= R; ++i) {
		for (int j = 1; j <= C; ++j) {
			if (g[i][j]) {
				cout << "*";
			} else {
				if (tag && a[i][j] == 0) {
					cout << "c";
					tag = false;
				} else {
					cout << ".";
				}
			}
		}
		cout << endl;
	}
}
void out(int st) {
	cout << st << endl;
	for (int i = 1; i <= R; ++i) {
		for (int j = 1; j <= C; ++j) {
			cout << g[i][j];
		}
		cout << endl;
	}
	cout << endl;
}
bool run() {
	int st = R * C;
	int tot = 1 << st;
	memset(g, 0, sizeof(g));
	int k = (1 << 20) - 1 - 2 - 16 - 32 - 1;
	//cout << gao(k) << endl;
	//out(k);
	for (int i = 0; i < tot; ++i) {
		if (gao(i) ^ M)
			continue;
		for (int j = 0; j < st; ++j) {
			g[(j / C) + 1][(j % C) + 1] = (i >> j) & 1;
		}
		//out(i);
		if (go()) {
			print();
			return true;
		}
	}
	return false;
}
int main() {
	ios::sync_with_stdio(false);
	int T;
	freopen("D:\\out.txt", "w", stdout);
	cin >> T;
	for (int cas = 1; cas <= T; ++cas) {
		cout << "Case #" << cas << ":" << endl;
		cin >> R >> C >> M;
		if (!run()) {
			cout << "Impossible" << endl;
		} else {
		}
	}
	return 0;
}
/*
 4
 5 5 23
 3 1 1
 2 2 1
 4 7 3
 */
