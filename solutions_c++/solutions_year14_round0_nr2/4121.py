#include<cstdio>
#include<iostream>

using namespace std;

int t;
double lasttime, farm, income, winner, x, y, z;

double czas(int l) {
    int i;
    double time;
    time=0;
    x=2;
    for (i=0; i<l; ++i) {
        time+=farm/x;
        x+=income;
    }
    time+=winner/x;
    return time;
}

int main() {
    double time;
    int i, j, k;
    scanf("%d", &t);
    for (j=1; j<=t; ++j) {
        lasttime=1000000004;
        scanf("%lf %lf %lf", &farm, &income, &winner);
        if (winner/farm-5<0) {
            y=0;
        } else {
            y=winner/farm-5;
        }
        for (i=y; i<y+10; ++i) {
            time=czas(i);
            if (time>lasttime) {
                time=lasttime;
                break;
            }
            /*
            if (i%10000==0) {
                printf("%.7lf   I!!! : %d\n", time, i);
            }
            */
            lasttime=time;
        }
        printf("Case #%d: %.7lf\n", j, time);
    }
    return 0;
}
