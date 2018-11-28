#include <bits/stdc++.h>

using namespace std;

template<class T>
using v = vector<T>;

void stupid()
{
    int n, k;
    cin >> n >> k;
    v<double> ps(n);
    for (int i = 0; i < n; ++i)
        cin >> ps[i];

    function<double(v<double>&, int)> make = [&](v<double> &ch, int pos) -> double
    {
        if (pos > n - 1 && ch.size() < k)
            return 0;
        if (ch.size() == k)
        {
            v<v<double>> dp(k + 1, v<double>(2 * k + 1));
            dp[0][k] = 1.0;
            for (int i = 1; i <= k; ++i)
            {
                dp[i][0] = (1 - ch[i - 1]) * dp[i - 1][1];
                dp[i][2 * k] = ch[i - 1] * dp[i - 1][2 * k - 1];
                for (int j = 1; j < dp[i].size() - 1; ++j)
                    dp[i][j] = dp[i - 1][j + 1] * (1 - ch[i - 1]) + dp[i - 1][j - 1] * ch[i - 1];
            }
            return dp[k][k];
        }
        double ans = 0;
        for (int i = pos; i < n; ++i)
        {
            ch.push_back(ps[i]);
            ans = max(ans, make(ch, i + 1));
            ch.pop_back();
        }
        return ans;
    };
    v<double> ch;
    cout.setf(ios::fixed);
    cout.precision(7);
    cout << make(ch, 0);
}


void solve()
{
    int n, k;
    cin >> n >> k;
    v<double> ps(n);
    for (int i = 0; i < n; ++i)
        cin >> ps[i];
    sort(ps.begin(), ps.end());
    int lp = 0;
    int rp = n - 1;
    v<double> ps2(2 * n + 1, 0);
    ps2[k] = 1.0;
    double ans = 0;
    for (int z = 0; z <= k; ++z)
    {
        v<double> ch;
        for (int j = 0; j < z; ++j)
            ch.push_back(ps[j]);
        for (int j = 0; j < (k - z); ++j)
            ch.push_back(ps[n - j - 1]);
        v<v<double>> dp(k + 1, v<double>(2 * k + 1));
        dp[0][k] = 1.0;
        for (int i = 1; i <= k; ++i)
        {
            dp[i][0] = (1 - ch[i - 1]) * dp[i - 1][1];
            dp[i][2 * k] = ch[i - 1] * dp[i - 1][2 * k - 1];
            for (int j = 1; j < dp[i].size() - 1; ++j)
                dp[i][j] = dp[i - 1][j + 1] * (1 - ch[i - 1]) + dp[i - 1][j - 1] * ch[i - 1];
        }
//        cerr << dp[k][k] << endl;
        ans = max(ans, dp[k][k]);
    }
    cout.setf(ios::fixed);
    cout.precision(7);
    cout << ans;
}

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        cout << "Case #" << i + 1 << ": ";
        solve();
        cout << endl;
    }
}