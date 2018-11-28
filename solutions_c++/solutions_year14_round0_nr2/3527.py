#include <iostream>
#include <cstdio>

using namespace std;

int main(void)
{
    int t;
    scanf("%i", &t);
    for (int i = 1; i <= t; i++)
    {
        double c,f,x;
        scanf ("%lf %lf %lf", &c, &f, &x);
        double res = 0;
        double delta = 2;
        res += min(x,c)/delta;
        if (c < x)
        {
            // think over counting result of this cycle at once
            while (c + delta * c/f < x)
            {
                delta += f;
                res += c/delta;
            } 
            res += (x-c)/delta;
        }
        printf("Case #%i: %.7lf\n", i, res);
    }
    return 0;
}
