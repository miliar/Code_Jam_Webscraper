#include <iostream>
#include <cstdio>

using namespace std;

int T, N;
double V, X;
double R[2], C[2];

int main()
{
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("B-small-attempt1.out", "w", stdout);

    scanf("%d", &T);

    for(int Ti = 1; Ti <= T; Ti++)
    {
        scanf("%d", &N);
        scanf("%lf %lf", &V, &X);

        for(int Ni = 0; Ni < N; Ni++)
            scanf("%lf %lf", &R[Ni], &C[Ni]);

        printf("Case #%d: ", Ti);

        if( N == 1 )
        {
            if( X != C[0] ) puts("IMPOSSIBLE");
            else printf("%.10f\n", V/R[0]);
        }
        else
        {
            if( C[0] > C[1] )
            {
                swap(C[0], C[1]);
                swap(R[0], R[1]);
            }

            if( X > C[0] && X > C[1] ) puts("IMPOSSIBLE");
            else if( X < C[0] && X < C[1] ) puts("IMPOSSIBLE");
            else if( X == C[0] && X == C[1] ) printf("%.10f\n", V/(R[0]+R[1]) );
            else if( X == C[0] ) printf("%.10f\n", V/R[0]);
            else if( X == C[1] ) printf("%.10f\n", V/R[1]);
            else
            {
                double rate = (X-C[0])/(C[1]-X);
                double t1 = V/(1+rate)/R[0];
                double t2 = V*rate/(1+rate)/R[1];

                printf("%.10f\n", max(t1, t2));
            }
        }
    }
}
