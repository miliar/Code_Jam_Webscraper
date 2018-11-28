#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <map>
#include <queue>
#include <vector>
using namespace std;

int tests, n, R, P, S;
int r[20][3], p[20][3], s[20][3];

void precalc() {
    // rs
    r[1][0] = 1; s[1][0] = 1; p[1][0] = 0;
    // rp
    r[1][1] = 1; s[1][1] = 0; p[1][1] = 1;
    // sp
    r[1][2] = 0; s[1][2] = 1; p[1][2] = 1;
    for (int i = 2; i <= 12; ++ i) {
        for (int j = 0; j < 3; ++ j) {
            r[i][j] = r[i - 1][j] + p[i - 1][j];
            p[i][j] = s[i - 1][j] + p[i - 1][j];
            s[i][j] = s[i - 1][j] + r[i - 1][j];
        }
    }
}

void reorder(int n, string &s) {
    vector<string> a, b;
    a.clear(); b.clear();
    int len = s.length();
    for (int i = 0; i < len / 2; ++ i)
        a.push_back(s.substr(i + i, 2));
    for (int k = 1; k < n; ++ k) {
        b.clear();
        for (int i = 0; i < a.size(); i += 2) {
            if (a[i] > a[i + 1]) swap(a[i], a[i + 1]);
            b.push_back(a[i] + a[i + 1]);
        }
        swap(a, b);
    }
    s = a[0];
}

void generate(int n, string s) {
    string t = "";
    for (int k = 1; k < n; ++ k) {
        t = "";
        for (int i = 0; i < s.length(); ++ i) {
            if (s[i] == 'S') t += "PS";
            if (s[i] == 'R') t += "RS";
            if (s[i] == 'P') t += "PR";
        }
        s = t;
    }
    reorder(n, s);
    cout << s << endl;
}

int main() {
    precalc();
    cin >> tests;
    for (int cases = 1; cases <= tests; ++ cases) {
        cin >> n >> R >> P >> S;
        bool mark = false;
        for (int i = 0; i < 3; ++ i) {
            if (R == r[n][i] && P == p[n][i] && S == s[n][i]) {
                printf("Case #%d: ", cases);
                if (i == 0) generate(n, "RS");
                if (i == 1) generate(n, "PR");
                if (i == 2) generate(n, "PS");
                mark = true;
                break;
            }
        }
        if (!mark) {
            printf("Case #%d: IMPOSSIBLE\n", cases);
        }
    }
    return 0;
}
