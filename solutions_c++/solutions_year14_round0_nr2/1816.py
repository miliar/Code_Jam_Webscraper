#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int nTests;
    scanf("%d", &nTests);
    for (int iTest = 0; iTest < nTests; ++iTest)
    {
        double c, f, x;
        scanf("%lf%lf%lf", &c, &f, &x);

        int k = 0;
        double best = 1e10;
        double now = 1e9;
        
        double prod = 2.0;
        double bases = 0.0;
        while (bases + x/prod < best)
        {
            best = bases + x/prod;
            bases += c/prod;
            prod += f;
        }
        printf("Case #%d: %.8lf\n", iTest + 1, best);
    }
    
    return 0;
}