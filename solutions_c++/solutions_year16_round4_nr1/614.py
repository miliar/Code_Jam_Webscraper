#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <climits>
#include <algorithm>
#include <map>
using namespace std;
string dp[15][3];
int win[3] = {1, 2, 0};
bool check(string str, int p, int r, int s) {
	int len = str.size();
	for(int i = 0; i < len; i++) {
		if(str[i] == 'P') {
			p--;
		} else if(str[i] == 'R') {
			r--;
		} else {
			s--;
		}
		if(p < 0 || r < 0 || s <0) {
			return false;
		}
	}
	return true;

}
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int cas = 0;
	int T = 0;
	scanf("%d", &T);
	while(T--) {
		int N, P, R, S;
		printf("Case #%d: ", ++cas);
		scanf("%d%d%d%d", &N, &R, &P, &S);
		if(P > 0) {
			dp[0][0] = "P";
		}
		if(R > 0) {
			dp[0][1] = "R";
		}
		if(S > 0) {
			dp[0][2] = "S";
		}
		for(int i = 1; i <= N; i++) {
			for(int j = 0; j < 3; j++) {
				dp[i][j] = "";
				string tmp1 = dp[i - 1][j] + dp[i - 1][win[j]];
				string tmp2 = dp[i - 1][win[j]] + dp[i - 1][j];
				if(dp[i - 1][j] != "" && dp[i - 1][win[j]] != "" && check(tmp1, P, R, S)) {
					if(dp[i][j] == "" || dp[i][j] > tmp1) {
						dp[i][j] = tmp1;
					}
				}
				if(dp[i - 1][win[j]] != "" && dp[i - 1][j] != "" && check(tmp2, P, R, S)) {
					if(dp[i][j] == "" || dp[i][j] > tmp2) {
						dp[i][j] = tmp2;
					}
				}
				//cout<<i<<" "<<j<<" "<<dp[i][j]<<" "<<dp[i - 1][j]<<" "<<dp[i - 1][win[j]]<<" "<<tmp1<<endl;
			}
		}
		string ans = "";
		for(int i = 0; i < 3; i++) {
			if(dp[N][i] != "") {
				if(ans == "" || ans > dp[N - 1][i]) {
					ans = dp[N][i];
				}
			}
		}
		if(ans == "") {
			ans = "IMPOSSIBLE";
		}
		printf("%s\n", ans.c_str());

	}
}
