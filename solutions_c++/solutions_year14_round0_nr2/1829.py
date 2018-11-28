#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <sstream>
#include <cstring>
#include <vector>
#include <map>
#include <set>
using namespace std;

double c, f, x, cr;
int main() {    
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%lf %lf %lf", &c, &f, &x);
        cr = 2;
        double ans = x / cr;
        double curt = 0;
        double tsum = 0;
        while (true) {
            curt += c / cr;
            if (curt >= ans) break;
            cr += f;
            tsum = curt + x / cr;
            if (tsum < ans) ans = tsum;
        }
        printf("Case #%d: ", t);
        printf("%.9lf", ans);
        printf("\n");
    }
}

