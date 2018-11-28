#include<stdio.h>

int main()
{
    int T, x, i;
    double C, F, X, y, f;
    scanf("%d", &T);
    for(x = 1; x <= T; x++) {
        scanf("%lf %lf %lf", &C, &F, &X);
        y = X/2;
        f = C/2;
        i = 1;
        while(f + X/(2+i*F) < y) {
            y = f + X/(2+i*F);
            f = f + C/(2+i*F);
            i++;
        }
        printf("Case #%d: %.7lf\n", x, y);
    }
    return 0;
}
