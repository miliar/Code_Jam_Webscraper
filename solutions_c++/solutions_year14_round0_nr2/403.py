#include <cstdio>

using namespace std;

int main(void)
{
    int t, tc=0;
    double r, c, f, x, res;
    for (scanf("%d", &t);t--;)
    {
        res=0.0;
        scanf("%lf%lf%lf", &c, &f, &x);
        for (r=2.0;x/r>c/r+x/(r+f);)
        {
            res+=c/r;
            r+=f;
        }
        res+=x/r;
        printf("Case #%d: %.7lf\n", ++tc, res);
    }
    return 0;
}
