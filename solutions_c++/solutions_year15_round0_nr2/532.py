/* Task solution for GCJ 2015
 * Tested with GCC
 * Build command line:
 *  g++ -std=gnu++11 -O2 -o <executable> <source.cpp>
 */

#include <cstdio>
#include <iostream>

using namespace std;

const int max_d = 1000;
int p[max_d];

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int TN;
    cin >> TN;
    for (int T = 1; T <= TN; T++) {
        int d, l = 1, r = 1;
        cin >> d;
        for (int i = 0; i < d; ++i) {
            cin >> p[i];
            if (p[i] > r) {
                r = p[i];
            }
        }
        while (l < r) {
            int t = (l + r) / 2; // Round to left
            int m = 0;
            while (m < t) {
                int a = 0;
                for (int i = 0; i < d; ++i) {
                    a += (p[i] - 1) / (t - m);
                }
                if (a <= m) {
                    break;
                }
                m = a;
            }
            if (m < t) { // Success with (m) movements in (t) minutes
                r = t;
            } else { // Fail in (t) minutes
                l = t + 1;
            }
        }
        cout << "Case #" << T << ": " << r << endl;
    }
    return 0;
}
