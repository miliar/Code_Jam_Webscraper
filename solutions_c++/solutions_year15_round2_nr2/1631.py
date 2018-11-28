#include <iostream>
#include <sstream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <string.h>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <vector>

using namespace std;


char c[16][16];
int s;
int ans = 10000;
int n, m;
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};


void get(int i, int j) {
	if (j == m) {
		i++;
		j = 0;
	}
	if (i == n) {
		if (s != 0) {
			return;
		}
		int k = 0;
		for (int j1 = 0; j1 < n; j1++) {
			for (int g = 0; g < m; g++) {
				if (c[j1][g] == '.') {
					continue;
				}
				for (int h = 0; h < 4; h++) {
					int j2 = j1 + dx[h];
					int g2 = g + dy[h];
					if (j2 < 0 || g2 < 0 || j2 >= n || g2 >= m) {
						continue;
					}
					if (c[j2][g2] == '#') {
						k++;
					}
				}
			}
		}
		ans = min(ans, k / 2);
		return;
	}
	c[i][j] = '.';
	get(i, j + 1);
	if (s > 0) {
		c[i][j] = '#';
		s--;
		get(i, j + 1);
		s++;
	}
}


int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		ans = 10000;
		cin >> n >> m >> s;
		get(0, 0);
		printf("Case #%d: %d\n", i + 1, ans);
	}
    return 0;
}
   