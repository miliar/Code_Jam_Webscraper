#include <stdio.h>
#include <algorithm>
#include <string.h>

using namespace std;

int main(){
    int t;
    double c, f, x, time, rate;

    scanf("%d", &t);
    for(int nt = 1; nt <= t; ++nt){
        scanf(" %lf %lf %lf", &c, &f, &x);
        rate = 2.0;
        time = 0.0;
        while(x/rate > (c/rate + x/(rate+f))){
            time += c/rate;
            rate += f;
        }
        time += x/rate;
        printf("Case #%d: %.7lf\n", nt, time);
    }

    return 0;
}
