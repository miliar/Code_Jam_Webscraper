#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    freopen("infile.in", "r", stdin);
    freopen("outfile.txt", "w", stdout);
    int t, p=1;
    double c, f, x, r;
    scanf("%d", &t);
    w1: while(t--)
    {
        double ans=0.0;
        r=2.0;
        scanf("%lf%lf%lf", &c, &f, &x);
        while(1) {
            if(ans + c/r + x/(r+f)< ans + x/r)
            {
                ans+=c/r;
                r+=f;
            }
            else
            {
                printf("Case #%d: %.7lf\n", p, ans + x/r);
                p++;
                goto w1;
            }
        }
        p++;
    }
    return 0;
}
