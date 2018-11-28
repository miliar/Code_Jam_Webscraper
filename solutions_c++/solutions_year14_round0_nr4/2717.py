/* 
 * File:   main.cpp
 * Author: bacho
 *
 * Created on April 12, 2014, 5:50 PM
 */

#include <cstdlib>
#include <fstream>
#include <iostream>
#include <algorithm>

using namespace std;

ifstream ifs("d.in");
ofstream ofs("d.out");

int main() {
    int t, l = 1;
    ifs>>t;
    while (t--) {
        int n;
        ifs>>n;
        double a[n], b[n];
        for (int i = 0; i < n; i++)
            ifs >> a[i];
        for (int i = 0; i < n; i++)
            ifs >> b[i];
        sort(a, a + n);
        sort(b, b + n);

        int j = n - 1;
        int mor = 0;
        for (int i = j; i >= 0; i--) {
            bool c = true;
            for (; j >= 0 && c; j--) {
                if (a[i] > b[j]) {
                    mor++;
                    c = false;
                }
            }
        }
        int mor1 = 0;
        j = 0;
        for (int i = 0; i < n; i++) {
            bool c = true;
            for (; j < n && c; j++) {
                if (a[i] < b[j]) {
                    c = false;
                } else mor1++;
            }
        }
        ofs << "Case #" << l++ << ": " << mor << " " << mor1 << "\n";
    }
    return 0;
}

