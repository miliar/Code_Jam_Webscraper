#include <iostream>
#include <cstdio>

using namespace std;

void solve() {
    double C, F, X;
    cin >> C >> F >> X;
    double prev = 0;
    double prev_time_needed = X/2;
    // linearly search #farms to buy
    for (int i = 1; ; ++i) {
        double rate = (i-1) * F + 2;
        double new_rate = i * F + 2;
        double time_needed = prev + C/rate + X/new_rate;
//        printf("%d can be bought after %.7lf time units\n", i, prev + C/rate);
//        printf("%.7lf\n", time_needed);
        if (prev_time_needed < time_needed + 1e-9) {
            printf("%.7lf\n", prev_time_needed);
            return;
        }
        prev_time_needed = time_needed;
        prev = prev + C / rate;
    }
}

int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        printf("Case #%d: ", i);
        solve();
    }
}
