/* Task solution for GCJ 2015
 * Tested with GCC
 * Build command line:
 *  g++ -std=gnu++11 -O2 -o <executable> <source.cpp>
 */

#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int TN;
    cin >> TN;
    for (int T = 1; T <= TN; T++) {
        string s;
        cin >> s;
        int k = 0;
        bool last = true;
        for (auto i = s.rbegin(), e = s.rend(); i != e; ++i) {
            bool cur = (*i == '+');
            if (cur != last) {
                last = cur;
                ++k;
            }
        }
        cout << "Case #" << T << ": " << k << endl;
    }
    return 0;
}
