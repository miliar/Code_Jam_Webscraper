#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;
int T;
double C, F, X;
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("test.out", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        scanf("%lf %lf %lf", &C, &F, &X);
        double ret = X / 2.0;
        double speed = 2.0;
        double total = 0;
        for (int i = 0; i <= X / C + 1; i++) {
            total += C / speed;
            speed += F;
            ret = min(total + X / speed, ret);
        }
        printf("Case #%d: %.7lf\n", cas, ret);
    }
    return 0;
}
