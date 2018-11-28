#include <bits/stdc++.h>
using namespace std;

double solve(vector<double> a) {
    int n = a.size();
    vector<vector<double>> dp(n, vector<double> (n + 1, 0));
    
    dp[0][1] = a[0];
    dp[0][0] = 1.0 - a[0];

    for(int i = 1; i < n; ++i)
        for(int j = 0; j <= (i + 1); ++j) {
            if(j - 1 >= 0)
                dp[i][j] += dp[i - 1][j - 1] * a[i];
            dp[i][j] += dp[i - 1][j] * (1.0 - a[i]);
        }

    return dp[n - 1][n / 2];
}

int main() {
    
    ifstream cin("testB.in");
    ofstream cout("testBlarge.out");

    int t; cin >> t;
    
    for(int t_case = 1; t_case <= t; ++t_case) {
        int n, k; cin >> n >> k;
        cout << "Case #" << t_case << ": ";

        vector<double> p(n, 0);
        for(int i = 0; i < n; ++i)
            cin >> p[i];
        
        double ans = 0.0;

        sort(p.begin(), p.end());
        
        for(int start = 0; start + (n - k) - 1 < n; ++start) {
            vector<double> who;
            for(int i = 0; i < n; ++i)
                if(i < start || i > start + (n - k) - 1)
                    who.push_back(p[i]);

            ans = max(ans, solve(who));
        }

        cout.precision(15);
        cout << ans << "\n";
    }
}
