#include <bits/stdc++.h>
using namespace std;

void flip(string &s, int l, int r) {
    if (l > r) return ;
    for (int i = 0; i <= r - l; ++ i) {
        if (s[r - i] == '-') s[l + i] = '+';
        else s[l + i] = '-';
    }
}

int main(void) {
    int T, cas = 1;
    cin >> T;
    while (T -- > 0) {
        string s;
        cin >> s;
        int l = 0, r = s.length() - 1;
        int ans = 0;
        for (int i = 1; i <= r; ++ i) {
            if (s[i] != s[i - 1]) ++ ans;
        }
        if (s[r] == '-') ++ ans;
        cout << "Case #" << (cas ++) << ": " << ans << endl;
    }

    return 0;
}
