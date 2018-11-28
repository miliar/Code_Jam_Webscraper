#include <stdio.h>
#include <iostream>

#define error 0.00000000001

using namespace std;

int main(){
    int T;

    scanf("%i\n", &T);
    
    for (int t = 0; t < T; ++t){
        double time = 0.0000;
        double F = 2.000;       // Initial rate of cookies
        
        double X,XF,FF;
        scanf("%lf %lf %lf\n", &XF, &FF, &X);

        double time_with, time_without; // Time remaining with and without buying a farm

        while (1){
            time_without = X/F;
            time_with = XF/F + X/(F+FF);

            if ( (time_with + error) < time_without){    // Buy farm
                time += (XF/F);
                F += FF;
            } else {
                time += time_without;
                break;
            }
        }

        printf("Case #%i: %.7F\n", t+1, time);
    }
    return 0;
}
