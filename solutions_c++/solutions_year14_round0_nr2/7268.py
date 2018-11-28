//
//  main.cpp
//  CookieClicker
//
//  Created by Ciupin Iaroslav on 12/04/14.
//  Copyright (c) 2014 Ciupin Iaroslav. All rights reserved.
//

#include <iostream>
#include <float.h>
using namespace std;

int main(int argc, const char * argv[])
{
    int T = 0;
    cin >> T;
    for (int t = 0; t < T; t++) {
        double C = 0.0, F = 0.0, X = 0.0;
        cin >> C >> F >> X;
        double prev_time = DBL_MAX;
        double current_time = DBL_MAX;
        double base_rate = 2.0;
        double prev_farms_time = 0.0;
        double current_farm_time = 0.0;
        double rest_time = 0.0;
        double rate = base_rate;
        do {
            prev_time = current_time;
            rest_time = X / rate;
            current_time = prev_farms_time + current_farm_time + rest_time;
            prev_farms_time += current_farm_time;
            current_farm_time = C / rate;
            rate += F;
        } while (prev_time > current_time);
        printf("Case #%d: %.7f\n", t + 1, prev_time);
    }
    return 0;
}

