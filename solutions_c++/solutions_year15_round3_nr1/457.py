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
        int r, c, w;
        cin >> r >> c >> w;
        int ans = (r - 1) * (c / w);
        ans += (c - 1) / w + w;
        cout << "Case #" << T << ": " << ans << endl;
    }
    return 0;
}
