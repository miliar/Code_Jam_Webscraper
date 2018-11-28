/* Task solution for GCJ 2015
 * Tested with GCC
 * Build command line:
 *  g++ -std=gnu++11 -O2 -o <executable> <source.cpp>
 */

#include <cstdio>
#include <iostream>

using namespace std;

const int maxb = 1000;
long long m[maxb];

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int TN;
    cin >> TN;
    for (int T = 1; T <= TN; T++) {
        int b;
        long long n;
        cin >> b >> n;
        long long l = 0, r = 0;
        for (int i = 0; i < b; ++i) {
            cin >> m[i];
            //cout << m[i] << ' ';
            if (m[i] > r) {
                r = m[i];
            }
        }
        //cout << endl;
        r *= n;
        //Binary search our time
        long long t, k;
        while (l < r) {
            t = (l + r) / 2;
            //cout << l << ' ' << r << ": " << t << ' ';
            k = 0;
            for (int i = 0; i < b; ++i) {
                k += t / m[i] + 1;
            }
            //cout << k << '/' << n << ' ';
            if (k >= n) {
                r = t;
                //cout << '+';
            } else {
                l = t + 1;
                //cout << '-';
            }
            //cout << endl;
        }
        t = l;
        k = 0;
        for (int i = 0; i < b; ++i) {
            k += t / m[i] + 1;
        }
        //cout << t << ": " << k << '/' << n << endl;
        int i;
        for (i = b - 1; i >= 0; --i) {
            //cout << k << '/' << n << " : " << (i + 1) << endl;
            if (!(t % m[i])) {
                if (k == n) {
                    break;
                }
                --k;
            }
        }
        cout << "Case #" << T << ": " << (i + 1) << endl;
    }
    return 0;
}
