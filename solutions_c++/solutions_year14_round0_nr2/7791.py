#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int T, cases;
    scanf("%d", &T);
    for (int cases = 1; cases <= T; cases++) {
        double C, F, X;
        cin >> C >> F >> X;
        double best = X / 2;
        double rate = 2;
        double time = 0;
        for (int farm = 0; ; farm++) {
            if (X / rate > (C/rate) + (X/(rate+F))) {
                time += C/rate;
                rate += F;
            } else {
                time += X/rate;
                break;
            }
        }
        printf("Case #%d: %.7lf\n", cases, time);
    }
}
