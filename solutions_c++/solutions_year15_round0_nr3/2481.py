#include <iostream>
#include <vector>
#include <string>
#include <map>
             //   1  i  j  k -1 -i -j -k
int mul[8][8] = {{0, 1, 2, 3, 4, 5, 6, 7},
                 {1, 4, 3, 6, 5, 0, 7, 2},
                 {2, 7, 4, 1, 6, 3, 0, 5},
                 {3, 2, 5, 4, 7, 6, 1, 0},
                 {4, 5, 6, 7, 0, 1, 2, 3},
                 {5, 0, 7, 2, 1, 4, 3, 6},
                 {6, 3, 0, 5, 2, 7, 4, 1},
                 {7, 6, 1, 0, 3, 2, 5, 4}};

using namespace std;

int main() {
    map<char, int> leg;
    leg['i'] = 1;
    leg['j'] = 2;
    leg['k'] = 3;
    int t, l, x;
    string s;
    cin >> t;
    for (int test = 0; test < t; ++test) {
        cin >> l >> x;
        cin >> s;

        int c = 0;
        int found = 0;
        for (int i = 0; i < l * x; ++i) {
            c = mul[c][leg[s[i % l]]];
//              cout << c << endl;
            if (c == found + 1 && found < 3) {
                found++;
                c = 0;
            }
        }

        bool ok = (found == 3 && c == 0);
        cout << "Case #" << test + 1 << ": " << ((ok) ? "YES" : "NO") << '\n';
    }
    return 0;
}

