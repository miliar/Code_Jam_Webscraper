#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <limits>
#include <algorithm>
#include <ctime>
#include <unordered_map>
#include <unordered_set>
#include <cstring>

using namespace std;

const int MAXN = 205;

int cs = 0, n, ans;

bool dfs(int cnt, vector<bool> &come, vector<bool> &visited, const vector<vector<bool>> &s) {
	bool ans = false;
	if (cnt == (int)visited.size()) return true;
	for (int k = 0; k < visited.size(); ++k) {
		if (come[k]) continue;
		come[k] = true;
		for (size_t i = 0; i < visited.size(); ++i) {
			if (visited[i] || !s[k][i]) continue;
			ans = true;
			visited[i] = true;
			if (!dfs(cnt + 1, come, visited, s)) return false;
			visited[i] = false;
		}
		come[k] = false;
	}
	return ans;
}

bool check(const vector<vector<bool>> &s) {
	vector<bool> visited(s.size(), false);
	vector<bool> come(s.size(), false);
	return dfs(0, come, visited, s);
}

vector<vector<vector<bool>>> yc[10];
vector<vector<bool>> input;

void search(int k, vector<vector<bool>> &s, int n) {
	if (k == n * n) {
		if (check(s)) {
			yc[n].push_back(s);

		}
		return;
	}
	int i = k / n, j = k % n;
	s[i][j] = true;
	search(k + 1, s, n);
	s[i][j] = false;
	search(k + 1, s, n);
}

void disp(vector<vector<bool>> s) {
	for (size_t i = 0; i < s.size(); ++i) {
		for (size_t j = 0; j < s.size(); ++j) {
			cout << s[i][j] ? 1 : 0;
		}
		cout << endl;
	}
	cout << endl;
}

int main() {
	freopen("D-small-attempt1.in", "r", stdin);
	freopen("D-small-attempt1.out", "w", stdout);
	for (int i = 1; i <= 4; ++i) {
		vector<vector<bool>> tmp(i, vector<bool>(i, false));
		search(0, tmp, i);
	}

	int t;
	cin >> t;
	while (t--) {
		cin >> n;
		ans = 10000;
		input = vector<vector<bool>>(n, vector<bool>(n, false));
		for (int i = 0; i < n; ++i) {
			string buf;
			cin >> buf;

			for (int j = 0; j < n; ++j) {
				input[i][j] = buf[j] == '1';
			}
		}
		for (auto v : yc[n]) {
			bool legal = true;
			int ccnt = 0;
			for (int a = 0; a < n; ++a)
				for (int b = 0; b < n; ++b) {
				if (!v[a][b] && input[a][b])legal = false;
				if (v[a][b] && !input[a][b]) ++ccnt;
				}
			if (!legal) continue;
			ans = min(ans, ccnt);
		}
		printf("Case #%d: ", ++cs);
		cout << ans << endl;

	}
	return 0;
}
