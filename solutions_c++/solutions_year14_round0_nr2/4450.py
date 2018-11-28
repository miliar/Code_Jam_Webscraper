#include <stdio.h>

int main ()
{
    int T;
    double C, F, X;
    double farmt, deltat, v;
    scanf("%d", &T);
    for (int i = 0; i < T; ++i)
    {
        // Take input
        scanf("%lf %lf %lf", &C, &F, &X);

        // Initialize
        farmt = 0;
        deltat = 0;
        v = 2 - F;

        // Calculate
        do
        {
            v += F;
            deltat = farmt + X/v;
            farmt += C/v;
        } while (deltat > farmt + X/(v+F));

        // Print result
        printf("Case #%d: %.7f\n", i+1, deltat);
    }
}
