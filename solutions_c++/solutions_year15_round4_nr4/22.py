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

const int MAXN = 128;
const int dx[4] = {1, -1, 0, 0};
const int dy[4] = {0, 0, 1, -1};

vector<vector<int> > smallest(vector<vector<int> > b) {
	vector<vector<int> > res = b;
	int n = b.size();
	int m = b[0].size();

	for (int o = 0; o < m; o++) {
		for (int i = 0; i < n; i++) {
			int o = b[i][0];
			for (int j = 0; j < m - 1; j++) b[i][j] = b[i][j + 1];
			b[i][m - 1] = o;
		}
		res = min(res, b);
	}
	return res;
}

/*struct comparator {
	bool operator() (const vector<vector<int> > &a, const vector<vector<int> > &b) const {
		return smallest(a) < smallest(b);
	}
};*/

vector<pair<int, int> > q;
int cnt[MAXN][MAXN], ost[MAXN][MAXN];
vector<vector<int> > a;
//set<vector<vector<int> >, comparator> st;
set<vector<vector<int> > > st;
int n, m;

void rec(int cur) {
	if (cur == (int)q.size()) {
		st.insert(smallest(a));
		return;
	}
	int x = q[cur].first, y = q[cur].second;
	for (int i = 1; i <= 4; i++) {
		a[x][y] = i;
		cnt[x][y] = 0;
		ost[x][y] = 0;

		bool fail = 0;
		for (int k = 0; k < 4; k++) {
			int nx = x + dx[k];
			int ny = (y + dy[k] + m) % m;
			if (nx < 0 || nx >= n) continue;
			cnt[x][y] += a[nx][ny] == i;
			ost[x][y] += a[nx][ny] == 0;
			if (a[nx][ny] && a[nx][ny] != a[x][y] && ost[nx][ny] == a[nx][ny] - cnt[nx][ny]) {
				fail = 1;
			}
			if (a[nx][ny] && a[nx][ny] == a[x][y] && a[nx][ny] == cnt[nx][ny]) {
				fail = 1;
			}
		}
		if (cnt[x][y] > i) continue;
		if (cnt[x][y] + ost[x][y] < i) continue;
		if (fail) continue;
		for (int k = 0; k < 4; k++) {
			int nx = x + dx[k];
			int ny = (y + dy[k] + m) % m;
			if (nx < 0 || nx >= n) continue;
			if (a[nx][ny] == a[x][y]) cnt[nx][ny]++;
			ost[nx][ny]--;
		}
		rec(cur + 1);
		for (int k = 0; k < 4; k++) {
			int nx = x + dx[k];
			int ny = (y + dy[k] + m) % m;
			if (nx < 0 || nx >= n) continue;
			if (a[nx][ny] == a[x][y]) cnt[nx][ny]--;
			ost[nx][ny]++;
		}
	}
	a[x][y] = 0;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++) {
		cout << "Case #" << test << ": ";
		cerr << "Case #" << test << ": ";

		cin >> n >> m;

		vector<vector<char> > vis(n, vector<char>(m));
		q.clear();
		int ii = 0;
		q.push_back(make_pair(0, 0));
		while (ii < (int)q.size()) {
			int x = q[ii].first, y = q[ii].second;
			ii++;
			for (int k = 0; k < 4; k++) {
				int nx = x + dx[k];
				int ny = (y + dy[k] + m) % m;
				if (nx < 0 || nx >= n) continue;
				if (!vis[nx][ny]) {
					vis[nx][ny] = 1;
					q.push_back(make_pair(nx, ny));
				}
			}
		}

		a.assign(n, vector<int>(m, 0));
		st.clear();
		rec(0);

		cout << st.size() << endl;
		cerr << st.size() << endl;
	}

    return 0;
}