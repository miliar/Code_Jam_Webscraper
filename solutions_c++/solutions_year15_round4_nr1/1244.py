#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <queue>

using namespace std;

const int N(105);

const int dir[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

int n, m;
string s[N];

bool inside(int x, int y) {
	return x >= 0 && x < n && y >= 0 && y < m;
}

int direct(char c) {
	if (c == '>') return 0;
	if (c == 'v') return 1;
	if (c == '<') return 2;
	if (c == '^') return 3;
	return -1;
}

bool go_outside(int x, int y, int d) {
	for (x += dir[d][0], y += dir[d][1]; inside(x, y) && s[x][y] == '.'; x += dir[d][0], y += dir[d][1]);
	return !inside(x, y);
}

int count(int x, int y) {
	if (s[x][y] == '.') return 0;
	if (!go_outside(x, y, direct(s[x][y]))) return 0;
	bool flag = true;
	for (int i = 0; i != 4; ++i) 
		if (!go_outside(x, y, i)) {
			return 1;
		}
	return -1;
}

int main() {
	freopen("in.txt", "r", stdin);
	int test_case;
	cin >> test_case;
	for (int tc = 1; tc <= test_case; ++tc) {
		cin >> n >> m;
		for (int i = 0; i != n; ++i)
			cin >> s[i];
		bool flag = true;
		int ans = 0;
		for (int i = 0; i != n; ++i) {
			for (int j = 0; j != m; ++j) { 
				int c = count(i, j);
				if (c != -1) {
					ans += c;
				}
				else flag = false;
			}
		}
		cout << "Case #" << tc << ": ";
		if (flag) {
			cout << ans << endl;
		}
		else {
			cout << "IMPOSSIBLE" << endl;
		}
	}
	return 0;
}
