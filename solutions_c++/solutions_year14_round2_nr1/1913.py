#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;
const int MAX_N = 105;
int dp[MAX_N][MAX_N];
	
int main()
{
	//freopen("A-small-attempt0.in","r", stdin);
	//freopen("A-small-attempt0.out", "w", stdout);

	int t;
	cin >> t;
	for (int cases = 1; cases <= t; cases++) {
        int n;
		cin >> n;
		string a, b;
		cin >> a >> b;
		memset(dp,-1, sizeof(dp));
		dp[0][0] = 0;
		for (int i = 1; i <= a.length(); i++) {
			for (int j = 1; j <= b.length(); j++) {
				if (a[i - 1] == b[j - 1]) {
					if (dp[i - 1][j - 1] >= 0) {
						if (dp[i][j] >= 0) {
							dp[i][j] = min(dp[i][j], dp[i - 1][j - 1]);
						} else {
							dp[i][j] = dp[i - 1][j - 1];
						}
					}
					if (dp[i - 1][j] >= 0) {
						if (dp[i][j] >= 0) {
							dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1);
						} else {
							dp[i][j] = dp[i - 1][j] + 1;
						}

					}
					if (dp[i][j - 1] >= 0) {
						if (dp[i][j] >= 0) {
							dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1);
						} else {
							dp[i][j] = dp[i][j - 1] + 1;
						}
					}
				}
			}
		}
		if (dp[a.length()][b.length()] >= 0) {
			printf("Case #%d: %d\n", cases, dp[a.length()][b.length()]);
		} else {
			printf("Case #%d: Fegla Won\n", cases);
		}
	}

}
			
		
