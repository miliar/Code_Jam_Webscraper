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
        int x['Z' - 'A' + 1] = {0};
        string s;
        cin >> s;
        string t(s.size(), '_');
        for (auto c: s) {
            ++x[c - 'A'];
        }
        char c = 'Z';
        auto l = t.begin();
        auto r = t.rbegin();
        for (auto i = s.rbegin(), e = s.rend(); i != e; ++i) {
            while (x[c - 'A'] == 0) {
                --c;
            }
            --x[*i - 'A'];
            if (c == *i) {
                *l = *i;
                ++l;
            } else {
                *r = *i;
                ++r;
            }
        }
        cout << "Case #" << T << ": " << t << endl;
    }
    return 0;
}
