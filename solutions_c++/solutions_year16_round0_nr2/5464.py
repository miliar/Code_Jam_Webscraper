#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    string s;
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    cin >> t;
    for (int c = 1; c <= t; c++) {
        int r = 0;
        cin >> s;
        char l = s[0];
        for (char si : s) {
            if (si != l) {
                r++;
                l = si;
            }
        }
        if (l == '-')
            r++;
        cout << "Case #" << c << ": " << r << '\n';
    }
    cout.flush();
}
