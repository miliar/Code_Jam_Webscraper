#include <stdio.h>
#include <math.h>
#include <iostream>

using namespace std;


double C,F,X;

int main()
{
    freopen("B.in","rt",stdin);
    freopen("B.out","wt",stdout);
    int tst,cas;
    scanf("%d",&tst);
    for(cas=1;cas<=tst;cas++) {
        scanf("%lf%lf%lf",&C,&F,&X);

        double mn = X;
        double sum = 0;
        double speed = 2;

        for(int i=0;i<=1000000;i++) {

            if( sum*C + X/speed < mn) mn = sum*C + X/speed;
            sum += (1/speed);
            speed += F;

        }
        printf("Case #%d: %.7lf\n",cas,mn);

    }
    return 0;
}
