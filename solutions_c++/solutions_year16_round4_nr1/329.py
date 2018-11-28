#include <bits/stdc++.h>
using namespace std;

int n, a, b, c, C[5];
char s[5] = "RPS";

string dfs (int l, int r, int now) {
    if (l == r) { C[now]++; string r = ""; r += s[now]; return r; }
    int m = l + r >>1;
    string s1 = dfs (l, m, now);
    string s2 = dfs (m + 1, r, (now + 2) % 3);
    if (s1 < s2) return s1 + s2;
    return s2 + s1;
}

int main () {
    freopen ("in.txt", "r", stdin);
    freopen ("out.txt", "w", stdout);
    int T, cas = 1;
    cin >> T;
    while (T--) {
        cin >> n >> a >> b >> c;
        string res = "";
        for (int i = 0; i< 3; i++) {
            C[0] = C[1] = C[2] = 0;
            string tmp = dfs (1, (1 << n), i);
            if (C[0] == a && C[1] == b && C[2] == c) {
                if (res == "") res = tmp;
                else res = min (res, tmp);
            }
        }
        printf ("Case #%d: ", cas++);
        if (res == "") cout << "IMPOSSIBLE\n";
        else cout << res << endl;
    }
}
