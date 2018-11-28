#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <numeric>
#include <bitset>
#include <complex>
#define rep(x, to) for (int x = 0; x < (to); x++)
#define REP(x, a, to) for (int x = (a); x < (to); x++)
#define foreach(itr, x) for (typeof((x).begin()) itr = (x).begin(); itr != (x).end(); itr++)
#define EPS (1e-14)

using namespace std;

typedef long long ll;
typedef pair<int, int> PII;
typedef pair<long, long> PLL;

int T;
int R, C;
string f[105];

bool is_impossible() {
	int rows[105][105] = {0};
	int cols[105][105] = {0};
	rep(i, R) rep(j, C) {
		rows[i+1][j+1] = rows[i+1][j];
		cols[i+1][j+1] = cols[i][j+1];
		rows[i+1][j+1] += (f[i][j] != '.');
		cols[i+1][j+1] += (f[i][j] != '.');
	}
	rep(i, R) rep(j, C) {
		if (f[i][j] != '.') {
			if (rows[i+1][j] == 0 &&
					rows[i+1][C] - rows[i+1][j+1] == 0 &&
					cols[i][j+1] == 0 &&
					cols[R][j+1] - cols[i+1][j+1] == 0) {
				return true;
			}
		}
	}
	return false;
}

void solve(int t) {
	int ans = 0;
	if (is_impossible()) {
		printf("Case #%d: IMPOSSIBLE\n", t);
		return;
	}
	//left
	for (int i = 0; i < R; i++) {
		int initial = 1;
		for (int j = 0; j < C; j++) {
			if (initial > 0 && f[i][j] != '.') {
				ans += f[i][j] == '<';
				initial--;
			}
		}
	}
	//right
	for (int i = 0; i < R; i++) {
		int initial = 1;
		for (int j = C-1; j >= 0; j--) {
			if (initial > 0 && f[i][j] != '.') {
				ans += f[i][j] == '>';
				initial--;
			}
		}
	}
	//top
	for (int i = 0; i < C; i++) {
		int initial = 1;
		for (int j = 0; j < R; j++) {
			if (initial > 0 && f[j][i] != '.') {
				ans += f[j][i] == '^';
				initial--;
			}
		}
	}
	//bottom
	for (int i = 0; i < C; i++) {
		int initial = 1;
		for (int j = R-1; j >= 0; j--) {
			if (initial > 0 && f[j][i] != '.') {
				ans += f[j][i] == 'v';
				initial--;
			}
		}
	}
	printf("Case #%d: %d\n", t, ans);
}

int main() {
	cin >> T;
	rep(i, T) {
		cin >> R >> C;
		rep(j, R) {
			cin >> f[j];
			//cout << f[j] << endl;
		}
		solve(i+1);
	}
	return 0;
}


