#include <bits/stdc++.h>

using namespace std;

const int MAXN = 100 + 10;

int n, r, p, s;

string gen(int n, char c) {
    if (n <= 0) return "";
    if (n == 1) {
        string res = "h";
        res[0] = c;
        return res;
    }

    char x = c, y;
    if (c == 'P') y = 'R';
    else if (c == 'R') y = 'S';
    else y = 'P';

    string L = gen(n - 1, x), R = gen(n - 1, y);
    if (L > R) swap(L, R);
    //cout << n << " " << c << " " << L << " " << R << endl;
    return L + R;
}

int cnt(string s, char c) {
    int res = 0;
    for(int i = 0; i < s.length(); i++) res += (s[i] == c);
    return res;
}

bool check(string st, int r, int p, int s) {
    return ((cnt(st, 'R') == r) && (cnt(st, 'P') == p) && (cnt(st, 'S') == s));
}

void solve() {
    cin >> n >> r >> p >> s;

    string res = "";
    string a = gen(n + 1, 'R'), b = gen(n + 1, 'P'), c = gen(n + 1, 'S');
    if ((check(a, r, p, s)) && ( (res == "") || (a < res)  )) res = a;
    if ((check(b, r, p, s)) && ( (res == "") || (b < res)  )) res = b;
    if ((check(c, r, p, s)) && ( (res == "") || (c < res)  )) res = c;

    if (res == "") res = "IMPOSSIBLE";
    cout << res << endl;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);

    int ntests;
    cin >> ntests;
    for(int tc = 1; tc <= ntests; tc++) {
        cout << "Case #" << tc << ": ";
        solve();
    }
}
