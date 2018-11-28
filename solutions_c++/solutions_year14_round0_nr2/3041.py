//
//  CookieClicker.cpp
//  
//
//  Created by John Nevard on 4/11/14.
//
//

#include <cstdio>
#include <vector>
using namespace std;

int main() {
    int nc;
    scanf("%d", &nc);
    for (int i = 1; i <= nc; ++i) {
        double c, f, x, rate = 2.0, time = 0.0, total = 0.0;
        scanf("%lf %lf %lf", &c, &f, &x);
        for (;;) {
            double t0 = (x - total) / rate;
            double t1 = (c - total) / rate;
            double t2 = x / (rate + f);
            if (t0 < t1 + t2) {
                time += t0;
                break;
            } else {
                time += t1;
                total = 0.0;
                rate += f;
            }
        }
        printf("Case #%d: %.7lf\n", i, time);
    }
    return 0;
}