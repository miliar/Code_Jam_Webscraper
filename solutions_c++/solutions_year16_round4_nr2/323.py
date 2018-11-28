//Problem B. Red Tape Committee
//By: phoenixinter@gmail.com
//May 28, 2016

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

vector<double> p;
double dp[201][201];

int main()
{
    int t, kase = 0;
    cin >> t;
    while (t--)
    {
        int n, k;
        cin >> n >> k;
        p.resize(n);
        for (int i = 0; i < n; i++)
            cin >> p[i];
        sort(p.begin(), p.end());
        double ans = 0;
        for (int leftCnt = 0; leftCnt <= k; leftCnt++)
        {
            vector<double> v;
            for (int i = 0; i < leftCnt; i++)
                v.push_back(p[i]);
            for (int i = n - (k - leftCnt); i < n; i++)
                v.push_back(p[i]);
            dp[0][0] = 1;
            for (int i = 1; i <= k; i++)
            {
                dp[i][0] = dp[i - 1][0] * (1 - v[i - 1]);
                for (int j = 1; j <= i; j++)
                    dp[i][j] = dp[i - 1][j] * (1 - v[i - 1]) + dp[i - 1][j - 1] * v[i - 1];
            }
            ans = max(ans, dp[k][k / 2]);
        }
        printf("Case #%d: %.8f\n", ++kase, ans);
    }
    return 0;
}