#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <algorithm>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <utility>
#include <iomanip>
#include <iostream>
#include <cmath>
#include <bitset>
#include <time.h>
#include <iterator>

using namespace std;

int a[10];

int main() {
	freopen("C-small-attempt4.IN", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int ans = 0, cnt = 0;
		vector<int> dp(50, 0);
		dp[0] = 1;
		int C, D, V;
		cin >> C >> D >> V;
		for (int i = 0; i < D; i++) {
			cin >> a[i];
		}
		for (int i = 0; i < D; i++) {
			for (int s = V; s >= 0; s--) {
				if (s - a[i] >= 0 && dp[s - a[i]])
					dp[s] = 1;
			}
		}
		for (int i = 1; i <= V; i++)
			cnt += dp[i];
		while (cnt < V) {
			int res = 0;
			for (int v = 1; v <= V; v++) {
				if (!dp[v]) {
					res = v;
					break;
				}
			}
			for (int s = V; s >= 0; s--) {
				if (s - res >= 0 && dp[s - res])
					dp[s] = 1;
			}
			cnt = 0;
			for (int i = 1; i <= V; i++)
				cnt += dp[i];
			ans++;
		}
		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}