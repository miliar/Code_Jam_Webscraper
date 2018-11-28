#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <cstdlib>
#include <cstdio>
using namespace std;

typedef unsigned long long ULL;

char m[101][101];
int R, C;

void input()
{
	cin >> R >> C;
	for (int i=0;i<R;++i) {
		cin >> m[i];
	}
}

int dx[] = {0, 1, 0, -1}, dy[] = {1, 0, -1, 0};

bool bad(int x, int y)
{
	for (int i=0;i<4;++i) {
		int tx = x + dx[i], ty = y + dy[i];
		while (tx >=0 && tx < R && ty >=0 && ty < C) {
			if (m[tx][ty] != '.') return false;
			tx += dx[i], ty += dy[i];
		}
	}
	return true;
}

int solve()
{
	int count = 0;
	for (int i=0;i<R;++i) {
		for (int j=0;j<C;++j) {
			if (m[i][j] != '.') {
				if (m[i][j] == '<') {
					if (bad(i,j)) return -1;
					count ++;
				}
				break;
			}
		}
		for (int j=C-1;j>=0;--j) {
			if (m[i][j] != '.') {
				if (m[i][j] == '>') {
					if (bad(i,j)) return -1;
					count ++;
				}
				break;
			}
		}
	}
	for (int j=0;j<C;++j) {
		for (int i=0;i<R;++i) {
			if (m[i][j] != '.') {
				if (m[i][j] == '^') {
					if (bad(i,j)) return -1;
					count ++;
				}
				break;
			}
		}
		for (int i=R-1;i>=0;--i) {
			if (m[i][j] != '.') {
				if (m[i][j] == 'v') {
					if (bad(i,j)) return -1;
					count ++;
				}
				break;
			}
		}
	}

	return count;
}

int main()
{
	int T, nCase = 1;
	cin >> T;
	while (T--) {
		input();
		cout << "Case #" << nCase ++ << ": ";
		int ans = solve();
		if (ans < 0) cout << "IMPOSSIBLE";
		else cout << ans;
		cout << endl;
	}

	return 0;
}

