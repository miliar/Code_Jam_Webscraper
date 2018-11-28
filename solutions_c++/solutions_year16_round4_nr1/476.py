#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
char valid(string x) {
    if (x == "") return '0';
    if (x.length() == 1) {
        return x[0];
    } else {
        cout << x << endl;
        char a = valid(x.substr(0, x.length() / 2)),
             b = valid(x.substr(x.length() / 2, x.length()));
        if (a == '0' || b == '0') return '0';
        if (a == b) return '0';
        if (a == 'P' && b == 'R') return 'P';
        if (a == 'P' && b == 'S') return 'S';
        if (a == 'S' && b == 'R') return 'R';
        if (a == 'R' && b == 'S') return 'R';
        if (a == 'R' && b == 'P') return 'P';
        if (a == 'S' && b == 'P') return 'S';
    }
}
string solve(int n, int p, int r, int s) {
    if (r < 0 || p < 0 || s < 0) return "";
    if (r + p + s != (1 << n)) return "";
    if (n == 1) {
        if (r >= 2 || p >= 2 || s >= 2)
            return "";
        else {
            string ans = "";
            if (p) ans = ans + "P";
            if (r) ans = ans + "R";
            if (s) ans = ans + "S";
            assert(ans.length() == 2);
            return ans;
        }
    } else {
        int a, b, c, tot;
        tot = r + p + s;
        tot /= 2;
        c = tot - p;
        a = tot - s;
        b = tot - r;
        string tmp = solve(n - 1, a, b, c), ans = tmp + tmp;
        for (int i = 0; i < tmp.length(); i++) {
            if (tmp[i] == 'P') ans[i * 2] = 'P', ans[i * 2 + 1] = 'R';
            if (tmp[i] == 'R') ans[i * 2] = 'P', ans[i * 2 + 1] = 'S';
            if (tmp[i] == 'S') ans[i * 2] = 'R', ans[i * 2 + 1] = 'S';
        }
        return ans;
    }
}
int main() {
    int cas;
    scanf("%d", &cas);
    for (int _ = 1; _ <= cas; _++) {
        int n, r, p, s;
        scanf("%d%d%d%d", &n, &r, &p, &s);
        printf("Case #%d: ", _);
        string ans = solve(n, p, r, s);
        if (ans != "") {
            printf("%s\n", ans.c_str());
        } else {
            printf("IMPOSSIBLE\n");
        }
    }
}
