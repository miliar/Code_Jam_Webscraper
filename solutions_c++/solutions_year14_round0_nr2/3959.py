#include <cstdio>
#include <algorithm>
using namespace std;


double C, F, X;


void solve_case(int test_case)
{
    scanf("%lf %lf %lf", &C, &F, &X);

    double best = X/2;
    double construction_time = 0;
    double rate = 2;

    for (int farms = 1; farms <= X; farms++)
    {
        construction_time += C / rate;
        rate += F;
        best = min(best, construction_time + X/rate);
    }

    printf("Case #%d: %.7lf\n", test_case, best);
}


int main()
{
    int T; scanf("%d", &T);
    for (int t = 1; t <= T; t++)
        solve_case(t);

    return 0;
}
