/**
 * @file cookie_clicker_alpha.cpp
 *
 * @breif Solving the 'Cookie Click Alpha' problem:
 * https://code.google.com/codejam/contest/2974486/dashboard#s=p1
 */
#include <iostream>

#include <stdio.h>

using namespace std;

int main()
{
    int test_cases;  // number of test cases
    cin >> test_cases;
    for (int t = 1; t <= test_cases; ++t) {
        double C, F, X;
        cin >> C >> F >> X;
        double cookies = 0.0;     // current cookies
        double production = 2.0;  // current cookie production
        double total_time = 0.0;
        // wait until can by a farm
        if (X <= C) {
            total_time = X / production;
        } else {
            total_time += C / production;
            cookies += C;
            double F_divides_C = C / F;
            while ((X-cookies)/production > F_divides_C) {  // worth to buy a farm
                production += F;  // buy an farm
                total_time += C / production;  // ready to buy the next farm
            }
            total_time += (X-cookies) / production;
        }
        printf("Case #%d: %.07lf\n", t, total_time);
    }
}
