#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int MAX = 205;
int N,K;
double ans,p[MAX],dp[2][MAX];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int casei = 1; casei <= T; ++casei) {
        scanf("%d%d",&N,&K);
        for(int i = 0; i < N; ++i)
            scanf("%lf",&p[i]);
        sort(p, p + N);
        ans = 0;
        for(int i = 0; i < K + 1; ++i) {
            int now = 1, pre = 0;
            memset(dp,0,sizeof(dp));
            dp[now][0] = 1;
            for(int j = 0; j < N; ++j) {
                if(j < i || j > i + N - K - 1) {
                    swap(pre,now);
                    memset(dp[now],0,sizeof(dp[now]));
                    for(int k = 0; k <= N; ++k) {
                        dp[now][k] += dp[pre][k] * (1-p[j]);
                        if(k < N)
                            dp[now][k+1] += dp[pre][k] * p[j];
                    }
                }
            }
            ans = max(ans, dp[now][K/2]);
        }
        printf("Case #%d: %.9f\n",casei,ans);
    }
    return 0;
}
