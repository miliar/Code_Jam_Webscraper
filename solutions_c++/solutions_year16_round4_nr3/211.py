#include <iostream> 
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <stack>
#include <functional>
#include <cstring>
#include <algorithm>
#include <map>
#include <cmath>
#include <ctime>
#include <unordered_map>

using namespace std;

using ld = long double;

const int N = 16;
char maze[N][N];

int R, C;

// U D R L
int dx[] = { 0, 0, 1, -1 };
int dy[] = { -1, 1, 0, 0 };

int check(int r, int c, int d) {
	if (r < 0) return c;
	if (c >= C) return C + r;
	if (r >= R) return C + R + (C - c - 1);
	if (c < 0) return (C + R) * 2 - r - 1;

	if (maze[r][c] == '/') d = (d + 2) % 4;
	else {
		if (d == 1 || d == 2) d = 3 - d;
		else d = 3 - d;
	}
	r += dy[d];
	c += dx[d];
	return check(r, c, d);
}

string solve() {
	cin >> R >> C;
	vector<int> a((R + C) * 2);
	for (auto &x : a) {
		cin >> x;
		--x;
	}

	for (int i = 0; i < (1 << R*C); ++i) {
		for (int j = 0; j < R*C; ++j) {
			maze[j / C][j % C] = (i >> j & 1) ? '/' : '\\';
		}
		vector<int> match((R + C) * 2);
		for (int i = 0; i < C; ++i) {
			int x = check(0, i, 1);
			match[i] = x;
			match[x] = i;
		}
		for (int i = 0; i < R; ++i) {
			int x = check(i, C - 1, 3);
			match[C + i] = x;
			match[x] = C + i;
		}
		for (int i = 0; i < C; ++i) {
			int num = C + R + (C - i - 1);
			int x = check(R - 1, i, 0);
			match[num] = x;
			match[x] = num;
		}
		for (int i = 0; i < R; ++i) {
			int num = (C + R) * 2 - i - 1;
			int x = check(i, 0, 2);
			match[num] = x;
			match[x] = num;
		}

		bool b = true;
		for (int i = 0; i < R + C; ++i) {
			b &= match[a[i * 2]] == a[i * 2 + 1];
		}
		if (b) {
			for (int i = 0; i < R; ++i) {
				string s;
				for (int j = 0; j < C; ++j) {
					s += maze[i][j];
				}
				cout << s << endl;
			}
			return "";
		}
	}
	cout << "IMPOSSIBLE" << endl;
	return "";
}


int main(){
	cin.tie(0);
	ios::sync_with_stdio(false);

	cout.setf(ios::fixed);
	cout.precision(9);

	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: \n", i);
		solve();
	}

}