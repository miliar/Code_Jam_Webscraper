#include <stdio.h>
#include <string.h>
#include <iostream>
#include <string>
#include <set>
#include <utility>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int m, n;
string ss[2048];
int of[16], a[16];

int solve(int b) {
    memset(a, 0, sizeof(a));
    rep (i, m) {
        of[i] = b % n;
        b /= n;
        a[of[i]]++;
    }
    rep (i, n) if (a[i] == 0) return -1;
    int ans = 0;
    rep (k, n) {
        set<string> p;
        rep (i, m) if (of[i] == k) {
            rep (j, ss[i].size()+1) {
                p.insert(ss[i].substr(0, j));
            }
        }
        ans += p.size();
    }
    return ans;
}

pair<int, int> solve() {
    int mm = 1;
    rep (_, m) mm *= n;
    int ans = 0, ansc = 0;
    rep (b, mm) {
        int r = solve(b);
        if (r >= 0) {
            if (ans < r) {
                ans = r;
                ansc = 0;
            }
            if (ans == r) ansc++;
        }
    }
    return make_pair(ans, ansc);
}

int main() {
    int T;
    cin >> T;
    for (int _q = 0; _q < T; _q++) {
        cin >> m >> n;
        rep (i, m) cin >> ss[i];
        pair<int, int> ans = solve();
        printf("Case #%d: %d %d\n", _q+1, ans.first, ans.second);
    }
    return 0;
}
