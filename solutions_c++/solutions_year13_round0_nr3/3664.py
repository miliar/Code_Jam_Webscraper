#include <iostream>
using namespace std;

typedef long long LL;

LL a, b;

bool is_palindr(LL x) {
    LL rev = 0;
    for (LL temp = x; temp; temp /= 10)
        rev = rev * 10 + temp % 10;
    return rev == x;
}

LL solve() {
    LL ret = 0;
    for (LL x = 1; x * x <= b; ++x) {
        if (!is_palindr(x)) continue;
        LL xx = x * x;
        if (xx < a || !is_palindr(xx)) continue;
        ++ret;
        // cout << x << ": " << xx << '\n';
    }
    return ret;
}

int main() {
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; ++tt) {
        cin >> a >> b;
        cout << "Case #" << tt << ": " << solve() << '\n';
    }

    return 0;
}

