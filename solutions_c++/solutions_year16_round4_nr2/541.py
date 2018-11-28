/*
* @Author: Comzyh
* @Date:   2016-05-28 23:28:54
* @Last Modified by:   Comzyh
* @Last Modified time: 2016-05-28 23:51:44
*/
#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
double P[201];
double get_p(const vector<double> &ps)
{
    int n = ps.size();
    static double dp[201][101]; //[front][yes]
    memset(dp, 0, sizeof(dp));
    dp[0][0] = 1;
    for (int i = 1; i <= n ; i++)
        for (int j = 0 ; j <= min(i , n / 2); j ++)
        {
            dp[i][j] += dp[i - 1][j] * (1.0 - ps[i - 1]); // no
            if (j)
                dp[i][j] += dp[i - 1][j - 1] * ps[i - 1]; // yes
        }
    return dp[n][n / 2];
}
int T, N, K;
int main()
{
    scanf("%d", &T);
    for (int TT = 1; TT <= T; TT++)
    {
        scanf("%d%d", &N, &K);
        for (int i = 0; i < N; i++)
            scanf("%lf", &P[i]);
        sort(P, P + N);
        vector<double> ps;
        ps.resize(K);
        double ans = 0;
        for (int left = 0; left <= K; left++)
        {
            int right =  K - left;
            for (int j =0; j < left; j ++)
                ps[j] = P[j];
            for (int j = 0; j < right; j ++)
                ps[left + j] = P[N - right + j];

            ans = max(ans, get_p(ps));
        }
        printf("Case #%d: %.12lf\n", TT, ans);
    }
    return 0;
}