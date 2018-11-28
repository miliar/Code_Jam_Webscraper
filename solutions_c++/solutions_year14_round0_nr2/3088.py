#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cstdio>
using namespace std;

double C, F, X;
double f[1000001];

void init()
{
    scanf("%lf %lf %lf\n", &C, &F, &X);
}

void prepare()
{
    f[0] = 0;
    for(int i = 1 ; i <= 1000000 ; i++)
    {
        f[i] = f[i - 1] + (2 + F * (i - 1));
    }
}

void work()
{
    double best = 1e99;
    int i = 0;
    double f = 0;
    while(1)
    {
        if(X / (2 + F * i) + f < best)
        {
            best = X / (2 + F * i) + f;
            i++;
            f = f + (C / (2 + F * (i - 1)));
        }
        else break;
    }
    printf("%.7lf\n", best);
}

int main()
{
    freopen("qb.in", "r", stdin);
    freopen("qb.out", "w", stdout);
    int tt;
    scanf("%d", &tt);
    for(int i = 1 ; i <= tt ; i++)
    {
        printf("Case #%d: ", i);
        init();
        work();
    }
    return 0;
}
