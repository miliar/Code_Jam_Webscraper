#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

const double eps = 1e-9;

int main()
{
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int test = 1; test <= T; ++test)
    {
        double c, f, x;
        scanf("%lf %lf %lf", &c, &f, &x);

        double ans = 0;
        double speed = 2;
        for (int k = 0; k < 10000000; ++k)
        {
            if (x / speed + eps > c / speed + x / (speed + f))
            {
                ans += c / speed;
                speed += f;
            }
            else
            {
                ans += x / speed;
                break;
            }
        }

        printf("Case #%d: %.7f\n", test, ans);

    }


    return 0;
}