#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

int T;
double C, F, X, CrtTime, CrtRatio, Ans;

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);

    scanf("%i", &T);
    for(int t = 1; t <= T; ++ t)
    {
        printf("Case #%i: ", t);

        scanf("%lf %lf %lf", &C, &F, &X);

        Ans = 1.0 * 0x3f3f3f3f;
        CrtTime = 0;
        CrtRatio = 2.0;
        for(int i = 0; i <= 100000; ++ i)
        {
            Ans = min(Ans, CrtTime + X / CrtRatio);
            CrtTime += C / CrtRatio;
            CrtRatio += F;
        }

        printf("%.7lf\n", Ans);
    }
}
