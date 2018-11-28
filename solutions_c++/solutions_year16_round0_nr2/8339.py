#include <bits/stdc++.h>

using namespace std;
typedef long long Long;


int main() {
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    string s;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cout << "Case #" << t << ": " ;
        cin >> s;
        int n = s.length(), d = 0;
        for (int i = 1; i < n; ++i) {
            if (s[i] != s[i - 1]) {
                ++d;
            }
        }
        --n;
        if (s[0] == '+') {
            if (s[n] == '+') {
                d = d;
            } else {
                d = d + 1;
            }
        } else {
            if (s[n] == '-') {
                d = d + 1;
            } else {
                d = d;
            }
        }
        cout << d;
        cout << "\n";
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
/****

 1                           =   0
 101                         =   2
 10101                       =   4
 1010101                     =   6

 10                         =   2
 1010                       =   4
 101010                     =   6


 0                           =   1
 010                         =   3
 01010                       =   5
 0101010                     =   7

 01                          =   1
 0101                        =   3
 010101                      =   5


 * */
