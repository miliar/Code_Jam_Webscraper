/**
used Codeblocks C++ lang ( free online )
**/
#include <cstdio>

#define EPS 0.0000001

using namespace std;
double C,F,X,crt,prod,best;
int tstcase;

void read()
{
    scanf("%lf%lf%lf",&C,&F,&X);
    best = X / (1.0*prod);
}

void solve()
{
    while(best + EPS > C / (1.0*prod) + crt + X / (1.0*(prod + F)) ) /// two choices
    {
        best = C / (1.0*prod) + crt + X / (1.0*(prod + F)); /// continue buying a cookie farm
        crt += C / (1.0 * prod);
        prod += F;
    } /// or we just wait to get all cookies from now :D
    printf("Case #%d: %.7lf\n",tstcase,best);
}

int main()
{
    freopen("cookie.in","r",stdin);
    freopen("cookie.txt","w",stdout);

    int T;
    scanf("%d",&T);
    while(T--)
    {
        ++tstcase;
        prod = 2; /// initializare
        crt = 0;
        read();
        solve();
    }

    return 0;
}
