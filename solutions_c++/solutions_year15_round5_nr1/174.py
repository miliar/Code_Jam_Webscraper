#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <string>
#include <iostream>
#include <cassert>
#include <queue>

#pragma comment(linker, "/STACK:256000000")

using namespace std;

const int MAXN = 1 << 20;
const int INF = 1e9;

int n, d;
int s[MAXN], as, cs, rs;
int m[MAXN], am, cm, rm;
vector<int> e[MAXN];
vector<pair<int, int> > vct;

void dfs(int v, int mn, int mx) {
	mn = max(mn, s[v] - d);
	mx = min(mx, s[v]);
	if (mn <= mx) {
		vct.push_back(make_pair(mn, -1));
		vct.push_back(make_pair(mx, +1));
	}
	for (int i = 0; i < (int)e[v].size(); i++) dfs(e[v][i], mn, mx);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cout.precision(10);
	cout << fixed;
	cerr.precision(10);
	cerr << fixed;

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++) {
		cout << "Case #" << test << ": ";
		cerr << "Case #" << test << ": ";

		cin >> n >> d;
		cin >> s[0] >> as >> cs >> rs;
		cin >> m[0] >> am >> cm >> rm;

		for (int i = 0; i < n; i++) e[i].clear();
		for (int i = 1; i < n; i++) {
			s[i] = (1LL * s[i - 1] * as + cs) % rs;
			m[i] = (1LL * m[i - 1] * am + cm) % rm;
			e[m[i] % i].push_back(i);
		}
		vct.clear();
		dfs(0, -INF, INF);
		sort(vct.begin(), vct.end());

		int mx = 0;
		int cur = 0;
		for (int i = 0; i < (int)vct.size(); i++) {
			cur -= vct[i].second;
			mx = max(mx, cur);
		}

		cout << mx << endl;
		cerr << mx << endl;
	}

    return 0;
}