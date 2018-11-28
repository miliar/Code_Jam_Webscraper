#include <cstdio>
#include <cstdlib>

using namespace std;

int main()
{
    int cases;
    scanf("%d", &cases);
    for( int tt = 1; tt <= cases; tt++ )
    {
        double C, F, X, ans, pp = 2.0;
        scanf("%lf %lf %lf", &C, &F, &X);
        ans = X / 2.0;
        while(1)
        {
            double tmp = ans - X / pp + C / pp + X / (pp + F);
            pp += F;
            if( tmp > ans ) break;
            else ans = tmp;
        }
        printf("Case #%d: %.7f\n", tt, ans);
    }
    return 0;
}
