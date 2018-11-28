#include <cstdio>
using namespace std;

int main()
{
    int tcase;
    scanf ("%d", &tcase);
    for (int i = 1; i <= tcase; i++)
    {
        double C, F, X, ans = 0.0, rate = 2.0;
        scanf ("%lf%lf%lf", &C, &F, &X);
        
        double init = X/rate ;
        double follow = C/rate + (X/(rate + F));
        while ( init > follow )
        {
              ans += (C/rate);
              rate += F;
              init = X/rate;
              follow = C/rate + (X/(rate + F));
        }
        
        ans += init;
        printf ("Case #%d: %.7lf\n", i, ans);
    }
    return 0;
}
