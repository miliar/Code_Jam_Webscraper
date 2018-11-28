/// This code is a pure govnocode
#include <bits/stdc++.h>
#define DEBUG(x) cout << #x << " = " << x << endl;
using namespace std;
const double ONE = 1e+0;
const int MAXN = 16;
const int MAX_MASK = (1 << 16) + 5;

double dp[MAX_MASK][2 * MAXN + 5];
double p[MAXN];

int one_count(int x)
{
    int res = 0;
    while(x != 0)
    {
        res += (x % 2);
        x /= 2;
    }
    return res;
}

int main()
{
    freopen("inputB.in", "r", stdin);
    freopen("outputB.out", "w", stdout);

    int _T;
    cin >> _T;
    cout << setprecision(20) << fixed;

    for (int _t = 1; _t <= _T; _t++)
    {
        int N, K;
        cin >> N >> K;
        for (int i = 1; i <= N; i++)
        {
            cin >> p[i];
            p[i] *= ONE;
        }

        double ans = 0.0;
        dp[0][MAXN] = ONE;
        for (int mask = 1; mask < (1 << N); mask++)
        {
            for (int balance = -N; balance <= N; balance++)
            {
                dp[mask][balance + MAXN] = 0.0;
                if (one_count(mask) >= abs(balance))
                {
                    int i = 1;
                    int bit = 1;
                    while((bit & mask) == 0) { bit *= 2; i++; }
                    dp[mask][balance + MAXN] =         p[i] * dp[mask ^ bit][(balance - 1) + MAXN] +
                                               (ONE - p[i]) * dp[mask ^ bit][(balance + 1) + MAXN];
                }
            }

            if (one_count(mask) == K)
            {
                ans = max(ans, dp[mask][MAXN]);
            }
        }

        //DEBUG(dp[2][MAXN + 1]);
        for (int i = 0; i < K; i++)
            ans /= ONE;

        cout << "Case #" << _t << ": " << ans << endl;
    }

    return 0;
}
