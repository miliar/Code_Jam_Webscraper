#include <cstdio>
#include <algorithm>
#include <iostream>
#include <set>
using namespace std;

double C, F, X;

bool better_buy_farm(double got, double rate) {
    if (got >= X)
        return false;
    // with a new farm
    double time_with_farm = 0;
    time_with_farm = (C - got) / rate;
    time_with_farm += X / (rate + F);
    // without a new farm
    double time_without_farm = 0;
    time_without_farm = (X - got) / rate;
    return time_with_farm < time_without_farm;
}

int main(void) {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int _case;
    scanf("%d", &_case);
    for (int i = 1; i <= _case; i++) {
        scanf("%lf%lf%lf", &C, &F, &X);
        double time_cost = 0, rate = 2.0, got = 0;
        while (better_buy_farm(got, rate)) {
            time_cost += (C - got) / rate;
            rate += F;
            got = 0;
        }
        time_cost += (X - got) / rate;
        printf("Case #%d: %.7lf\n", i, time_cost);
    }
    return 0;
}
