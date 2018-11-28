#include <bits/stdc++.h>
using namespace std;


void solve(int test) {
    int n;
    cin >> n;
    double a[n];
    double b[n];
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    for (int i = 0; i < n; ++i) {
        cin >> b[i];
    }

    sort(a, a + n);
    sort(b, b + n);

    int ans1 = 0;
    int i = 0, j = 0;
    for (i = 0; i < n; ++i) {
        while (j < n && a[j] < b[i]) {
            ++j;
        }
        if (j < n) {
            ++j;
            ++ans1;
        }
    }
    int ans2 = 0;
    i = 0, j = 0;
    for (i = 0; i < n; ++i) {
        while (j < n && b[j] < a[i]) {
            ++j;
        }
        if (j < n) {
            ++j;
            ++ans2;
        }
    }
    ans2 = n - ans2;
    cout << "Case #" << test << ": ";
    cout << ans1 << " " << ans2 << endl;
}

int main() {
    freopen("D-large.in", "r", stdin);
    freopen("out", "w", stdout);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        solve(i + 1);
    }
    return 0;
}
