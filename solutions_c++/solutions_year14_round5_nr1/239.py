#include <bits/stdc++.h>
using namespace std;

const int N = 1000000;
long long a[N];
long long s[N + 1];

inline void solve(int test) {
    int n;
    long long p, q, r, S;
    cin >> n >> p >> q >> r >> S;
    for (int i = 0; i < n; ++i) {
        a[i] = (i * p + q) % r + S;
    }

    s[0] = 0;
    for (int i = 0; i < n; ++i) {
        s[i + 1] = s[i] + a[i];
    }

    long long sum = s[n];

    long long ans = 0;
    int l = 0;
    for (int i = 0; i < n; ++i) {
        while (l < i && (s[i + 1] - s[l] >= s[l] && s[i + 1] - s[l] >= s[n] - s[i + 1])) {
            ++l;
        }
        if (l > 0) {
            --l;
        }
        if ((s[i + 1] - s[l] >= s[l] && s[i + 1] - s[l] >= s[n] - s[i + 1])) {
            ans = max(ans, sum - (s[i + 1] - s[l]));
        }
    }
    l = 1;
    for (int i = 0; i < n; ++i) {
        if (l < i + 1) {
            l = i + 1;
        }
        while (l <= n && s[l] - s[i + 1] <= s[i + 1]) {
            ++l;
        }
        --l;
        if (s[l] - s[i + 1] <= s[i + 1] && s[i + 1] >= s[n] - s[l]) {
            ans = max(ans, sum - s[i + 1]);
        }
    }
    reverse(a, a + n);
    s[0] = 0;
    for (int i = 0; i < n; ++i) {
        s[i + 1] = s[i] + a[i];
    }
    l = 1;
    for (int i = 0; i < n; ++i) {
        if (l < i + 1) {
            l = i + 1;
        }
        while (l <= n && s[l] - s[i + 1] <= s[i + 1]) {
            ++l;
        }
        --l;
        if (s[l] - s[i + 1] <= s[i + 1] && s[i + 1] >= s[n] - s[l]) {
            ans = max(ans, sum - s[i + 1]);
        }
    }
    cout << "Case #" << test << ": ";
    cout << setprecision(10) << fixed << ans / (double)sum << endl;
}

int main() {
    freopen("A.in", "r", stdin);
    freopen("out", "w", stdout);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        solve(i + 1);
    }
    return 0;
}
