#include <bits/stdc++.h>
using namespace std;

int p[1005];
int n;
int memo[15][15];
int get_ans(int i, int maxi) {
	if (i == n) return maxi;
	int &ret = memo[i][maxi];
	if (ret == -1) {
		ret = 1 << 30;
		for (int y = 1; y <= p[i]; ++y) {
			ret = min(ret, get_ans(i + 1, max(maxi, y)) + (p[i] + y - 1) / y - 1);
		}
	}
	return ret;
}

int main() {
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, K = 1;
	cin >> T;
	while (T--) {
		memset(memo, -1, sizeof memo);
		cin >> n;
		for (int i = 0; i < n; ++i) {
			cin >> p[i];
		}

		int ans = get_ans(0, 0);

		cout << "Case #" << K++ << ": " << ans << endl;
	}
	return 0;
}
