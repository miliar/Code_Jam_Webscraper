#include <cstdio>
double C, F, X;
int main() {
        freopen("B-large.in","r",stdin);
        freopen("B.out","w",stdout);
        int T, ca=1;
        scanf("%d",&T);
        while(T--) {
                scanf("%lf%lf%lf",&C,&F,&X);
                double ans = -1;
                double nowTime = 0, nowRate = 2;
                for(;;) {
                        double tmp = nowTime + X / nowRate;
                        if(ans == -1 || tmp < ans) ans = tmp;
                        else break;
                        nowTime += C / nowRate;
                        nowRate += F;
                }
                printf("Case #%d: %.7f\n",ca++,ans);
        }
        return 0;
}
