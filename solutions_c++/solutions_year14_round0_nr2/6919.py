#include <stdio.h>
#include <set>
#include <vector>
#include <iostream>
using namespace std;

int main() {
    int test;
    cin >> test;
    for (int cas = 1; cas <= test; ++cas) {
        double C, F, X;
        cin >> C >> F >> X;
        double rate = 2.0;
        double now = 0.0;
        while (true) {
            double time_buy_farm = C / rate;
            if (time_buy_farm + X / (rate + F) < X / rate) {
                rate += F;
                now += time_buy_farm;
            } else {
                now += X / rate;
                break;
            }
        }
        printf("Case #%d: %.7f\n", cas, now);
    }
}
