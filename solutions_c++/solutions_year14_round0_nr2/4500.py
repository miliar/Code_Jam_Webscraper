#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int main() {
    int  cases;
    scanf("%d", &cases);
    double C, F, X;
    for (int T = 1; T <= cases; T++) {
        scanf("%lf %lf %lf", &C, &F, &X);
        double best = 1e10;
        double farm = 0;
        double FF = 2.0;
        while (true) {
            double now = farm + X / FF;
            if (now > best) {
                break;
            } else {
                best = now;
            }
            farm += C / FF;
            FF += F;
        }
        printf("Case #%d: %.9lf\n", T, best);
    }
}