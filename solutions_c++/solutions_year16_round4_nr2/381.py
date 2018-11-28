#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;

const int MAX = 200 + 10;

double rec[MAX];
double now[MAX];
double dp[MAX][MAX];

double calc(int n){
    memset(dp, 0, sizeof(dp));
    dp[0][1] = now[0];
    dp[0][0] = 1.0 - now[0];
    for(int i = 1 ; i < n ; i++){
        for(int j = 0 ; j <= i ; j++){
            dp[i][j+1] += dp[i-1][j] * now[i];
            dp[i][j] += dp[i-1][j] * (1-now[i]);
        }
    }
    return dp[n-1][n/2];
}

int main(){
    int TN;
    scanf("%d", &TN);
    for(int casen = 1 ; casen <= TN ; casen++){
        printf("Case #%d: ", casen);
        int n, k;
        scanf("%d %d", &n, &k);
        for(int i = 0 ; i < n ; i++){
            scanf("%lf", &rec[i]);
        }
        sort(rec, rec+n);
        for(int i = 0 ; i < n ; i++) now[i] = rec[i];
        double ans = calc(k);
        for(int i = 1 ; i <= k ; i++){
            now[k-i] = rec[n-i];
            double newans = calc(k);
            ans = max(ans, newans);
        }
        printf("%.7f\n", ans);
    }
    return 0;
}
