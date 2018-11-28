#include <cstdio>
#include <algorithm>
#include <iostream>
#include <stack>
using namespace std;

#define mp(a,b) make_pair(a, b)

int dx[] = {0, 1, 0, -1};
int dy[] = {1, 0, -1, 0};

char buf[105][105];

bool Check(int x, int y, int r, int c, int dir) {
	x += dx[dir];
	y += dy[dir];
	while (x > -1 && y > -1 && x < r && y < c) {
		if (buf[x][y] != '.') {
			return true;
		}
		x += dx[dir];
		y += dy[dir];
	}
	return false;
}

void Solve() {
	int r, c;
	cin >> r >> c;
	for (int i = 0; i < r; ++i) {
		cin >> buf[i];
	}
	int ret = 0;
	bool fail = false;
	for (int i = 0; i < r; ++i) {
		for (int j = 0; j < c; ++j) {
			int dir = -1;
			switch (buf[i][j]) {
				case '^':
					dir = 3;
					break;
				case 'v':
					dir = 1;
					break;
				case '>':
					dir = 0;
					break;
				case '<':
					dir = 2;
					break;
			}
			if (dir != -1) {
				if (Check(i, j, r, c, dir)) {
					continue;
				}
				bool ok = false;
				for (int k = 0; k < 4; ++k) {
					if (Check(i, j, r, c, k)) {
						ok = true;
						break;
					}
				}
				if (ok) {
					++ret;
				} else {
					fail = true;
				}
			}
		}
	}
	if (fail) {
		puts("IMPOSSIBLE");
	} else {
		cout << ret << endl;
	}
}

int main() {
	freopen("a_large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int I = 0; I < T; ++I) {
		printf("Case #%d: ", I + 1);
		Solve();
	}
	return 0;
}