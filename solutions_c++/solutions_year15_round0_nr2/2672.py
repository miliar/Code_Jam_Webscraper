#include <assert.h>
#include <cstring>
#include <iostream>
#include <fstream>
#include <climits>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <list>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>

using namespace std;

int dp[1100][1100];

int main() {
    memset(dp, 0, sizeof(dp));
    for (int i = 1; i <= 1000; i++) {
        for (int j = i+1; j <= 1000; j++) {
            dp[j][i] = 1000;
            for (int k = 1; k <= j-i; k++) {
                dp[j][i] = min(dp[k][i] + dp[j-k][i] + 1, dp[j][i]);
            }
        }
    }
    // cout << dp[100][25] << endl;

    int cases;
    cin >> cases;
    for (int t = 1; t <= cases; t++) {
        int n;
        cin >> n;
        vector<int> v(n);
        int maxi = 0;
        for (int i = 0; i < n; i++) {
            cin >> v[i];
            maxi = max(maxi, v[i]);
        }
        int optimal = maxi;
        for (int i = maxi; i > 0; i--) {
            int spm = 0;
            for (int j = 0; j < n; j++) {
                spm += dp[v[j]][i];
            }
            optimal = min(spm + i, optimal);
        }
        printf("Case #%d: %d\n", t, optimal);
    }
    return 0;
}