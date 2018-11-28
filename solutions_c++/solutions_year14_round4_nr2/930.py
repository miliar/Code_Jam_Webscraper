#include <cstdio>
#include <iostream>

using namespace std;

const int INF = 1000000009;
const int MAXN = 1009;

int dp[MAXN][MAXN];
int a[MAXN];

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int TC;
    cin >> TC;
    for (int tc = 1; tc <= TC; tc++)
    {

        for (int i = 0; i < MAXN; i++)
            for (int j = 0; j < MAXN; j++)
                dp[i][j] = INF;
        dp[0][0] = 0;

        int N;
        cin >> N;
        for (int i = 0; i < N; i++)
            scanf("%d", a + i);

        int S = N;

        for (int k = 0; k < N; k++)
        {
            int mp = 0;
            for (int i = 0; i < S; i++)
            {
                if (a[i] < a[mp])
                    mp = i;
            }

            for (int i = 0; i <= k; i++)
            {
                dp[i+1][k-i] = min(dp[i+1][k-i], dp[i][k-i] + mp);
                dp[i][k-i+1] = min(dp[i][k-i+1], dp[i][k-i] + S - mp - 1);
            }

            for (int i = 0; i < S; i++)
            {
                if (i >= mp)
                {
                    a[i] = a[i+1];
                }
            }
            S--;

        }

        int ans = INF;
        for (int i = 0; i <= N; i++)
        {
            ans = min(ans, dp[i][N-i]);
        }
        cout << "Case #" << tc << ": " << ans << endl;
    }
}
