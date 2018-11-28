#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
using namespace std;
const int MAX_N = 100 + 10;
int n, m;
char map[MAX_N][MAX_N];
const int di[] = { -1, 1, 0, 0 }, dj[] = { 0, 0, -1, 1 };
const string DIR = "^v<>";

bool inrange(int r, int c) {
	return r >= 0 && r < n && c >= 0 && c < m;
}

bool check(int r, int c, int d) {
	r += di[d], c += dj[d];
	while (inrange(r, c)) {
		if (map[r][c] != '.')
			return true;
		r += di[d], c += dj[d];
	}
	return false;
}

int main() {
	int T;
	cin >> T;
	for (int nc = 1; nc <= T; ++nc) {
		scanf("%d%d", &n, &m);
		for (int r = 0; r < n; ++r) {
			scanf("%s", map[r]);
		}

		int ans = 0;
		bool chk = true;

		for (int r = 0; r < n; ++r) {
			for (int c = 0; c < m; ++c) {
				if (map[r][c] == '.')
					continue;
				if (!check(r, c, DIR.find(map[r][c]))) {
					++ans;
					bool ok = false;
					for (int d = 0; d < 4; ++d) {
						if (check(r, c, d)) {
							ok = true;
						}
					}
					if (!ok) {
						chk = false;
						break;
					}
				}
			}
		}

		if (!chk) {
			printf("Case #%d: IMPOSSIBLE\n", nc);
		} else {
			printf("Case #%d: %d\n", nc, ans);
		}
	}
}
