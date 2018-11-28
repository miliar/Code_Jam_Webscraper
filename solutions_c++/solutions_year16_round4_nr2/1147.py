#include <bits/stdc++.h>
using namespace std;
double p[300];
double dp[300][300];
void Solve(){
    int N, K;
    scanf("%d %d", &N, &K);
    for(int i=0;i<N;i++)
        scanf("%lf", &p[i]);
    sort(p, p+N);
    vector<double> s;
    s.push_back(0);
    for(int i=0;i<K/2;i++){
        s.push_back(p[i]);
        s.push_back(p[N-1-i]);
    }
    dp[0][0] = 1;
    for(int i=1;i<=K;i++){
        for(int j=0;j<=K;j++){
            dp[i][j] = dp[i-1][j-1] * s[i] + dp[i-1][j] * (1.0 - s[i]);
        }
    }
    printf("%lf\n", dp[K][K/2]);
}
int main(){
    int T;
    scanf("%d", &T);
    int t =1;
    while(T--){
        printf("Case #%d: ", t++);
        Solve();
    }
    return 0;
}
