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
    int cases, case_id;
    double c, f, x, rate, t;
    for (scanf("%d", &cases), case_id = 1; case_id <= cases; case_id ++)
    {
        scanf("%lf%lf%lf", &c, &f, &x);
        rate = 2, t = 0;
        while(x > 0)
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
                //printf("%lf %lf\n", rate, t);
            }
            else
            {
                t += t1;
                break;
            }
        }
        printf("Case #%d: %.9lf\n", case_id, t);

    }
}
