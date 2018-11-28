/* Task solution for GCJ 2015
 * Tested with GCC
 * Build command line:
 *  g++ -std=gnu++11 -O2 -o <executable> <source.cpp>
 */

#include <cstdio>
#include <iostream>

using namespace std;

const int maxn = 1000;
int v[maxn];

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int TN;
    cin >> TN;
    for (int T = 1; T <= TN; T++) {
        int n;
        cin >> n;
        for (int i = 0; i < n; ++i) {
            cin >> v[i];
        }
        int a = 0, b = 0;
        for (int i = 1; i < n; ++i) {
            int d = v[i - 1] - v[i];
            if (d > 0) {
                a += d;
                if (d > b) {
                    b = d;
                }
            }
        }
        int c = 0;
        for (int i = 0; i < n - 1; ++i) {
            c += min(b, v[i]);
        }
        cout << "Case #" << T << ": " << a << ' ' << c << endl;
    }
    return 0;
}
