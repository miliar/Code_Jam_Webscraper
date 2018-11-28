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
    cin >> skipws;
    int TN;
    cin >> TN;
    for (int T = 1; T <= TN; T++) {
        int n, k = 0, s = 0;
        char c;
        cin >> n;
        for (int i = 0; i <= n; ++i) {
            cin >> c;
            c -= '0';
            if (c > 0 && i > s) {
                k += i - s;
                s = i;
            }
            s += c;
        }
        cout << "Case #" << T << ": " << k << endl;
    }
    return 0;
}
