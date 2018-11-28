#include <cstdio>
#include <math.h>
using namespace std;
int counter = 0;
double cookies = 0;
double time = 0;
double cur_rate, tte, ttf;
void work() {
    printf("Case #%d: ", ++counter);
    double c, f, x;
    scanf("%lf %lf %lf", &c, &f, &x);
    cur_rate = 2;
    time = 0;
    tte = x / cur_rate;
    ttf = c / cur_rate;
    while (time + tte  > time + ttf + (x / (cur_rate + f))) {
        cur_rate += f;
        time     += ttf;
        tte = x / cur_rate;
        ttf = c / cur_rate;
    }
    time += tte;
    printf("%.7f", time); 
    printf("\n");
    return;
}

int main() {
    int t; scanf("%d", &t);
    while(t--) {
        work();
    }
    return 0;
}