#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>

typedef long long i64;

using namespace std;

bool check(i64 lim, i64 r, i64 k) {
    i64 sum = (2 * r + 1 + 2 * r + 4 * k - 3) * k / 2;
    return sum <= lim;
}

i64 solve(i64 lim, i64 r) {
    i64 low = 0, high = min((i64)sqrt((double)lim * 2), lim / r + 1) + 1, mid, ret = -1;

    while (low <= high) {
        mid = (low + high) >> 1;
        if (check(lim, r, mid)) {
            ret = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    return ret;
}

int main() {
    int t, ct = 0;
    i64 s, r, ans;

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    cin >> t;
    while (t--) {
        cin >> r >> s;
        ans = solve(s, r);
        printf("Case #%d: ", ++ct);
        cout << ans << endl;
    }

    return 0;
}
