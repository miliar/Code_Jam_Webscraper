#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int test;
    scanf("%d", &test);
    for (int i = 1; i <= test; ++i)
    {
        double c, f, x;
        scanf("%lf %lf %lf", &c, &f, &x);
        int maxk = x/c;
        double time = 0, sum = 0, ans = -1;
        for (int k = 0; k <= maxk; ++k)
        {
            if (k > 0)
                time += (c/(f*(k-1) + 2));
            sum = time + (x / (f*k + 2));
            if (ans == -1 || sum < ans)
                ans = sum;
        }
        printf("Case #%d: %.7lf\n", i, ans);
    }
    return 0;
}
