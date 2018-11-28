//#include "testlib.h"
//#include <spoj.h>

#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>
#include <math.h>
#include <assert.h>
#include <time.h>
#include <memory.h>
#include <set>
#include <numeric>
#include <map>
#include <queue>
#include <stack>
#include <bitset>
#include <unordered_map>

using namespace std;

int dp[111][2];

int main() {
    ios::sync_with_stdio(0);
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    
    int t;
    cin >> t;
    for(int T = 1; T <= t; ++T) {
        string s;
        cin >> s;
        dp[0][1] = s[0]=='-';
        dp[0][0] = s[0]=='+';
        for(int i = 1; i < s.size(); ++i) {
            if (s[i] == '-') {
                dp[i][0] = min(dp[i-1][0], dp[i-1][1]+1);
                dp[i][1] = min(dp[i-1][0]+1, dp[i-1][1]+2);
            }
            else {
                dp[i][0] = min(dp[i-1][1]+1, dp[i-1][0]+2);
                dp[i][1] = min(dp[i-1][1], dp[i-1][0]+1);
            }
        }
        cout << "Case #" << T << ": ";
        cout << dp[s.size()-1][1] << "\n";
    }
    return 0;
}