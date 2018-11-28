#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++)
    {
        printf("Case #%d: ", i + 1);
        double c, f, x;
        scanf("%lf %lf %lf", &c, &f, &x);
        double v = 2.0;
        double T = 0.0;

        for(;;)
        {
            double t1 = x / v;
            double t2 = c / v + x / (v + f);
            if (t2 < t1)
            {
                T += c / v;
                v += f;
            }
            else
            {
                T += x / v;
                printf("%.20lf\n", T);
                break;
            }
        }
    }
    return 0;
}
