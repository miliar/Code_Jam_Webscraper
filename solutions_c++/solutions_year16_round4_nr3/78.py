#include <functional>
#include <sstream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <string>
#include <cassert>
#include <ctime>
#include <map>
#include <math.h>
#include <cstdio>
#include <set>
#include <deque>
#include <memory.h>
#include <queue>


using namespace std;

#pragma comment(linker, "/STACK:64000000")

typedef long long ll;

const int MAXK = 0;
const int MAXN = 1 << MAXK;
const int INF = (int)1e9;


int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++) {
		cout << "Case #" << test << ": " << endl;
		cerr << "Case #" << test << ": " << endl;
		
		int n, m;
		cin >> n >> m;
		vector<pair<int, int> > vct;
		vector<int> p(2 * (n + m));
		for (int i = 0; i < n + m; i++) {
			int u, v;
			cin >> u >> v;
			u--; v--;
			p[u] = v;
			p[v] = u;
		}
		for (int j = 1; j <= m; j++) {
			vct.push_back(make_pair(0, j));
		}
		for (int i = 1; i <= n; i++) {
			vct.push_back(make_pair(i, m + 1));
		}
		for (int j = m; j >= 1; j--) {
			vct.push_back(make_pair(n + 1, j));
		}
		for (int i = n; i >= 1; i--) {
			vct.push_back(make_pair(i, 0));
		}

		function<int(int, int)> ok = [&](int i, int j) {
			return 1 <= i && i <= n && 1 <= j && j <= m;
		};

		bool found = 0;
		for (int mask = 0; mask < 1 << (n * m); mask++) {
			vector<vector<int> > type(n + 2, vector<int>(m + 2));
			for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) type[i + 1][j + 1] = (mask >> (i * m + j)) & 1;
			vector<vector<vector<char> > > was(n + 2, vector<vector<char> >(m + 2, vector<char>(2, 0)));
			bool cok = 1;
			for (int i = 0; i < (int)p.size(); i++) {
				queue<pair<pair<int, int>, int> > q;
				q.push(make_pair(vct[i], 0));
				q.push(make_pair(vct[i], 1));
				if (was[vct[i].first][vct[i].second][0] || was[vct[i].first][vct[i].second][1]) continue;
				was[vct[i].first][vct[i].second][0] = 1;
				was[vct[i].first][vct[i].second][1] = 1;
				set<pair<int, int> > st;
				while (!q.empty()) {
					int i = q.front().first.first;
					int j = q.front().first.second;
					int up = q.front().second;
					q.pop();
					if (!ok(i, j)) {
						st.insert(make_pair(i, j));
					}

					function<void(int, int, int)> go = [&](int ni, int nj, int nup) {
						if (ok(i, j) + ok(ni, nj) >= 1 && !was[ni][nj][nup]) {
							was[ni][nj][nup] = 1;
							q.push(make_pair(make_pair(ni, nj), nup));
						}
					};

					if (up == 0 && type[i][j] == 0) {
						go(i - 1, j, 1);
						if (j - 1 >= 0) go(i, j - 1, type[i][j - 1] ^ 1);
					}
					if (up == 0 && type[i][j] == 1) {
						go(i - 1, j, 1);
						if (j + 1 <= m + 1) go(i, j + 1, type[i][j + 1]);
					}
					if (up == 1 && type[i][j] == 0) {
						go(i + 1, j, 0);
						if (j + 1 <= m + 1) go(i, j + 1, type[i][j + 1]);
					}
					if (up == 1 && type[i][j] == 1) {
						go(i + 1, j, 0);
						if (j - 1 >= 0) go(i, j - 1, type[i][j - 1] ^ 1);
					}
				}
				pair<int, int> xr = vct[i];
				for (auto o : st) {
					xr.first ^= o.first;
					xr.second ^= o.second;
				}
				if (!(st.size() == 2 && xr == vct[p[i]])) {
					cok = 0;
					break;
				}
			}
			if (cok) {
				found = 1;
				for (int i = 1; i <= n; i++) {
					for (int j = 1; j <= m; j++) {
						char c = type[i][j] ? '\\' : '/';
						cout << c;
						cerr << c;
					}
					cout << endl;
					cerr << endl;
				}
				break;
			}
		}
		if (!found) {
			cout << "IMPOSSIBLE" << endl;
			cerr << "IMPOSSIBLE" << endl;
		}
	}

	return 0;
}