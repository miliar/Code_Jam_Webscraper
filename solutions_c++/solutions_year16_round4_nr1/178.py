#include <bits/stdc++.h>
using namespace std;
const int MAXN = 15;
struct state {
    int p, r, s;
    string str;
    state (int _p=0, int _r=0, int _s=0, string _str=""): p(_p), r(_r), s(_s), str(_str) {}
    state operator+ (const state& b) {
        if (str < b.str)
            return state(p+b.p, r+b.r, s+b.s, str+b.str);
        else
            return state(p+b.p, r+b.r, s+b.s, b.str+str);
        
    }
};
bool v[MAXN][3];
state req[MAXN][3];
int TC;
state dp(int n, int m) {
    if (v[n][m]) return req[n][m];
    v[n][m] = 1;
    return req[n][m] = dp(n-1, m) + dp(n-1, (m+1)%3);
}
int main () {
    req[0][0] = state(1, 0, 0, "P");
    req[0][1] = state(0, 1, 0, "R");
    req[0][2] = state(0, 0, 1, "S");
    v[0][0] = v[0][1] = v[0][2] = 1;

    scanf("%d", &TC);
    for (int T = 1, N, R, P, S; T <= TC; ++T) {
        scanf("%d%d%d%d", &N, &R, &P, &S);
        string ans = ""; bool can = 0;
        for (int i = 0; i < 3; ++i) {
            state c = dp(N, i);
            if (c.r == R && c.p == P && c.s == S) {
                if (!can) {
                    can = 1;
                    ans = c.str;
                }
                else ans = min(c.str, ans);
            }
        }
        if (!can) printf("Case #%d: IMPOSSIBLE\n", T);
        else printf("Case #%d: %s\n", T, ans.c_str());
    }
}