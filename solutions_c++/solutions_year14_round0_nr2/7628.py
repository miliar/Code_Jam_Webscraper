#include<stdio.h>

void processCookieCase(int testCaseNumber)
{
    double C,F,X;
    double requierdSec = 0.0;
    double currentF = 2.0;
    double currentCookies = 0.0;
    double remainingTimeIfBuy,remainingTimeIfNotBuy;
    bool shouldBuyFarm = false;

    scanf("%lf%lf%lf",&C,&F,&X);

    /* check weather farm value is more then the target */
    if( C < X )
    {
        do
        {
            if(currentCookies >= C)
            {
                /* decide weather or not buy a farm */
                double futureF = currentF + F;
                double shortOfTarget = X - currentCookies;

                remainingTimeIfNotBuy = (shortOfTarget/currentF);
                remainingTimeIfBuy = ((shortOfTarget+C)/futureF);

                shouldBuyFarm = (remainingTimeIfBuy < remainingTimeIfNotBuy)?
                                true : false ;

                if(shouldBuyFarm)
                {
                    currentF = futureF;
                    currentCookies -= C;
                }
                else
                {
                    requierdSec += remainingTimeIfNotBuy;
                    currentCookies += shortOfTarget;
                }
            }
            else
            {
                /* get minimum C cookies */
                double reqCookies = C - currentCookies;
                requierdSec +=  reqCookies / currentF ;
                currentCookies += reqCookies;
            }

        }while(currentCookies < X);
    }
    else
    {
        requierdSec = X/currentF;
    }

    printf("Case #%d: %.7lf\n",testCaseNumber,requierdSec);
}

int main()
{
    freopen("CookieClickerAlpha_ip.txt","r",stdin);
    freopen("CookieClickerAlpha_op.txt","w",stdout);

    int numberOfTestCases = 0;
    scanf("%d",&numberOfTestCases);

    for(int testCaseNumber=1; testCaseNumber<=numberOfTestCases; testCaseNumber++)
    processCookieCase(testCaseNumber);

    return 0;
}
