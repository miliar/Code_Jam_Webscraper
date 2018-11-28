#include <iostream>
#include <set>
#include <vector>

using namespace std;


#define TASK "test"

const int N = 1000000;
double build[N];

void precalc(double C, double F) {
    double V = 2;
    build[0] = 0;
    for (int i = 1; i < N; i++) {
        build[i] = build[i - 1] + C / V;
        V += F;
    }
}

double get_time(int K, double F, double X) {
    return build[K] + X / (2 + F * K);
}

int main() {
    freopen(TASK ".in", "r", stdin);
    freopen(TASK ".out", "w", stdout);
    int tests;
    cin >> tests;
    for (int t = 1; t <= tests; t++) {
        printf("Case #%d: ", t);
        double C, F, X;
        cin >> C >> F >> X;
        precalc(C, F);
        double prev = get_time(0, F, X);
        double cur = prev;
        int k = 1;
        do {
            prev = cur;
            cur = get_time(k++, F, X);
        } while (cur < prev);
        printf("%.7lf\n", prev);
    }
    return 0;
}