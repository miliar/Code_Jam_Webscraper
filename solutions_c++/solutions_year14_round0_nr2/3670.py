#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

double C, F, X;

void init()
{
    scanf("%lf %lf %lf", &C, &F, &X);
}

double work()
{
    double res = 0;
    
    double curG = 0, v = 2.0;
    
    while (curG < X)
    {
        double t1 = (X - curG) / v;
        double t2 = C / v + (X - curG) / (v + F);
        if (t1 <= t2)
        {
            curG = X;
            res += t1;
        }
        else
        {
            curG = 0;
            res += C/v;
            v += F;
        }
    }
    
    return res;
}


int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    
    int T;
    scanf("%d", &T);
    
    for (int tim=1; tim<=T; tim++)
    {
        init();
        printf("Case #%d: %.7f\n", tim, work());
    }
    return 0;
}
