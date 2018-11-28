#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int k, n;
const int MXN = 16;

double P[MXN];

double dp[(1<<MXN)][1+MXN];

static int cntB(int v)
{
    int ans=0;
    while (v){if(v&1) ans++;
        v/=2;
    }
    return ans;
}

double solve()
{
    double ans = 0;
    dp[0][0] = 1;
    for (int m=1; m<(1<<n); m++)
    {
        int j=0;
        while ((m & (1<<j)) == 0)j++;
        int prev = m ^ (1<<j);
        int bc = cntB(m);

        dp[m][bc] = 0;
        for (int i=0; i<bc; i++)
        {
            dp[m][i] = dp[prev][i] * (1-P[j]);
        }
        for (int i=1; i<=bc; i++)
        {
            dp[m][i] += dp[prev][i-1] * P[j];
        }
        if (bc == k)
        {
            ans = max(ans, dp[m][k/2]);
        }
        /*for (int i=0; i<=bc; i++) {
            printf("m:%d j:%d %f i:%d %f\n", m, j, P[j], i, dp[m][i]);
        }*/
    }
    return ans;
}

int main()
{
    int t;
    scanf("%d", &t);
    for (int i=1; i<=t; i++)
    {
        scanf("%d %d", &n, &k);
        for (int i=0; i<n; i++) scanf("%lf", P+i);
        printf("Case #%d: %.7f\n", i, solve());
    }
}
