/* Task solution for GCJ 2015
 * Tested with GCC
 * Build command line:
 *  g++ -std=gnu++11 -O2 -o <executable> <source.cpp>
 */

#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

int rn, sn, pn;
string ans;

void chk(const string &str)
{
    if (str < ans) {
        int r = rn, s = sn, p = pn;
        for (char c : str) {
            if (c == 'R') {
                --r;
            } else if (c == 'S') {
                --s;
            } else { // c == 'P'
                --p;
            }
        }
        if (!(r || s || p)) {
            ans = str;
        }
    }
}

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int TN;
    cin >> TN;
    for (int T = 1; T <= TN; T++) {
        int n;
        cin >> n >> rn >> pn >> sn;
        string r = "R";
        string s = "S";
        string p = "P";
        while (n > 0) {
            --n;
            string tr = r < s ? r + s : s + r;
            s = s < p ? s + p : p + s;
            p = p < r ? p + r : r + p;
            r = tr;
        }
        ans = "z";
        chk(r);
        chk(s);
        chk(p);
        if (ans == "z") {
            ans = "IMPOSSIBLE";
        }
        cout << "Case #" << T << ": " << ans << endl;
    }
    return 0;
}
