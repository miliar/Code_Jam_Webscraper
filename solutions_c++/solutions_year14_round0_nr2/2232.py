#include<cstdio>
#include<cstdlib>

double C, F, X, ans;

void DFS(double now, double prod){
    double tmp1, tmp2;
    tmp1 = now+X/prod;
    if(tmp1 < ans) ans = tmp1;
    if((X-C)/prod < X/(prod+F)) return;
    DFS(now+C/prod, prod+F);
    return;
}

void solve(void){
    ans = 100000000;
    double tmp1, tmp2;
    scanf("%lf%lf%lf", &C, &F, &X);
    DFS(0, 2);

    printf("%.7lf\n", ans);
    return;
}

int main(void){
    int T;
    scanf("%d", &T);
    for(int i = 1; i <= T; i++){
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
