#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define REP(i, n) for (int i = 0; i < (int)(n); ++i)
typedef long long LL;
typedef pair<int, int> PII;

int tt;
int n, r, p, s;
string rr[13], pp[13], ss[13];

void check(string &ans, string &x, int r, int p, int s) {
    for (char c : x) {
        if (c == 'R') --r;
        else if (c == 'P') --p;
        else --s;
    }
    if (r == 0 && p == 0 && s == 0) {
        if (ans.empty() || ans > x) {
            ans = x;
        }
    }
}

int main() {
    rr[0] = "R";
    pp[0] = "P";
    ss[0] = "S";
    //PR PS RS -> P S R
    for (int i = 1; i <= 12; ++i) {
        if (rr[i - 1] < ss[i - 1]) {
            rr[i] = rr[i - 1] + ss[i - 1];
        } else {
            rr[i] = ss[i - 1] + rr[i - 1];
        }
        if (rr[i - 1] < pp[i - 1]) {
            pp[i] = rr[i - 1] + pp[i - 1];
        } else {
            pp[i] = pp[i - 1] + rr[i - 1];
        }
        if (pp[i - 1] < ss[i - 1]) {
            ss[i] = pp[i - 1] + ss[i - 1];
        } else {
            ss[i] = ss[i - 1] + pp[i - 1];
        }
    }
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &tt);
    for (int test = 1; test <= tt; ++test) {
        printf("Case #%d: ", test);
        scanf("%d%d%d%d", &n, &r, &p, &s);
        string ans = "";
        check(ans, rr[n], r, p, s);
        check(ans, pp[n], r, p, s);
        check(ans, ss[n], r, p, s);
        if (ans.empty()) {
            printf("IMPOSSIBLE\n");
        } else {
            printf("%s\n", ans.c_str());
        }
    }
    return 0;
}
