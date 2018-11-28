#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
using namespace std;
int main() {
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int caseCount = 0;
	scanf("%d", &caseCount);
	for (int i = 0; i < caseCount; i++) {
		char line[1000];
		scanf("%s", line);
		int len = strlen(line);
		vector<vector<int>>dp(len, vector<int>(2, 0));
		if (len > 0) {
			dp[0][0] = line[0] == '+';
			dp[0][1] = line[0] == '-';
			for (int j = 1; j < len; j++) {
				if (line[j] == '-') {
					dp[j][1] = min(dp[j - 1][0] + 1, dp[j - 1][1] + 2);
					dp[j][0] = min(dp[j - 1][0], dp[j - 1][1] + 1);
				}
				else {
					dp[j][1] = min(dp[j - 1][1], dp[j - 1][0] + 1);
					dp[j][0] = min(dp[j - 1][0] + 2, dp[j - 1][1] + 1);
				}
			}
			cout << "Case #" << i + 1 << ": " << min(dp[len - 1][1], dp[len - 1][0] + 1) << endl;
		}
		else {
			cout << "Case #" << i + 1 << ": 0" << endl;
		}
	}
	return 0;
}