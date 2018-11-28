#include <iostream>
#include <stdio.h>
#include <string.h>
const double EPS = 1e-9;
double cost, f, x;
int main(){     freopen("B-large.in", "r", stdin);
                freopen("B-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int TT=1; TT<=T; TT++){\
        scanf("%lf %lf %lf", &cost, &f, &x);\
        double ans=111111.0, v=2.0, now=0.0, pt=0.0;
        for(int i=1; i<=x; i++){
            now = x/v + pt;     // new time + _ttl update
            if( ans > now )    ans = now;
            else               break;
            pt += cost/v;       // last ttl update
            v += f;             // last v update
        }
        printf("Case #%d: %.7lf\n", TT, ans);
    }
    return 0;
}
