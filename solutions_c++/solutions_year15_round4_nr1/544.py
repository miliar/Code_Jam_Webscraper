#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
#include <memory.h>
#include <vector>
#include <sstream>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <complex>

using namespace std;

#define REP(a,b) for (int a=0; a<(int)(b); ++a)
#define FOR(a,b,c) for (int a=(b); a<(int)(c); ++a)


const int MAXN = 110;

int r, c;
char g[MAXN][MAXN];
int d[MAXN][MAXN];

void read_input() {
	cin >> r >> c;
	REP(i, r) cin >> g[i];
}


void solve() {
	memset(d, 0, sizeof(d));

	REP(i, r) {
		int j = 0;
		while (j < c && g[i][j] == '.') ++j;
		if (j < c) d[i][j] |= 1;
		j = c - 1;
		while (j >= 0 && g[i][j] == '.') --j;
		if (j >= 0) d[i][j] |= 2;
	}

	REP(j, c) {
		int i = 0;
		while (i < r && g[i][j] == '.') ++i;
		if (i < r) d[i][j] |= 4;
		i = r - 1;
		while (i >= 0 && g[i][j] == '.') --i;
		if (i >= 0) d[i][j] |= 8;
	}

	int res = 0;
	REP(i, r) REP(j, c) if (g[i][j] != '.') {
		if (d[i][j] == 15) {
			cout << "IMPOSSIBLE" << endl;
			return;
		}

		if (g[i][j] == 'v' && (d[i][j] & 8)) ++res;
		if (g[i][j] == '^' && (d[i][j] & 4)) ++res;
		if (g[i][j] == '<' && (d[i][j] & 1)) ++res;
		if (g[i][j] == '>' && (d[i][j] & 2)) ++res;
	}

	cout << res << endl;
}


int main(int argc, char* argv[]) {
	int nt, single_tc = 0;

	if (argc > 1) {
		sscanf(argv[1], "%d", &single_tc);
	}

	scanf("%d", &nt);
	for (int t = 1; t <= nt; ++t) {
		read_input();
		if (single_tc == 0 || single_tc == t) {
			printf("Case #%d: ", t);
			solve();
		}
	}

	return 0;
}