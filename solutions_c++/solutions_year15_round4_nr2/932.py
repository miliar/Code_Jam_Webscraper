#include <bits/stdc++.h>
#define endl "\n"
#define FOR(x, y, z) for (int x = (y); x < (z); ++x)
#define FORR(x, y, z) for (int x = (y); x > (z); --x)
#define GET(a, n) for (int __i = 0; __i < (n); ++__i) cin >> a[__i];
#define GETM(a, n, m) for (int __i = 0; __i < (n); ++__i) for (int __j = 0; __j < m; ++__j) cin >> a[__i][__j];
#define PRINTM(a, n, m) for (int __i = 0; __i < (n); ++__i) { for (int __j = 0; __j < m; ++__j) cout << a[__i][__j] << " ";  cout << endl; };
#define PRINT(a, n) for (int __i = 0; __i < (n); ++__i) cout << a[__i] << " ";
#define IT(a) a.begin(), a.end()
#define CASE(a, s) cout << "Case #" << a << ": " << s << endl;
#define DEB(a) cout << #a << " = " << (a) << endl; cout.flush();
#define DEBA(a) for (auto __i: a) cout << __i << " "; cout << endl;
#define IFDEB(b, a) if (b) { cout << #a << " = " << a << endl; cout.flush(); }
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
typedef vector <int> VI;
typedef vector <vector <int>> VVI;
typedef pair <int, int> PII;
const int MOD = 1000000007;
template <class T> typename T::value_type arr_sum(const T& v, int n) { typename T::value_type sum = 0; FOR(i, 0, n) sum += v[i]; return sum; }
struct Sync_stdio { Sync_stdio() { cin.tie(NULL); ios_base::sync_with_stdio(false); } } _sync_stdio;

double eps = 1e-14;

int main()
{
    int t;
    cin >> t;
    cout << fixed << setprecision(9);
    FOR (l, 0, t) {
        int n;
        cin >> n;
        double v;
        double tem;
        cin >> v >> tem;
        vector <pair <double, double>> a(n);
        FOR (i, 0, n) {
            cin >> a[i].first >> a[i].second;
        }
        if (n == 1) {
            if (abs(tem - a[0].second) < eps) {
                CASE(l + 1, v / a[0].first);
                continue;
            } else {
                CASE(l + 1, "IMPOSSIBLE");
                continue;
            }
        }
        double best = 1e20;
        if (abs(tem - a[0].second) < eps) {
            best = min(best, v / a[0].first);
        }
        if (abs(tem - a[1].second) < eps) {
            best = min(best, v / a[1].first);
        }
        if (abs(tem - a[0].second) < eps && abs(tem - a[1].second) < eps) {
            best = min(best, v / (a[0].first + a[1].first));
        }
        if (tem - a[0].second > eps && tem - a[1].second > eps) {
            CASE(l + 1, "IMPOSSIBLE");
            continue;
        }
        if (a[0].second - tem > eps && a[1].second - tem > eps) {
            CASE(l + 1, "IMPOSSIBLE");
            continue;
        }
        if (best < 1e18) {
            CASE(l + 1, best);
            continue;
        }
        //double tx = (a[0].first * a[0].second + a[1].first * a[1].second) / (a[0].first + a[1].first);
        double b1 = 1;
        double b2 = (tem - a[0].second) / (a[1].second - tem);
        //DEB(b2);
        double c1 = b1 / a[0].first;
        double c2 = b2 / a[1].first;
        //DEB(c1);
        //DEB(c2);
        double c = max(c1, c2);
        double vx = 1 + b2;
        //DEB(vx);
        best = min(best, v * c / vx);
        if (best > 1e18) {
            CASE(l + 1, "IMPOSSIBLE");
        } else {
            CASE(l + 1, best);
        }
    }
}
