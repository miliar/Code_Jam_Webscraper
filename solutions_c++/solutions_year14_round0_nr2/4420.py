#include <cstdio>

int main()
{
    int TC;

    scanf("%d", &TC);

    for(int tc = 1; tc <= TC; ++tc)
    {
        double low = 0, up = 1e+12, mid = 0, ans = 0;
        double C, F, X, upperBound;
        scanf("%lf%lf%lf", &C, &F, &X);
                
        
        for(int iter = 0; iter < 150; iter++)
        {
            double res = 0, rate = 2, nowt = 0;
            mid = (low+up)/2;
            upperBound = (mid * F - C)/F;
            while(nowt < mid)
            {
                double plusTime = C/rate;
                if(plusTime + nowt > mid) plusTime = mid-nowt;
                //ending test!
                if(rate*(mid-nowt) + res >= X)
                {
                    res += rate*(mid-nowt);
                    break;
                }

                if(plusTime + nowt <= upperBound) //buy more
                {
                    rate += F;
                    nowt += plusTime;
                }
                else
                {
                    nowt += plusTime;
                    res += (plusTime * rate);
                }
            }

            if(res >= X) up = mid, ans = mid;
            else low = mid;
        }

        printf("Case #%d: %.9f\n", tc, ans);
    }
    return 0;
}
