#include <bits/stdc++.h>
#ifndef M_PI
#define M_PI 3.14159265358979323846264338327
#endif // M_PI
#define endl "\n"
#define FOR(x, y, z) for (int x = (y); x < (z); ++x)
#define FORR(x, y, z) for (int x = (y); x > (z); --x)
#define GET(a, n) for (int __i = 0; __i < (n); ++__i) cin >> a[__i];
#define GETM(a, n, m) for (int __i = 0; __i < (n); ++__i) for (int __j = 0; __j < m; ++__j) cin >> a[__i][__j];
#define PRINTM(a, n, m) for (int __i = 0; __i < (n); ++__i) { for (int __j = 0; __j < m; ++__j) cout << a[__i][__j] << " ";  cout << endl; };
#define PRINT(a, n) for (int __i = 0; __i < (n); ++__i) cout << a[__i] << " ";
#define IT(a) a.begin(), a.end()
#define SQR(x) (x) * (x)
#define CASE(a) cout << "Case #" << a << ": " << endl;
#define DEB(a) cout << #a << " = " << (a) << endl; cout.flush();
#define DEBA(a) for (auto __i: a) cout << __i << " "; cout << endl; cout.flush();
#define IFDEB(b, a) if (b) { cout << #a << " = " << (a) << endl; cout.flush(); }
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
typedef pair <int, int> PII;
typedef pair <LL, LL> PLL;
const int MOD = 1000000007;
struct Sync_stdio { Sync_stdio() { cin.tie(NULL); ios_base::sync_with_stdio(false); } } _sync_stdio;

int is_not_probable_prime(LL x)
{
    FOR (i, 2, min(x, 100000LL)) {
        if (x % i == 0) {
            return i;
        }
    }
    return 0;
}

vector <int> ans(11);

int check(int x, int n)
{
    FOR (k, 2, 11) {
        LL res = 0;
        FORR (j, n - 1, -1) {
            res *= k;
            res += (x >> j) & 1;
        }
        assert(k != 2 || x == res);
        if (!(ans[k] = is_not_probable_prime(res))) {
            return 0;
        }
    }
    return 1;
}

void print(int x, int sz)
{
    FORR (i, sz - 1, -1) {
        cout << ((x >> i) & 1);
    }
    cout << " ";
    FOR (i, 2, 11) {
        cout << ans[i] << " ";
    }
    cout << endl;
}

int solve(int l)
{
    int n, k;
    cin >> n >> k;
    CASE(l + 1);
    for (int i = 1 + (1 << (n - 1)); k > 0 && i < (1 << n); i += 2) {
        if (check(i, n)) {
            print(i, n);
            --k;
        }
    }
    assert(k == 0);
    return 0;
}

int main()
{
    int t;
    cin >> t;
    FOR (i, 0, t) {
        solve(i);
    }
}
