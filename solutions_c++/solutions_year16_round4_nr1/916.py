#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

string solve_test(int n, int r, int p, int s) {
    int r0 = r, p0 = p, s0 = s;
    int x, y, z;
    vector < string > s_r(r, "R"), s_p(p, "P"), s_s(s, "S"), t_r, t_p, t_s;
    while (r > 0 && p > 0 && s > 0) {
        if ((p + s - r) % 2 == 1) {
            return "IMPOSSIBLE";
        }
        z = (p + s - r) / 2;
        y = s - z;
        x = p - z;
        if (x < 0 || y < 0 || z < 0) {
            return "IMPOSSIBLE";
        }
        t_r.clear();
        t_p.clear();
        t_s.clear();
        for (int i = 0; i < x; ++i) {
            t_p.push_back(min(s_p.back(), s_r.back()) + max(s_p.back(), s_r.back()) );
            s_p.pop_back();
            s_r.pop_back();
        }
        for (int i = 0; i < y; ++i) {
            t_r.push_back(min(s_s.back(), s_r.back()) + max(s_s.back(), s_r.back()) );
            s_s.pop_back();
            s_r.pop_back();
        }
        for (int i = 0; i < z; ++i) {
            t_s.push_back(min(s_p.back(), s_s.back()) + max(s_p.back(), s_s.back()) );
            s_s.pop_back();
            s_p.pop_back();
        }
        sort(t_r.begin(), t_r.end());
        sort(t_s.begin(), t_s.end());
        sort(t_p.begin(), t_p.end());
        reverse(t_r.begin(), t_r.end());
        reverse(t_s.begin(), t_s.end());
        reverse(t_p.begin(), t_p.end());
        s_s = t_s;
        s_r = t_r;
        s_p = t_p;
        p = x;
        r = y;
        s = z;
    }
    if (r < 0 || p < 0 || s < 0 || r > 1 || p > 1 || s > 1) {
        return "IMPOSSIBLE";
    }
    string res = "";
    if (s_r.size() > 0) {
        if (res > s_r[0]) {
            res = s_r[0] + res;
        } else {
            res = res + s_r[0];
        }
    }
    if (s_p.size() > 0) {
        if (res > s_p[0]) {
            res = s_p[0] + res;
        } else {
            res = res + s_p[0];
        }
    }
    if (s_s.size() > 0) {
        if (res > s_s[0]) {
            res = s_s[0] + res;
        } else {
            res = res + s_s[0];
        };
    }
    return res;
}

void solve() {
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        int r, p, s, n;
        cin >> n >> r >> p >> s;
        cout << "Case #" << i + 1 << ": " << solve_test(n, r, p, s) << endl;
    }
}

int main() {
#ifdef ALEXEY
    freopen("input", "r", stdin);
    freopen("output", "w", stdout);
#endif
    solve();
    return 0;
}