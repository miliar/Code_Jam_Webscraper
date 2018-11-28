#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    int caseNum = t;
    while (t--) {
        string str;
        cin >> str;
        int n = int(str.size());
        vector<vector<int> > dp(n, vector<int>(2));
        if (str[0] == '-') {
            dp[0][0] = 1;
            dp[0][1] = 0;
        }
        if (str[0] == '+') {
            dp[0][0] = 0;
            dp[0][1] = 1;
        }
        for (int i = 1; i < n; i++) {
            if (str[i] == '+') {
                dp[i][0] = min(dp[i - 1][0], dp[i - 1][1] + 1);
                dp[i][1] = min(dp[i - 1][0] + 1, dp[i - 1][1] + 2);
            } else {
                dp[i][0] = min(dp[i - 1][0] + 2, dp[i - 1][1] + 1);
                dp[i][1] = min(dp[i - 1][0] + 1, dp[i - 1][1]);
            }
        }
        cout << "Case #" << caseNum - t << ": " << dp[n - 1][0] << endl;
    }
    return 0;
}