/* Task solution for GCJ 2015
 * Tested with GCC
 * Build command line:
 *  g++ -std=gnu++11 -O2 -o <executable> <source.cpp>
 */

#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
    int primes[5] = {2};
    for (int i = 1, p = 3; i < sizeof(primes) / sizeof(*primes); p += 2) {
        for (int d : primes) {
            if (d * d > p) {
                primes[i++] = p;
                break;
            }
            if (!(p % d)) {
                break;
            }
        }
    }
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int TN;
    cin >> TN;
    for (int T = 1; T <= TN; T++) {
        cout << "Case #" << T << ":" << endl;
        int n, j;
        cin >> n >> j;
        bool s[n];
        s[0] = s[n - 1] = true;
        for (int i = 1; i < n - 1; ++i) {
            s[i] = false;
        }
        for (;;) {
            int divs[11];
            int r;
            for (int b = 2; b <= 10; ++b) {
                for (int p : primes) {
                    r = 0;
                    for (bool i : s) {
                        r *= b;
                        if (i) {
                            ++r;
                        }
                        r %= p;
                    }
                    if (!r) {
                        divs[b] = p;
                        break;
                    }
                }
                if (r) {
                    break;
                }
            }
            if (!r) {
                for (bool i : s) {
                    cout << (i ? '1' : '0');
                }
                for (int b = 2; b <= 10; ++b) {
                    cout << ' ' << divs[b];
                }
                cout << endl;
                if (!--j) {
                    break;
                }
            }
            int i = n - 2;
            while (i && s[i]) {
                s[i] = false;
                --i;
            }
            if (!i) {
                cout << "FAIL: " << j << endl;
                break;
            }
            s[i] = true;
        }
    }
    return 0;
}
