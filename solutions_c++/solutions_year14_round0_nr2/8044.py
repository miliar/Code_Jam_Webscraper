#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>
using namespace std;


int main()
{
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    int cas, case_id = 0;
    double c, f, x, rate, t;
    scanf("%d", &cas);
    while(cas --)
    {
        scanf("%lf%lf%lf", &c, &f, &x);
        rate = 2, t = 0;
        while(1)
        {
            double t1 = x / rate;
            double t2 = c / rate;
            if (x <= c)
            {
                t += t1;
                break;
            }
            if (x / (rate + f) + t2 < t1)
            {
                rate += f;
                t += t2;
            }
            else
            {
                t += t1;
                break;
            }
        }
        printf("Case #%d: %.9lf\n", ++case_id, t);

    }
}
