#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;
double C, F, X;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int T;
    scanf("%d", &T);

    for(int t = 1; t <= T; t++)
    {
        scanf("%lf%lf%lf", &C, &F, &X);

        double ratio = 2.0;
        double init = 0.0;
        double best = X/ratio + init;

        for(int i = 0; i <= X; i++)
        {
            init += C/ratio;
            ratio += F;
            best = min(best, X/ratio + init);
        }

        printf("Case #%d: %.7lf\n", t, best);
    }

    return 0;
}
