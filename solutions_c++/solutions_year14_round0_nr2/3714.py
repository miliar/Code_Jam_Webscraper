#include <cstdio>
using namespace std;

int main()
{
    int kase;
    scanf("%d",&kase);
    for (int k=1; k<=kase;k++)
    {
        double C,F,X;
        scanf("%lf %lf %lf", &C, &F, &X);
        double current = 2.0;
        double ans = 0;
        if (C>=X)
            ans = X/current;
        else
        {
            while ((X-C)/current > X/(current+F))
            {
                //printf("%lf : %lf\n",current,C/current);
                ans+= C/current;
                current += F;
            }
            ans+= X/current;
        }

        printf("Case #%d: %.7lf\n",k, ans);
    }
    return 0;
}

