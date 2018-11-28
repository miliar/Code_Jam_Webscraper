#include <bits/stdc++.h>
using namespace std;

int N;
vector<string> Ns[2];
pair<int, long long> dp[1 << 16];

void solve() {
	scanf("%d", &N);
	for (int i = 0; i < N; ++i) {
		string a, b;
		cin >> a >> b;
		Ns[0].push_back(a);
		Ns[1].push_back(b);
	}

	vector<string> Ss[2];

	for (int i = 0; i < N; ++i) {
		Ss[0].push_back(Ns[0][i]);
		Ss[1].push_back(Ns[1][i]);
	}

	for (int i = 0; i < 2; ++i) {
		sort(Ss[i].begin(), Ss[i].end());
		Ss[i].erase(unique(Ss[i].begin(), Ss[i].end()), Ss[i].end());
	}

	vector<int> hoge[2];

	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < 2; ++j) {
			for (int idx = 0; idx < Ss[j].size(); ++idx) {
				if (Ss[j][idx] == Ns[j][i]) {
					hoge[j].push_back(idx);
					break;
				}
			}
		}
	}

	fill(dp, dp + (1 << N), make_pair(0, 0LL));

	for (int i = 0; i < 1 << N; ++i) {
		for (int j = 0; j < N; ++j) {
			if (i & (1 << j)) continue;
			int x1 = 1 << hoge[0][j] + N;
			int x2 = 1 << hoge[1][j];
			int st = dp[i].first;
			long long bit = dp[i].second;
			if (x1 & bit && x2 & bit) ++st;
			bit |= x1 | x2;
			dp[i | (1 << j)] = max(dp[i | (1 << j)], make_pair(st, bit));
		}
	}

	int res = 0;
	for (int i = 0; i < 1 << N; ++i) res = max(res, dp[i].first);

	printf("%d\n", res);

	Ns[0].clear(), Ns[1].clear();
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
