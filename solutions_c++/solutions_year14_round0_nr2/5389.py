#include <iostream>
#include <cstdio>
#include <iomanip>
#define f cin
#define g cout

using namespace std;

int main()
{
    #ifndef ONLINE_JUDGE
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    #endif

    int T;
    long double rate, ans, F, C, X, cans, nans;

    f >> T;
    for (int t=1; t<=T; t++)
    {
        f >> C >> F >> X;

        rate=2.0;
        ans=X/rate;
        cans=0;

        for (int i=1; i<=10000000; i++)
        {
            cans+=C/rate;
            rate+=F;

            nans=cans + X/rate;
            ans=min(nans, ans);
        }

        g << "Case #" << t << ": " << fixed << setprecision(20) << ans << '\n';
    }

    return 0;
}

