#include <bits/stdc++.h>
using namespace std;

const int N = 1 << 16, M = 220;

int a[50][50], n, b[50][50];

int dfs (int k, int st) {
//    cout << "  " << k << ' '<< st << endl;
    if (k == (1 << n) - 1) return 1;
    for (int o = 0; o < n; o++) if ((k & (1 << o)) == 0) {
        int flag = 0;
        for (int i = 0; i < n; i++) if (a[o + 1][i + 1] && (st & (1 << i)) == 0) {
            flag = 1;
            if (dfs (k | (1 << o), st | (1 << i)) == 0) return 0;
        }
        if (flag == 0) return 0;
    }
    return 1;
}

int getnum (int i) {
    int num = 0;
    for (int j = 0; j < (n * n); j++) if (i & (1 << j)) num++;
    return num;
}

int solve (int i) {
    memcpy (a, b, sizeof a);
    for (int j = 1, l = 0; j <= n; j++) {
        for (int k = 1; k <= n; k++, l++) {
//            cout << i << ' '  << j << ' ' << k << ' ' << a[j][k] << endl;
            if (i & (1 << l))  {
                if (a[j][k])return 0;
                else a[j][k] = 1;
            }
        }
    }
//    cout << i << endl;
    int res = dfs (0, 0);
//    if (res && getnum (i) == 3) {
//        for (int j = 1, l = 0; j <= n; j++) {
//            for (int k = 1; k <= n; k++, l++) {
//    //            cout << i << ' '  << j << ' ' << k << ' ' << a[j][k] << endl;
//                cout << a[j][k];
//            }
//            cout << endl;
//        }
//        cout << endl;
//    }
//    for (int j = 1, l = 0; j <= n; j++) {
//        for (int k = 1; k <= n; k++, l++) {
//            if (i & (1 << l)) a[j][k] = 0;
//        }
//    }
    return res;
}

int main () {
    freopen ("in.txt", "r", stdin);
    freopen ("out.txt", "w", stdout);
//    for (int i = 1; i < N; i++) num[i] = num[i ^ (i & -i)] + 1;
    int T, cas = 1;
    cin >> T;
    while (T--) {
//        int n;
        cin >> n;
        int res = 1e9;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                scanf ("%1d", &b[i][j]);
            }
        }
        for (int i = 0; i < (1 << n * n); i++) {
//            cout << i << endl;
            if (solve (i)) {
//                cout << i << endl;

                res = min (res, getnum (i));
            }
        }
        printf ("Case #%d: %d\n", cas++, res);
    }
}
