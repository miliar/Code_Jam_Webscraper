#include <cstdio>
using namespace std;
int main () {
    int T;
    scanf("%d", &T);
    for(int a=1; a<=T; a++){
        double C, F, X, cps=2.0,time=0.0;
        scanf("%lf", &C);
        scanf("%lf", &F);
        scanf("%lf", &X);
        while((X/cps)>((C/cps)+X/(cps+F))){
            time+=C/cps;
            cps+=F;
        }
        printf("Case #%d: %.7f\n",a,(X/cps+time));
    }
};
