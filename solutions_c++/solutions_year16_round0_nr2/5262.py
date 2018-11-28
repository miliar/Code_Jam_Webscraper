#include <iostream>

using namespace std;

#define long unsigned long long

string s;

// incl
void EZFlip(int l, int r) {
    for (int i = l; i <= r; ++i) {
        if (s[i] == '+') {
            s[i] = '-';
        } else {
            s[i] = '+';
        }
    }

    for (int i = 0; i < (r - l) / 2; ++i) {
        int x = l + i;
        int y = r - i;

        char tmp = s[x];
        s[x] = s[y];
        s[y] = tmp;
    }
}

bool EZOK() {
    for (char c : s) {
        if (c == '-') return false;
    }
    return true;
}


/*
5
-
-+
+-
+++
--+-
 */

int main() {
    int t;
    cin >> t;
    for (int test = 0; test < t; ++test) {
        cin >> s;
        cout << "Case #" << (test + 1) << ": ";

        int ans = 0;
        while (!EZOK()) {
            int idx;
            for (idx = 1; idx < s.length() && s[idx] == s[idx - 1]; ++idx) {
            }
            EZFlip(0, idx - 1);
            ans++;
        }

        cout << ans << endl;
    }
    return 0;
}