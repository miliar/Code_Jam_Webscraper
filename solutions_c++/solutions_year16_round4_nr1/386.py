#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
using namespace std;

const string str = "RSP";
string dp[14][3];

int main() {
	int T;
	cin >> T;

	for (int i = 0; i < 3; ++i) {
		dp[0][i] = string(1, str[i]);
	}

	for (int dep = 1; dep <= 12; ++dep) {
		for (int me = 0; me < 3; ++me) {
			string a = dp[dep - 1][me];
			string b = dp[dep - 1][(me + 1) % 3];
			dp[dep][me] = min(a + b, b + a);
		}
	}

	for (int nc = 1; nc <= T; ++nc) {
		int N, R, P, S;
		cin >> N >> R >> P >> S;
		int cnt[3] = { R, S, P };
		string ans = "";
		for (int me = 0; me < 3; ++me) {
			bool ok = true;
			for (int j = 0; j < 3; ++j) {
				if (count(dp[N][me].begin(), dp[N][me].end(), str[j])
						!= cnt[j]) {
					ok = false;
					break;
				}
			}
			if (ok) {
				if (ans == string(""))
					ans = dp[N][me];
				else
					ans = min(ans, dp[N][me]);
			}
		}
		if (ans == string(""))
			ans = "IMPOSSIBLE";

		cout << "Case #" << nc << ": " << ans << endl;
	}
	return 0;
}
