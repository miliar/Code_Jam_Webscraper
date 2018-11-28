#define _CRT_SECURE_NO_WARNINGS
#include <functional>
#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <sstream>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <ctime>
#include <set>
#include <map>

#define ll long long
#define ld long double
#define sqr(x) ((x) * (x))
#define mp make_pair
#define TASKNAME ""

const int inf = (int)1e9;
const int mod = (int)1e9 + 7;
const ll infll = (ll)1e18;
const ld eps = 1e-9;

using namespace std;


void solve() {
	vector<vector<int> > g;
	int r, c;
	scanf("%d %d", &r, &c);
	vector<vector<char> > table(r, vector<char>(c));
	for (int i = 0; i < r; i++) {
		scanf("\n");
		for (int j = 0; j < c; j++) {
			scanf("%c", &table[i][j]);
		}
	}
	vector<int> v(c, -1);
	vector<char> dirs;
	bool rem1 = false;
	int n = 0;
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			if (table[i][j] == '.')
				continue;
			g.push_back(vector<int>(4, -1));
			dirs.push_back(table[i][j]);
			if (rem1) {
				g[n][0] = n - 1;
				if (n > 0)
					g[n - 1][1] = n;
			}
			g[n][2] = v[j];
			if (v[j] >= 0)
				g[v[j]][3] = n;
			v[j] = n;
			rem1 = true;
			n++;
		}
		rem1 = false;
	}
	bool ok = true;
	map<char, int> dir;
	dir['<'] = 0;
	dir['>'] = 1;
	dir['^'] = 2;
	dir['v'] = 3;
	int ans = 0;
	for (int i = 0; i < n && ok; i++) {
		if (g[i][0] == -1 && g[i][1] == -1 && g[i][2] == -1 && g[i][3] == -1) {
			ok = false;
			printf("IMPOSSIBLE");
			return;
		}
		if (g[i][dir[dirs[i]]] == -1)
			ans++;
	}
	printf("%d", ans);
}

int main() {
#ifdef __DEBUG__
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	clock_t start = clock();
#endif
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		solve();
		printf("\n");
	}

#ifdef __DEBUG__
	fprintf(stderr, "\nTime: %Lf\n", ((clock() - start) / (ld)CLOCKS_PER_SEC));
#endif
	return 0;
}