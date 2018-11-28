#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>

int main() {
    int T;
    std::cin >> T;
    int CA = 1;
    while(T--) {
        double C, F, X;
        std::cin >> C >> F >> X;

        double best = X/2;

        double state_t = 0;
        double state_c = 2;
        for(int i = 0; i < 200000000; i ++) {
            best = std::min(best, state_t + (X/state_c));
            double next = C/state_c;
            state_t += next;
            state_c += F;
        }

        std::printf("Case #%i: %.8f\n", CA++, best);
    }
    return 0;
}
