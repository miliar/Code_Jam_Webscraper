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
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int TN;
    cin >> TN;
    for (int T = 1; T <= TN; T++) {
        cout << "Case #" << T << ":";
        long long k, c, s;
        cin >> k >> c >> s;
        if ((k + c - 1) / c > s) {
            cout << " IMPOSSIBLE";
        } else {
            long long i = 0;
            while (i < k) {
                long long p = 0;
                for (int j = 0; j < c; ++j) {
                    p *= k;
                    if (i < k) {
                        p += i;
                        ++i;
                    }
                }
                cout << ' ' << (p + 1);
            }
        }
        cout << endl;
    }
    return 0;
}
