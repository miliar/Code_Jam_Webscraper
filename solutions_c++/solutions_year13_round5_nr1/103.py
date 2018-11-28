#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

typedef long long LL;
const LL MOD = 1000002013;

LL sum(const vector<LL>& s, int i, int j) {
    LL res = 0;
    for (int k = i; k < j; ++k) res += s[k];
    return res;
}

void solve() {
    LL B;
    int N;
    cin >> B >> N;
    vector<LL> c(37);
    for (int i = 0; i < N; ++i) cin >> c[i];
    sort(c.begin(), c.end());
//    reverse(c.begin(), c.end());

    double res = 0;

    for (int k = 1; k < 37; ++k) {
        int l = 35 - k;
        for (int j = 0; j <= l; ++j) if (c[k + j - 1] < c[k + j]) {
            LL S = sum(c, 0, k);
            LL D = sum(c, k, k + j);

            LL X = min(S + D + B, (c[k + j] - 1) * (k + j) + j);
            LL H = (X - j) / (k + j);
            if (H < c[k - 1]) continue;
            if (H + 1 < c[k + j - 1]) continue;

            LL Y = H * k - S;

            res = max(res, Y * 36.0 / k - H * (k + j) - j + S + D);
        }
    }

    static int testid;
    cout << "Case #" << ++testid << ": ";
    printf("%.10lf\n", res);
}

int main() {
    int tests;
    cin >> tests;
    while (tests --> 0)
        solve();
    return 0;
}
