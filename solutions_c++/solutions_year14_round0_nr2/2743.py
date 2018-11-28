#include<iostream>
#include<cstdio>

using namespace std;

int main() {
    int t, k;
    scanf("%d", &t);
    for(k=1; k<=t; k++) {

        double c,f,x,time=0.0;
        double s = 2.0;  //start value

        scanf("%lf%lf%lf", &c, &f, &x);

        while(true) {
            if((x/s) < (c/s + x/(s+f))) {
                time += x/s;
                break;
            }
            else {
                time += c/s;
                s += f;
            }
        }

        printf("Case #%d: %.7lf\n", k, time);

    }
    return 0;
}

