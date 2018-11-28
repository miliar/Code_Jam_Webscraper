#include <bits/stdc++.h>

using namespace std;

int i,j,k,l,m,n,t, r, s;
string ans1, ans2, ans3;
double p[202];

int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    for (int test = 0; test < t; test++){
        cout << "Case #"<< test+1 << ": ";
        cin >> n >> k;
        for (i = 0; i < n; i++)
            cin >> p[i];
        sort (p, p + n);
        double ans = 0.0;
        for (i = 0; i <= k; i++) {
            vector <double> current;
            for (j = 0; j < i; j++){
                current.push_back(p[j]);
            }
            for (j = 0; j < k - i; j++){
                current.push_back(p[n - 1 - j]);
            }
            
            //solve the problem for current array, dp[i][j]: among the first 0..i, exactly j said yes
            /*for (j = 0; j < current.size(); j++){
                cout << current[j] << " ";
            }
            cout << "\n";*/
            double dp[202][202];
            memset(dp, 0, sizeof(dp));
            dp[0][0] = 1.0 - current[0];
            dp[0][1] = current[0];
            for (int ii = 1; ii < k; ii++){
                for (j = 0; j <= ii + 1; j++){
                    dp[ii][j] += dp[ii - 1][j] * (1.0 - current[ii]);
                    if (j > 0)
                    dp[ii][j] += dp[ii - 1][j - 1] * (current[ii]);
                    //cout << "dp gets " << dp[ii][j] << " coordinates " << ii << " " << j << "\n";
                }
            }
            if (ans < dp[k - 1][k / 2]) ans = dp[k - 1][k / 2];
            //cout << dp[k - 1][k / 2] << "\n\n";
        }
        cout.precision(8);
        cout << fixed << ans << "\n";
    }
    return 0;
}
