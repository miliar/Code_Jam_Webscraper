#include <iostream>
#include <bitset>
#include <string>
#include <cmath>
#include <cstdio>

using namespace std;

void solve_case(int case_num) {
    long double C;
    long double F;
    long double X;
    cin >> C >> F >> X;
    long double prev_time = X / 2.0L;
    long double farm_buying_time = 0.0L;
    long double cookies_per_second= 2.0L;

    while (true) {
        farm_buying_time = farm_buying_time + C/cookies_per_second;
        cookies_per_second += F;
        long double this_time = farm_buying_time + X/(cookies_per_second);
        if (this_time > prev_time) {
            printf("Case #%d: %.7Lf\n", case_num, prev_time);
            return;
        }
        prev_time = this_time;
    }
}

int main(int argc, char** argv) {
    int num_cases;
    cin >> num_cases;
    for (int i = 0; i < num_cases; ++i) {
        solve_case(i + 1);
    }
    return 0;
}

