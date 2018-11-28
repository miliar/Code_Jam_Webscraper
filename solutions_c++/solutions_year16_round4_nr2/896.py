//writed by dnvtmf
#include <bits/stdc++.h>
#define INF 1000000007
#define FI first
#define SE second
#define PB push_back
#define VI vector<int>
using namespace std;
typedef long long LL;
typedef pair <int, int> P;
const int NUM = 220;
int N, K;
double p[NUM];
double dp[2][NUM][NUM];//dp[n][i] the probability of i in n person who votes "YES"
double check_ans;
void check(int i, int k, int mask)
{
    if(k > K) return ;
    if(i == N)
    {
        if(k != K) return ;
        memset(dp[0], 0, sizeof(dp[0]));
        dp[0][0][0] = 1.0;
        for(int i = 0; i < N; ++i)
        {
            if(!(mask & (1 << i))) continue;
            for(int j = K; j >= 0; --j)
            {
                for(int k = 0; k <= j; ++k)
                {
                    dp[0][j + 1][k + 1] += dp[0][j][k] * p[i];
                    dp[0][j + 1][k] += dp[0][j][k] * (1.0 - p[i]);
                }
            }
        }
        check_ans = max(check_ans, dp[0][K][K / 2]);
        return ;
    }
    check(i + 1, k, mask);
    check(i + 1, k + 1, mask | (1 << i));
}
int main()
{
#ifdef ACM_TEST1
    freopen("in.txt", "r", stdin);
//  freopen("in.txt", "w", stdout);
#else
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
#endif
    int T; scanf("%d", &T);
    for(int cas = 1; cas <= T; ++cas)
    {
        printf("Case #%d: ", cas);
        scanf("%d%d", &N, &K);
        for(int i = 0; i < N; ++i) scanf("%lf", &p[i]);
//        memset(dp, 0, sizeof(dp));
//        dp[0][0][0] = 1.0;
//        int now = 0, nxt = 1;
//        for(int i = 1; i <= N; ++i)
//        {
//            //memcpy(dp[nxt], dp[now], sizeof(dp[nxt]));//i'th not't select
//            memset(dp[nxt], 0, sizeof(dp[nxt]));
//            for(int j = i - 1; j >= 0; --j)//j person vote
//            {
//                for(int k = 0; k <= j; ++k)// k person vote "YES"
//                {
//                    dp[nxt][j + 1][k + 1] = max(dp[nxt][j + 1][k + 1], dp[now][j][k] * p[i]);
//                    dp[nxt][j + 1][k] = max(dp[nxt][j + 1][k], dp[now][j][k] * (1 - p[i]));
//                }
//            }
//            for(int j = 0; j <= i; ++j)
//                for(int k = 0; k <= j; ++k)
//                    dp[nxt][j][k] = max(dp[nxt][j][k], dp[now][j][k]);
//            swap(now, nxt);
//        }
//        printf("%.10f\n", dp[now][K][K / 2]);
        check_ans = 0.0;
        check(0, 0, 0);
        printf("%.10f\n", check_ans);
    }
    return 0;
}
