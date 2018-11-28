#include <bits/stdc++.h>

using namespace std;

int dp1[105];
int dp2[105];

int main(void) {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		memset(dp1, 0, sizeof dp1);
		memset(dp2, 0, sizeof dp2);
		string s;
		cin >> s;
		int n = (int) s.size();
		if (s[0] == '-') {
			dp1[0] = 1;
		}
		else {
			dp2[0] = 1;
		}
		for (int i = 1; i < n; ++i) {
			if (s[i] == '-') {
				dp1[i] = dp2[i - 1] + 1;
				dp2[i] = dp2[i - 1];
			}
			else {
				dp1[i] = dp1[i - 1];
				dp2[i] = dp1[i - 1] + 1;
			}
		}
		printf("Case #%d: %d\n", i, dp1[n - 1]);
	}
}