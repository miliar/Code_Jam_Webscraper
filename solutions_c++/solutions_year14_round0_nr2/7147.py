#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>

using namespace std;

int main()
{
    ifstream f("data.in");
    freopen("data.out", "w", stdout);
    int T;
    f >> T;
    for (int t = 1; t <= T; ++ t)
    {
        long double C, F, X;
        f >> C >> F >> X;
        long double ans = X / 2.0;
        long double sum = 0;
        int N = 0;
        while (sum + C / (2.0 + N * F) + X / (2.0 + (N+1) * F) < ans)
        {
            sum += C / (2.0 + N * F);
            ans = sum + X / (2.0 + (N+1) * F);
            ++ N;
        }
        double ret = ans;
        printf("Case #%d: %.7lf\n", t, ret);
    }
    return 0;
}
