#include <bits/stdc++.h>
typedef long long LL;
using namespace std;
#define ALL(x) (x.begin(), x.end())
#define rep(i,n) for(int i = 0;i < n;i ++)

const int inf = 1e9;

int main() {
//	freopen("out.txt", "w", stdout);
	ios :: sync_with_stdio(false);
	cout << fixed << setprecision(16);
	int T;
	char S[101];
	cin >> T;
	rep(cas, T) {
		cin >> S;
		int n = strlen(S);
		int dp[2][n + 1];
		rep(i, n) {
			if (!i) {
				dp[0][i] = S[i] == '-' ? 0: 1;
				dp[1][i] = S[i] == '+' ? 0: 1;
			} else {
				dp[0][i] = min(dp[0][i - 1] + (S[i] == '+' ? 2: 0), dp[1][i - 1] + 1);
				dp[1][i] = min(dp[1][i - 1] + (S[i] == '-' ? 2: 0), dp[0][i - 1] + 1);
			}
		}
		cout << "Case #" << cas + 1 << ": " << dp[1][n - 1] << endl;
	}
	return 0;
}

