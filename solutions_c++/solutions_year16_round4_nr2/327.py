#include <bits/stdc++.h>
using namespace std;

const int N = 1 << 16, M = 220;
int num[N], bn, an;
double x[M], t[M], a[M], b[M], dp[M][M];

double solve (int l1, int r1, int l2, int r2) {
//    if (l1 > r1 || l2 > r2) return 0.0;
    int tn = 0;
//    for (int i = l1; i <= r1; i++) if (i < 1 || i > an) return 0.0; else t[++tn] = a[i];
//    for (int i = l2; i <= r2; i++) if (i < 1 || i > bn) return 0.0; else t[++tn] = b[i];
    for (int i = l1; i <= r1; i++) t[++tn] = x[i];
    for (int i = l2; i <= r2; i++) t[++tn] = x[i];
//    cout << l1 << ' ' << r1 << ' ' << l2 << ' ' << r2 << endl;
//    for (int i = 1; i <= tn; i++) cout << t[i] << ' '; cout << endl;
    memset (dp, 0, sizeof dp);
    dp[0][0] = 1;
    for (int i = 0; i < tn; i++) {
        for (int j = 0; j <= tn; j++) if (dp[i][j]) {
            dp[i + 1][j + 1] += dp[i][j] * t[i + 1];
            dp[i + 1][j] += dp[i][j] * (1 - t[i + 1]);
        }
    }
    return dp[tn][tn / 2];
}

int main () {
    freopen ("in.txt", "r", stdin);
    freopen ("out.txt", "w", stdout);
//    for (int i = 1; i < N; i++) num[i] = num[i ^ (i & -i)] + 1;
    int T, cas = 1;
    cin >> T;
    while (T--) {
        int n, k;
        cin >> n >> k;
        double res = 0;
        int ri;
        for (int i= 1; i<= n; i++) cin >> x[i];
        sort (x + 1, x + 1 + n);
        an = 0, bn = 0;
        double res2 = 0;
//        for (int i = 1; i <= n; i++) if (x[i] < 0.5) a[++an] = x[i]; else b[++bn] = x[i];
//        cout << an << ' ' << bn << endl;
        for (int i = 0; i <= k; i++) {
//            for (int j = 1; j + i - 1 <= an; ) {
//                for (int l = 1; l + (k - i) - 1 <= bn; l++) {
//                    res2 = min (res2, solve (j, j + i - 1, l, l + (k - i) - 1));
//                }
//            }
            res2 = max (res2, solve (1, i, n - (k - i) + 1, n));
//            res2 = max (res2, solve (1, i, 1, (k - i)));
//            res2 = max (res2, solve (1, i,       bn - (k - i) + 1, bn));
//            res2 = max (res2, solve (an - i + 1, an, 1, (k - i)));
//            res2 = max (res2, solve (an - i + 1, an, bn - (k - i) + 1, bn));
        }
//        for (int i = 1; i < (1 << n); i++) if (num[i] == k) {
////            cout << i << endl;
//            int tn = 0;
//            for (int j = 0; j < n; j++) if (i & (1 << j)) {
//                t[tn++] = x[j + 1];
//            }
//            double tmp = 0;
//            for (int j = 0; j < (1 << k); j++) if (num[j] == k / 2) {
////                cout << j << endl;
//                double tmp2 = 1;
//                for (int K = 0; K < k; K++) {
//                    if (j & (1 << K)) tmp2 *= t[K];
//                    else tmp2 *= (1 - t[K]);
//                }
//                tmp += tmp2;
//            }
////            cout << i << ' ' << tmp << endl;
//            if (res < tmp) {
//                res = max (res, tmp);
//                ri = i;
//            }
//        }
        printf ("Case #%d: %.10f\n", cas++, res2);
//        printf ("Case #%d: %.10f\n", cas++, res);
//        for (int j = 0; j < n; j++) cout << x[j + 1] << ' '; cout << endl;
//        for (int j = 0; j < n; j++) if (ri & (1 << j)) {
//            cout << x[j + 1] << ' ';
//        }
//        cout << endl;
    }
}
