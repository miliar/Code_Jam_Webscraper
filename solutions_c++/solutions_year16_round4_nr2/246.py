#include <bits/stdc++.h>

#define NAME "test"

#define EPS (1e-9)
#define INF ((int)(1e+9))
#define LINF ((long long)(1e+18))

#define pb push_back
#define mp make_pair
#define fi first
#define se second

using namespace std;

typedef long long li;

void solve(int test_number);

int main() {
#ifdef _GEANY
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
#else
#endif
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    cout.setf(ios::fixed);
    cout.precision(9);
    cerr.setf(ios::fixed);
    cerr.precision(6);
    int n = 1;
    cin >> n;
    for (int i = 0; i < n; i++) {
        solve(i + 1);
    }
    return 0;
}

const int MAXN = 210;
int SHIFT = 200;

int n, k;
long double a[MAXN];
long double dp[MAXN][2 * MAXN + 10];
long double a1[MAXN];

pair<long double, int> naive() {
    for (int i = 0; i <= n; i++) {
        a1[i] = a[i];
    }
    long double res = 0;
    int rmask = 0;
    for (int msk = 0; msk < (1 << n); msk++) {
        int len = 1;
        for (int i = 0; i <= n; i++) {
            if (msk & (1 << i)) {
                a[len++] = a1[i + 1];
            }
        }
        if (len != k + 1)
            continue;
        //for (int i = 1; i <= k; i++) {
            //cerr << a[i] << ' ';
        //}
        //cerr << endl;
        memset(dp, 0, sizeof(dp));        
        dp[0][SHIFT] = 1;
        int n = k;
        for (int i = 0; i < n; i++) {
            for (int bal = 0; bal <= 2 * MAXN; bal++) {
                dp[i + 1][bal + 1] += dp[i][bal] * a[i + 1];
                dp[i + 1][bal - 1] += dp[i][bal] * (1.0 - a[i + 1]);
            }
        }
        if (dp[n][SHIFT] > res) {
            res = dp[n][SHIFT];
            rmask = msk;
        }
    }
    return { res, rmask};
}

void solve(int test_number) {
    cout << "Case #" << test_number << ": ";
    cin >> n >> k;
    for (int i = 1; i <= n; i++) {
        cin >> a[i];
    }
    sort(a + 1, a + n + 1);
    //pair<long double, int> cc = naive();
    //long double nres = cc.first;
    //int msk = cc.second;

    for (int i = 0; i <= n; i++) {
        a1[i] = a[i];
    }
    long double res = 0;
    for (int st = 0; st <= k; st++) {
        memset(a, 0, sizeof(a));
        for (int i = 0; i < st; i++) {
            a[i + 1] = a1[i + 1];
        }
        int f = k - st;
        for (int i = 0; i < f; i++) {
            a[st + 1 + i] = a1[n - (f - i) + 1];
        }
        //for (int i = 1; i <= n; i++) {
            //cout << a1[i] << ' ';
        //}
        //cout << endl;
        //cerr << st << ' ' << f << endl;
        //for (int i = 1; i <= k; i++) {
            //cerr << a[i] << ' ';
        //}
        //cerr << endl;
        memset(dp, 0, sizeof(dp));
        dp[0][SHIFT] = 1;
        for (int i = 0; i < k; i++) {
            for (int bal = 0; bal <= 2 * MAXN; bal++) {
                dp[i + 1][bal + 1] += dp[i][bal] * a[i + 1];
                dp[i + 1][bal - 1] += dp[i][bal] * (1.0 - a[i + 1]);
            }
        }
        res = max(res, dp[k][SHIFT]);
    }

    //if (fabs(res - nres) > EPS) {
        //cerr << "FAIL " << test_number << " " << nres << ' ' << res << endl;
        //while (msk != 0) {
            //cerr << msk % 2;
            //msk /= 2;
        //}
        //cerr << endl;
        //exit(0);
    //}
        //while (msk != 0) {
            //cerr << msk % 2;
            //msk /= 2;
        //}
        //cerr << endl;
    cout << res << endl;
    cerr << test_number << endl;
}

