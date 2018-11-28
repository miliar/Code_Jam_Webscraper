#include <iostream>
#include <string>
#include <algorithm>


using namespace std;

const int N = 1050;
int n, m;
int dp[N][N];
int a[N];
pair<int, int> b[N];

int move(int i, int j, int k) {
	if (k == 0 && i <= j) return 0;
	if (k == 1 && i >= j) return 0;
	return i < j ? j - i : i - j;
}

int lp[N], rp[N];

void solve() {
	cin >> n;
	for (int i = 0; i < n; i++) cin >> a[i], b[i] = make_pair(a[i], i);
	sort(b, b + n);
	memset(dp, 0, sizeof(dp));
	memset(lp, 0, sizeof(lp));
	memset(rp, 0, sizeof(rp));
	for (int i = 0; i < n; i++)
	for (int j = 0; j < n; j++) {
		if (i < j && a[i] > a[j]) dp[0][0]++;
		if (i < j && a[i] < a[j]) rp[i]++;
		if (i > j && a[i] < a[j]) lp[i]++;
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j <= i; j++) {
			dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] - rp[b[i].second]);
			dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] - lp[b[i].second]);
		}
	}
	int ans = 0;
	for (int i = 0; i <= n; i++)
		ans = max(ans, dp[n][i]);
	cout << dp[0][0] - ans;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		solve();
		cout << endl;
	}
}