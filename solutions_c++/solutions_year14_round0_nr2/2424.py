#include<stdio.h>
int T;
double C,F,X;

int main() {
    freopen("cookie.in","r",stdin);
    freopen("cookie.out","w",stdout);
    scanf("%d",&T);
    for(int t=1;t<=T;++t) {
        printf("Case #%d: ",t);
        scanf("%lf%lf%lf",&C,&F,&X);
        bool ok=0;
        double N=2.0;
        double rez = 1.0*X/N;
        while(true) {
            if(rez <= rez - 1.0*X/N + 1.0*C/N + 1.0*X/(N+F)) {
                break;
            } else {
                rez = rez - 1.0*X/N + 1.0*C/N + 1.0*X/(N+F);
                N += F;
            }
        }
        printf("%.10lf\n",rez);
    }
    return 0;
}
