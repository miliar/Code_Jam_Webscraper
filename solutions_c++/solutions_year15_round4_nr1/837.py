#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <set>
using namespace std;

void setIO(string name) {
	string in_f = name + ".in";
	string out_f = name + ".out";
	freopen(in_f.c_str(), "r", stdin);
	freopen(out_f.c_str(), "w", stdout);
}

const int N = 1111;

int n, m;
char map[N][N];

bool find(int x, int y) {
	for (int i = 1; i <= n; ++i) {
		if (map[i][y] != '.' && i != x) return true;
	}
	for (int i = 1; i <= m; ++i) {
		if (map[x][i] != '.' && i != y) return true;
	}
	return false;
}

int main() {
	setIO("A");
	int TT;
	scanf("%d", &TT);
	for (int T = 1; T <= TT; ++T) {
		printf("Case #%d: ", T);
		fprintf(stderr, "Now solving %d\n", T);
		scanf("%d %d", &n, &m);
		for (int i = 1; i <= n; ++i) {
			scanf("%s", map[i] + 1);
		}
		int ans = 0;
		bool flag = true;
		for (int i = 1; i <= n; ++i) {
			for (int j = 1; j <= m; ++j) {
				if (map[i][j] == '<') {
					bool f = false;
					for (int k = 1; k < j; ++k) {
						if (map[i][k] != '.') {
							f = true;
							break;
						}
					}
					if (!f) {
						++ans;
						if (!find(i, j)) {
							flag = false;
							break;
						}
					}
				}
				else if (map[i][j] == '>') {
					bool f = false;
					for (int k = j + 1; k <= m; ++k) {
						if (map[i][k] != '.') {
							f = true;
							break;
						}
					}
					if (!f) {
						++ans;
						if (!find(i, j)) {
							flag = false;
							break;
						}
					}
				}
				else if (map[i][j] == '^') {
					bool f = false;
					for (int k = 1; k < i; ++k) {
						if (map[k][j] != '.') {
							f = true;
							break;
						}
					}
					if (!f) {
						++ans;
						if (!find(i, j)) {
							flag = false;
							break;
						}
					}
				}
				else if (map[i][j] == 'v') {
					bool f = false;
					for (int k = i + 1; k <= n; ++k) {
						if (map[k][j] != '.') {
							f = true;
							break;
						}
					}
					if (!f) {
						++ans;
						if (!find(i, j)) {
							flag = false;
							break;
						}
					}
				}
			}
		}
		if (!flag) puts("IMPOSSIBLE");
		else printf("%d\n", ans);
	}
	return 0;
}
