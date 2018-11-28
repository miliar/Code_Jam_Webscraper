#include <bits/stdc++.h>
using namespace std;
void init_ios() {ios_base::sync_with_stdio(false); cin.tie(nullptr);}

int N;

void solve() {
	scanf("%d", &N);

	vector<vector<int>> v(2 * N - 1);
	for (size_t i = 0; i < v.size(); ++i) {
		for (int j = 0; j < N; ++j) {
			int a;
			scanf("%d", &a);
			v[i].push_back(a);
		}
	}

	vector<int> pos(v.size(), -1);
	int x = -1, rc = -1;

	for (int i = 0; i < N; ++i) {
		int mn = 1 << 30;
		for (size_t j = 0; j < v.size(); ++j) {
			if (pos[j] != -1) continue;
			mn = min(mn, v[j][i]);
		}

		vector<int> ids;
		for (size_t j = 0; j < v.size(); ++j) {
			if (pos[j] != -1) continue;
			if (v[j][i] == mn) {
				pos[j] = i;
				ids.push_back(j);
			}
		}

		if (ids.size() == 1) {
			x = ids.front();
			rc = i;
		}
	}

	// printf("%d %d\n", x, rc);

	vector<int> res;
	for (int i = 0; i < N; ++i) {
		for (size_t j = 0; j < v.size(); ++j) {
			if (pos[j] != i) continue;

			if (v[x][i] != v[j][rc]) res.push_back(v[j][rc]);
		}

		if ((int)res.size() == i) res.push_back(v[x][i]);
	}

	for (size_t i = 0; i < res.size(); ++i) {
		if (i) putchar(' ');
		printf("%d", res[i]);
	}
	puts("");
}

int main() {
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
