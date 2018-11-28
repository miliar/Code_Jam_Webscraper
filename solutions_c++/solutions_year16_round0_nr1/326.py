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
        cout << "Case #" << T << ": ";
        int n;
        cin >> n;
        if (n) {
            int m = 0, k = 10;
            bool f[10] = {false};
            while (k) {
                m += n;
                int t = m;
                while (t) {
                    bool &p = f[t % 10];
                    t /= 10;
                    if (!p) {
                        p = true;
                        k -= 1;
                    }
                }
            }
            cout << m;
        } else {
            cout << "INSOMNIA";
        }
        cout << endl;
    }
    return 0;
}
