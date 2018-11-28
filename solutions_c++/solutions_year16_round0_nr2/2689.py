#include <bits/stdc++.h>

using namespace std;

void solve()
{
    string s;
    cin >> s;
    int n = s.size();
    int dp[n + 1][2];
    dp[0][0] = dp[0][1] = 0;
    for(int i = 1; i <= n; i++)
    {
        dp[i][0] = dp[i][1] = 1e9;
        for(int j = i; j >= 1; j--)
        {
            if(s[j - 1] == '-')
                break;
            dp[i][0] = min(dp[i][0], dp[j - 1][1] + 1);
            dp[i][1] = min(dp[i][1], dp[j - 1][1]);
        }
        for(int j = i; j >= 1; j--)
        {
            if(s[j - 1] == '+')
                break;
            dp[i][0] = min(dp[i][0], dp[j - 1][0]);
            dp[i][1] = min(dp[i][1], dp[j - 1][0] + 1);
        }
    }
    cout << dp[n][1] << "\n";
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for(int i = 0; i < t; i++)
    {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
}
