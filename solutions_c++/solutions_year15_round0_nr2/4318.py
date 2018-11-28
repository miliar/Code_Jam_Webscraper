#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <math.h>
using namespace std;
const int maxn = 1005;
int D;
int P[maxn];
int dp[maxn][maxn];
int main()
{
    int T;
    freopen("codejam.ans","w",stdout);
    cin >> T;
    int cas = 1;
    while(T --)
    {
        cin >> D;
        int _max = 0;
        for(int i = 0; i < D; i ++)
        {
            cin >> P[i];
            _max = max(_max, P[i]);
        }
        for(int i = 0; i< D; i++)
        {
            for(int j = 1; j <= _max; j++)
            {
                dp[i][j] = ceil(1.0 * P[i] / j) - 1;
                dp[i][j] = max(0, dp[i][j]);
            }
        }
        int ans = 0x3f3f3f3f;
        for(int i=1; i<=_max; i++)
        {
            int t = i;
            for(int j=0; j<D; j++)
            {
                t += dp[j][i];
            }
            //printf("%d %d\n", i, t);
            ans = min(ans, t);
        }
        printf("Case #%d: %d\n",cas++, ans);
    }
    return 0;
}
