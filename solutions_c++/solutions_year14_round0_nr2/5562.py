#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);

    int test;
    scanf("%i", &test);
    for(int i = 0; i < test; i++) fprintf(stderr, "-"); fprintf(stderr, "\n");
    for(int t = 1; t <= test; t++)
    {
        double c, f, x;
        scanf("%lf %lf %lf", &c, &f, &x);

        double buy_ = ((x - c) * f / c - 2.0) / f;
        int buy = buy_;
        if(buy_ - (double)buy > 1e-6) buy++;
        if(buy_ < 0) buy = 0;
        //printf("%i\n", buy);

        double res = 0;
        for(int i = 0; i < buy && ((double)i * f < 1e8); i++) res += c / (2.0 + (double)i * f);
        res += x / (2.0 + (double)buy * f);
        printf("Case #%i: %.7lf\n", t, res);
        fprintf(stderr, "+");
    }
    return 0;
}
