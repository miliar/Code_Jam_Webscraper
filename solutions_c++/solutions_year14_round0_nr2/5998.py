/* 
 * File:   cookie_clicker_alpha.
 * Author: vivek
 *
 * Created on April 12, 2014, 7:21 AM
 */

#include <cstdlib>

#include <iostream>
#include <cstdio>


#include <vector>
#include <set>
#include <algorithm>
#include <map>

#include <cmath>
#include <iomanip>



using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        long double c, f, x;
        cin >> c >> f >> x;


        long double timeSpent = 0;
        long double currentRate = 2;

        while (true) {
            long double total_time_require = (x) / currentRate;

            long double time_require_to_reach_farm = c / currentRate;
            long double time_require_after_farm = x / (currentRate + f);

            long double total_time_with_farm = time_require_to_reach_farm + time_require_after_farm;

            if (total_time_with_farm >= total_time_require) {
                timeSpent += (x / currentRate);
                break;
            } else {
                timeSpent += time_require_to_reach_farm;
                currentRate += f;
            }

        }
        std::cout << std::fixed;
        std::cout << std::setprecision(7);
        cout << "Case #" << i << ": " << timeSpent << endl;
    }
    return 0;
}

