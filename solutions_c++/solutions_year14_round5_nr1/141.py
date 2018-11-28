#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
typedef long long Int;

int n;
Int xs[2000000], s[2000000];

Int f(Int a, Int b, Int c) {
    return a + b + c - max(a, max(b, c));
}

double solve() {
    rep (i, n) s[i+1] = s[i] + xs[i];
    int j = 0;
    Int ans = 0;
    rep (i, n) {
        while (j < i) {
            if (s[i+1] - s[j+1] < s[j+1]) break;
            j++;
        }
        ans = max(ans, f(s[j], s[i+1]-s[j], s[n]-s[i+1]));
        ans = max(ans, f(s[j+1], s[i+1]-s[j+1], s[n]-s[i+1]));
//        rep (j, i+1) {
//            ans = max(ans, f(s[j], s[i+1]-s[j], s[n]-s[i+1]));
//        }
    }
    return (double)ans / s[n];
}

int main() {
    int T;
    cin >> T;
    rep (_q, T) {
        Int p, q, r, s;
        cin >> n >> p >> q >> r >> s;
        rep (i, n) xs[i] = (i * p + q) % r + s;
        double ans = solve();
        printf("Case #%d: %.12f\n", _q+1, ans);
    }
    return 0;
}
