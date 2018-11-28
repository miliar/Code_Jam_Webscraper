#include <cstdio>
#include <algorithm>
#include <iostream>

using namespace std;

int main () {
    int T;
    double c,f,x, currenttime, currentrate, besttime, currentfinishtime;
    scanf("%d", &T);
    for (int cases = 1; cases <= T; cases ++) {
        scanf("%lf %lf %lf", &c, &f, &x);
        currenttime = 0.0;
        currentrate = 2.0;
        besttime = x / currentrate;
        while (besttime > currenttime + c / currentrate + x/ (currentrate + f)) {
            currenttime += c/currentrate;
            currentrate += f;
            besttime = currenttime + x / currentrate;
        }
        printf("Case #%d: %.7lf\n", cases, besttime);
    }
}
