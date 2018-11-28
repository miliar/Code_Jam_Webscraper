#include <bits/stdc++.h>
#ifndef M_PI
#define M_PI 3.14159265358979323846264338327
#endif // M_PI
#define endl "\n"
#define S struct
#define X first
#define Y second
#define V vector
#ifndef __linux__
#define LLD "%I64d"
#else
#define LLD "%ll""d"
#endif
#define FOR(x, y, z) for (int x = (y); x < (z); ++x)
#define FORR(x, y, z) for (int x = (y); x > (z); --x)
#define GET(a, n) for (int __i = 0; __i < (n); ++__i) cin >> a[__i];
#define GETM(a, n, m) for (int __i = 0; __i < (n); ++__i) for (int __j = 0; __j < m; ++__j) cin >> a[__i][__j];
#define PRINTM(a, n, m) for (int __i = 0; __i < (n); ++__i) { for (int __j = 0; __j < m; ++__j) cout << a[__i][__j] << " ";  cout << endl; };
#define PRINT(a, n) for (int __i = 0; __i < (n); ++__i) cout << a[__i] << " ";
#define IT(a) a.begin(), a.end()
#define SQR(x) (x) * (x)
#define CASE(a, s) cout << "Case #" << a << ": " << s << endl;
#define DEB(a) cout << #a << " = " << (a) << endl; cout.flush();
#define DEBA(a) for (auto __i: a) cout << __i << " "; cout << endl; cout.flush();
#define IFDEB(b, a) if (b) { cout << #a << " = " << (a) << endl; cout.flush(); }
using namespace std;
typedef long long LL;
typedef long double LD;
typedef unsigned long long ULL;
typedef pair <int, int> PII;
typedef pair <LL, LL> PLL;
const int MOD = 1000000007;
void sync_stdio() { cin.tie(NULL); ios_base::sync_with_stdio(false); }
S Sync_stdio { Sync_stdio() { cin.tie(NULL); ios_base::sync_with_stdio(false); } } _sync_stdio;

int solve(int t)
{
    int n;
    cin >> n;
    CASE(t + 1, n);
}

#define double LD

int solve2(int t)
{
    int n, k;
    cin >> n >> k;
    vector <double> p(n);
    FOR (i, 0, n) {
        cin >> p[i];
    }
    double res = 0;
    FOR (i, 0, 1 << n) {
        if (__builtin_popcount(i) != k) {
            continue;
        }
        vector <vector <double>> dp(n + 1, vector <double> (n + 1));
        dp[0][0] = 1;
        int t = i;
        FOR (j, 0, n) {
            int x = t & 1;
            if (x == 1) {
                FOR (l, 0, n) {
                    dp[j + 1][l] += dp[j][l] * (1 - p[j]);
                    dp[j + 1][l + 1] += dp[j][l] * p[j];
                }
            } else {
                FOR (l, 0, n) {
                    dp[j + 1][l] = dp[j][l];
                }
            }
            t /= 2;
        }
        res = max(res, dp[n][k / 2]);
    }
    CASE(t + 1, res);
}

int main()
{
    int n;
    cin >> n;
    cout << fixed << setprecision(10);
    FOR (i, 0, n) {
        cerr << "CASE " << i + 1 << endl;
        solve2(i);
    }
    return 0;
}
