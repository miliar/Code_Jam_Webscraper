/* 
 * File:   main.cpp
 * Author: bacho
 *
 * Created on April 12, 2014, 12:40 AM
 */

#include <cstdlib>
#include <fstream>
#include <iostream>
#include <iomanip>

using namespace std;

ifstream ifs("a.in");
ofstream ofs("a.out");

int main() {
    int t, i = 1;
    ifs>>t;
    while (t--) {
        double c, f, x, cps = 2;
        ifs >> c >> f>>x;
        double a, b, d = 0, k = x / cps;
        bool q = true;
        do {
            a = c / cps;
            b = k;
            cps += f;
            k = x / cps;
            if (a + k < b) {
                d += a;
            } else {
                q = false;
                d += b;
            }
        } while (q);
//        cout << "Case #" << i << ": " << fixed << setprecision(7) << d << "\n";
        ofs << "Case #" << i++ << ": " << fixed << setprecision(7) << d << "\n";
    }
    return 0;
}

