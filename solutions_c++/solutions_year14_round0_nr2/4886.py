#include <cstdio>

long double solve(long double C, long double F, long double X) 
{
    long double s, total;
    total = X / 2;
    int farms = 1;

    do {
        s = total;
        total = 0;
        for(int f = 0; f < farms; f++) {
            total += C / (2 + F*f);
        }
        total += X / (2 + F*farms);
        farms++;
    } while (total < s);
    return s;
}

int main()
{
    int T;
    long double C, F, X;
    scanf("%d", &T);
    for(int t = 1; t <= T; t++) {
        scanf("%Lf%Lf%Lf", &C, &F, &X);
        printf("Case #%d: %.7Lf\n", t, solve(C, F, X));
    }
}
