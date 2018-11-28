#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

char a[1000];
int n, r, p, s;

string solve(char ch, int l) {
    if (l == 1) {
        string t = "";
        t = t + ch;
        return t;
    }
    char z;
    if (ch == 'R') z = 'S';
    if (ch == 'P') z = 'R';
    if (ch == 'S') z = 'P';
    string s1 = solve(ch, l >> 1), s2 = solve(z, l >> 1);
    if (s1 + s2 > s2 + s1) return s2 + s1;
    return s1 + s2;
}

string getmin(string a, string b) {
    int tr = 0, tp = 0, ts = 0;
    for (int i = 0; i < 1 << n; ++i)
        if (b[i] == 'R') ++tr;
        else if (b[i] == 'P') ++ tp;
        else if (b[i] == 'S') ++ ts;
    if (tr != r || tp != p || ts != s) return a;
    if (a == "" || a > b) return b;
    return a;
}

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int T;
    scanf("%d", &T);
    while (T--) {
        scanf("%d%d%d%d", &n, &r, &p, &s);
        string ans = "";
        ans = getmin(ans, solve('R', 1 << n));
        ans = getmin(ans, solve('P', 1 << n));
        ans = getmin(ans, solve('S', 1 << n));
        static int ca = 0;
        if (ans == "") ans = "IMPOSSIBLE";
        printf("Case #%d: %s\n", ++ca, ans.c_str());
    }
    return 0;
}
