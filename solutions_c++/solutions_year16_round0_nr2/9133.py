#include <bits/stdc++.h>
using namespace std;

int t;

int main() {

    freopen("B-large.in", "r", stdin);
    freopen("out", "w", stdout);

    cin >> t;

    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        string s; cin >> s;
        reverse(s.begin(), s.end());
        int result = 0;
        int dir = 0;
        for (int j = 0; j < s.length(); j++) {
            if ((s[j] == '-' && dir == 0) || s[j] == '+' && dir == 1) {
                dir ^= 1;
                result++;
            }
        }
        cout << result << "\n";
    }

    return 0;
}
