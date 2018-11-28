#include <bits/stdc++.h>
using namespace std;

typedef unsigned long long ullong;

int main () {
    ios::sync_with_stdio(false);

    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        string s;
        cin >> s;

        char last = '+';
        int flips = 0;
        int i = (int)s.size()-1;
        while (i >= 0 && s[i] == '+') i--;

        for (i; i >= 0; i--) {
            if (s[i] != last) { flips++; last = s[i]; }
        }

        cout << "Case #" << t << ": " <<  flips << "\n";
    }
}
