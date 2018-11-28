#include<bits/stdc++.h>
typedef long double ld;
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
using namespace std;

int main() {
    freopen(".in", "r", stdin);
    freopen(".out", "w", stdout);
    int T;
    cin >> T;

    cout << fixed; 
    cout.precision(12);
    for (int test = 1; test <= T; ++test) {        
        int n, k;
        cin >> n >> k;
        int kk = k / 2;

        vector<double> P(n);
        for (int i = 0; i < n; ++i) {
            cin >> P[i];
        }
        sort(P.begin(), P.end());

        double ans = 0;
        vector<double> p, f, f1;
        for (int l = 0; l <= k; ++l) {
            p.clear();
            for (int j = 0; j < l; ++j) {
                p.push_back(P[j]);
            }
            for (int j = n - k + l; j < n; ++j) {
                p.push_back(P[j]);
            }
            if (p.size() != k) {
                continue;
            }

            f.assign(k + 1, 0.0);
            f[0] = 1.0;
            for (int i = 0; i < k; ++i) {
                f1.assign(k + 1, 0.0);
                for (int j = 0; j <= kk && j <= i; ++j) {
                    f1[j + 1] += f[j] * p[i];
                    f1[j] += f[j] * (1.0 - p[i]);
                }
                f.swap(f1);
            }
            ans = max(ans, f[kk]);
        }
        cout << "Case #" << test << ": ";
        cout << ans;
        cout << endl;
    }

    return 0;
}
