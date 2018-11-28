/* Task solution for GCJ 2015
 * Tested with GCC
 * Build command line:
 *  g++ -std=gnu++11 -O2 -o <executable> <source.cpp>
 */

#include <cstdio>
#include <iostream>

using namespace std;

const int maxcount = 100;

int in[maxcount + 1];

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int TN;
    cin >> TN;
    for (int T = 1; T <= TN; T++) {
        int c, d, v;
        cin >> c >> d >> v;
        for (int i = 0; i < d; ++i) {
            cin >> in[i];
        }
        in[d] = v + 1;
        int i = 0, s = 0, ans = 0;
        while (s < v) {
            if (s + 1 >= in[i]) {
                s += c * in[i++];
            } else {
                s += c * (s + 1);
                ++ans;
            }
        }
        cout << "Case #" << T << ": " << ans << endl;
    }
    return 0;
}
