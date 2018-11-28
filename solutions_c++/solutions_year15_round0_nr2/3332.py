#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

int p[1005];
int n;

int bin_search(int l, int r) {
    //cout << l << " " << r << "\n";
    if (l == r) return l;
    int m = (l + r) / 2;
    for (int s = 0; s < m; ++s) {
        //cout << s << " " << m << "\n";
        int k = 0;
        for (int i = 0; i < n; ++i) {
            if (p[i] % (m - s) == 0)
                k += p[i] / (m - s) - 1;
            else
                k += p[i] / (m - s);
        }
        if (k <= s) return bin_search(l, m);
    }
    return bin_search(m + 1, r);
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        cin >> n;
        int mx = -1;
        for (int i = 0; i < n; ++i) {
            cin >> p[i];
            mx = max(mx, p[i]);
        }
        int ans;
        ans = bin_search(0, mx);
        cout << "Case #" << t + 1 << ": " << ans << "\n";
    }
    return 0;
}
