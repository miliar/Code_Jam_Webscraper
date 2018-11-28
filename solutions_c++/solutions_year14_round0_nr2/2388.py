#include <cstdio>
int T,n;
double ans,t,C,F,X;
int main() {
    scanf("%d",&T);
    for (int K = 1;K <= T;K++) {
        scanf("%lf%lf%lf",&C,&F,&X);
        t = n = 0;ans = X/2.0;
        while (true) {
            t += C/(2+n*F);
            n++;
            if (ans > t+X/(2+n*F))
                ans = t+X/(2+n*F);
            else break;
        }
        printf("Case #%d: %.6lf\n",K,ans);
    }
    return 0;
}
