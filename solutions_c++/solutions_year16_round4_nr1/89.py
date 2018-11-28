#include <bits/stdc++.h>
using namespace std;

string dp[13][3];

string f(int x, int y) {
    if (dp[x][y] != "") {
        return dp[x][y];
    }
    string &res = dp[x][y];
    if (x == 0) {
        if (y == 1) return res = "R";
        else if (y == 2) return res = "S";
        else return res = "P";
    } else {
        string s1 = f(x - 1, y);
        string s2 = f(x - 1, (y + 1) % 3);
        return res = min(s1 + s2, s2 + s1);
    }
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        int n, r, p, s;
        scanf("%d%d%d%d", &n, &r, &p, &s);
        string res = "";
        for (int i = 0; i < 3; i++) {
            string tmp = f(n, i);
            int rs = 0, ps = 0, ss = 0;
            for (auto &c : tmp) {
                if (c == 'R') rs++;
                else if (c == 'S') ss++;
                else ps++;
            }
            if (rs == r && ps == p && ss == s) {
                if (res == "" || res > tmp) {
                    res = tmp;
                }
            }
        }
        printf("Case #%d: ", cas);
        fprintf(stderr, "Case #%d: ", cas);
        if (res == "") {
            printf("IMPOSSIBLE\n");
            fprintf(stderr, "IMPOSSIBLE\n");
        } else {
            printf("%s\n", res.c_str());
            fprintf(stderr, "%s\n", res.c_str());
        }
    }
    return 0;
}