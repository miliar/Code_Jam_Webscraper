#include <cstdio>

using namespace std;

int main()
{
    int t;
    scanf("%d", &t);

    double P, C, F, X;

    double tX;
    double res, res1;

    for(int k = 1; k <= t; k++){
        P = 2;
        scanf("%lf", &C);
        scanf("%lf", &F);
        scanf("%lf", &X);

        tX = 0;
        res = (X / P);
        for(int i = 0;; i++){
            tX += C / (P + i*F); // add new farm

            res1 = tX + (X / (P + (i+1)*F)); // get time with new farm

            if(res1 > res) break;

            res = res1;
        }

        printf("Case #%d: %lf\n", k, res);
    }
}
