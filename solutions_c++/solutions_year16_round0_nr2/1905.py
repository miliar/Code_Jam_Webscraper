#include <iostream>
#include <vector>
#include <cstdlib>
#include <string>
#include <fstream>
#define mp(a, b) make_pair(a, b)
using namespace std;

typedef long long int int64;
const int INF = 1000000007;

int solve(string s) {
    s = " " + s;
    vector < pair<int, int> > dp(s.length(), mp(INF, INF));
    dp[0].first = dp[0].second = 0;
    for (int i = 1; i < (int)s.length(); ++i) {
        if (s[i] == '+') {
            dp[i].first = min(dp[i - 1].first, dp[i].first);
            dp[i].first = min(dp[i - 1].second + 1, dp[i].first);
            dp[i].second = min(dp[i - 1].first + 1, dp[i].second);
            dp[i].second = min(dp[i - 1].second + 2, dp[i].second);
        } else {
            dp[i].second = min(dp[i - 1].second, dp[i].second);
            dp[i].second = min(dp[i - 1].first + 1, dp[i].second);
            dp[i].first = min(dp[i - 1].second + 1, dp[i].first);
            dp[i].first = min(dp[i - 1].first + 2, dp[i].first);
        }
    }

    return dp[s.length() - 1].first;
}

int solve2(string a) {
    int ans = 0;
    for (int i = 0; i + 1 < (int)a.length(); ++i) {
        if (a[i] != a[i + 1]) {
            ++ans;
        }
    }
    if (a[a.length() - 1] == '-') {
        ++ans;
    }
    return ans;
}

int main() {/*
    ifstream cin("in");
    ofstream cout("out2");*/
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        string s;
        cin >> s;
        cout << "Case #" << i + 1 << ": " << solve(s)<< "\n";
        if (solve(s) != solve2(s)) {
            exit(-1);
        }
    }
    return 0;
}
