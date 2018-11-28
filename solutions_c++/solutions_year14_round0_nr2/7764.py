/* 
 * File:   main.cpp
 * Author: Shiva Prasad Goud Bandari <bshivagoud@gmaill.com>
 *
 * Created on 12 April, 2014, 4:23 PM
 */

#include <iostream>
#include <cstdio>

using namespace std;

int main() {
    unsigned int T;
    double C, F, X, cookies = 0, time_elapsed = 0, time_required, time_required_with_buy,Freq=2;

    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> C >> F >> X;

        time_elapsed = 0;
        Freq=2;

        while (X > C) {
            time_elapsed += C / Freq;
            X -= C;

            //not buy
            time_required = X / Freq;

            //choose to buy
            time_required_with_buy = (X + C) / (Freq + F);

            if (time_required_with_buy < time_required) {
                Freq += F;
                X += C;
            }
        }
        time_elapsed += X/Freq;
        
        cout << "Case #" << t << ": ";
        printf("%.7f\n",time_elapsed);

    }

    return 0;
}

