#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    FILE *in, *out;
    in = fopen("B-small-attempt4.in","r");
    out = fopen("1.out", "w");
    int n; fscanf(in, "%d", &n);
    for (int t=1; t<=n; t++)
    {
        double C, F, X, base = 2, ans = 0;
        fscanf(in, "%lf%lf%lf", &C, &F, &X);
        while ( 1 ) 
        {
            double p = base + F, q = C/base+X/p, tt = X/base;
            if (C/base + X/(base+F) < X/base)
            {
                ans  += C/base;
                base += F;
            }else break;
        }
        ans += X/base;
        fprintf(out, "Case #%d: %.7lf\n", t, ans);
        //printf("Case #%d: %.7lf\n", t, ans);
    }
    //system("pause");
    return 0;
}
