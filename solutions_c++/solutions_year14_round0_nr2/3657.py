#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    int k;
    scanf("%d", &k);
    for(int t=1; t<=k; t++) {
        double C,F,X;
        scanf("%lf %lf %lf", &C, &F, &X);

        double totalSecs = 0.0, minSecs = (X / 2.0) + 1;
        double full, next, production = 2.0;
        while( 1 ) {
            full = X / production;
            
            //printf("%lf %lf %lf %lf\n", totalSecs, minSecs, full, production);

            if( totalSecs + full > minSecs)
                break;
            
            minSecs = totalSecs + full;
            
            next = C / production;
            production += F;
            totalSecs += next;
        }

        printf("Case #%d: %.7lf\n", t, minSecs);
    }


    return 0;
}
