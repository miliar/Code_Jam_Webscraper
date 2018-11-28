#include <iostream>
#include <cstdio>
using namespace std;
int a[10][10],b[10][10],c[10],d[10],p,q;
int main(){
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    cin >> T;
    for (int o = 1; o <= T; o++){
        double C,F,X;
        scanf("%lf%lf%lf", &C, &F, &X);
        if (X <= C){
            printf("Case #%d: %.6f\n",o, X / 2);
            continue;
        }
        double ans = 0, inc = 2, now = 0;
        while (1){
            if(X / inc < C / inc + X / (inc + F)){
                ans += X / inc; break;
            } else {
                ans += C / inc; inc += F;
            }
        }
        printf("Case #%d: %.6f\n",o, ans);
    }
}
