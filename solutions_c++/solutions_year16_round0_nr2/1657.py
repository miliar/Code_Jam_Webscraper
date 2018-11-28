#include <bits/stdc++.h>

using namespace std;

int main (void) {
    int T;
    cin >> T;
    for (int c = 1; c <= T; ++c) {
        printf ("Case #%d: ", c);
        string s;
        cin >> s;
        int n = s.size()-1;
        int ans = 0;
        for (int i = n; i >= 0; --i) {
            if (s[i] == '-') {
                if (s[0] == '+') {
                    for (int j = 0; j <= i; ++j) {
                        if (s[j] == '+') s[j] = '-';
                        else break;
                    }
                    ans++;
                }
                for (int j = 0; j <= i; ++j) {
                    if (s[j] == '+') s[j] = '-';
                    else s[j] = '+';
                }
                for (int j = 0; j <= i/2; ++j) {
                    swap (s[j], s[i-j]);
                }
                ans++;
            }
        }
        printf ("%d\n", ans);
    }
}
