#include <stdio.h>
#include <stdlib.h>

int main()
{
    freopen("B-large.in","rt",stdin);
    freopen("B-large.out","wt",stdout);
    int nTest;
    scanf("%d",&nTest);
    double C,F,X,bestTime,rate,cTime;
    for(int test = 1; test<= nTest;test++)
    {
        scanf("%lf %lf %lf",&C,&F,&X);
        bestTime = X/2;

        for(rate = 2,cTime = C/rate;bestTime>cTime + X/(rate + F);)
        {
            bestTime=cTime  + X/(rate + F);
            rate+=F;
            cTime += C/rate;
        }
        printf("Case #%d: %.7lf\n",test,bestTime);
    }
    return 0;
}
