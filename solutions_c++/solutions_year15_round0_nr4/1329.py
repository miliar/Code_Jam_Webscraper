#include <iostream>
#include <ctime>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define REP(i, n) for(int i(0); (i)<(int)(n); i++)
#define FOR(i, a, b) for (int i(a); i <= int(b); i++)

int T, n, m, k, Q[5][5][5];

void solve() {
	cin >> k >> n >> m;
	static int z = 0;
	printf("Case #%d: %s\n", ++z, Q[n][m][k] == 1 ? "GABRIEL" : "RICHARD");
}

int main() {
	int c = 0;
	FOR(i, 1, 4) FOR(j, 1, 4) FOR(k, 1, 4) {
		if (i * j % k != 0) {
			Q[i][j][k] = 2; continue;
		}
		if (k >= min(i, j) * 2 + 1) {
			Q[i][j][k] = 2; continue;
		}
		if (k > max(i, j)) {
			Q[i][j][k] = 2; continue;
		}
		if (i > j) {
			Q[i][j][k] = Q[j][i][k];
			continue;
		}
		if (k <= 3) {
			Q[i][j][k] = 1; continue;
		}
		if (i == 2) {
			Q[i][j][k] = 2; continue;
		}
		if (k <= 4) {
			Q[i][j][k] = 1; continue;
		}
		cout << ++c << ' ' << i << ' ' << j << ' ' << k << endl;
	}


	cin >> T;
	while (T--) solve();
	return 0;
}

