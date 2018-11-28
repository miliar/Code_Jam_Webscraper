#include <iostream>
#include <iomanip>
#include <vector>
#include <set>
#include <queue>
#include <algorithm>

using namespace std;

#define TOTAL 100000

int n, p, q;
int h[100], g[100];
int dp[TOTAL], dp2[TOTAL];

void solve() {
	cin >> p >> q >> n;
	fill_n(dp, TOTAL, -1);
	dp[1] = 0;
	for (int i=0; i<n; i++) {
		cin >> h[i] >> g[i];
		int tshots = (h[i] + q - 1) / q;
		int hrem = (h[i] - q * (tshots - 1));
		int pshots = (hrem + p - 1) / p;
		fill_n(dp2, TOTAL, -1);
		for (int f=0; f<TOTAL; f++) {
			if (dp[f] < 0) continue;
			// Kill it
			if (f + tshots - 1 - pshots >= 0) {
				int freeshots = min(TOTAL-1, f + tshots - 1 - pshots);
				dp2[freeshots] = max(dp2[freeshots], dp[f] + g[i]);
			}
			// Don't kill it
			int freeshots = min(TOTAL-1, f + tshots);
			dp2[freeshots] = max(dp2[freeshots], dp[f]);
		}
		swap(dp, dp2);
	}
	int gold = 0;
	for (int i=0; i<TOTAL; i++) {
		gold = max(gold, dp[i]);
	}
	cout << gold;
}

int main() {
	int t;
	cin >> t;
	for (int casenum=1; casenum<=t; casenum++) {
		cout << "Case #" << casenum << ": ";
		solve();
		cout << "\n";
	}
}
