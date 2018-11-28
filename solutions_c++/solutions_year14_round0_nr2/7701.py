#include <bits/stdc++.h>

using namespace std;

int main()
{

    freopen("B-large_2.in","r",stdin);
    freopen("out.txt","w",stdout);

    int test, Case = 0;
    scanf("%d",&test);

    while (test--) {

        double C=0.0, F=0.0, X=0.0, T=0.0, Y=0.0, P=0.0, ANS=0.0;
        P = 2.0;

        scanf("%lf %lf %lf", &C, &F, &X);

            do {
                    ANS += T;
                    Y = X / P;
                    T = C / P;
                    P += F;
            }
            while( Y > T+(X/P) );

        ANS += Y;
        printf("Case #%d: %.7lf\n",++Case, ANS);
    }


    return 0;
}
