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

vector <vector <int>> v;

int go (vector <int> used1, vector <int> used2)
{
    if (count(IT(used1), 0) == 0) {
        return 1;
    }
    int n = used1.size();
    int flag = 0;
    FOR (i, 0, n) {
        if (used1[i] == 1) {
            continue;
        }
        FOR (j, 0, n) {
            if (used2[j] == 1) {
                continue;
            }
            if (v[i][j] == 1) {
                used1[i] = 1;
                used2[j] = 1;
                flag = 1;
                if (!go(used1, used2)) {
                    return 0;
                }
                used1[i] = 0;
                used2[j] = 0;
            }
        }
    }
    return flag;
}

int check(int x, int n)
{
    v.assign(n, vector <int> (n));
    FOR (i, 0, n) {
        FOR (j, 0, n) {
            v[i][j] = x & 1;
            x /= 2;
        }
    }
    vector <int> used1(n);
    vector <int> used2(n);
    int flag = 0;
    FOR (i, 0, n) {
        FOR (j, 0, n) {
            if (v[i][j] == 1) {
                used1[i] = 1;
                used2[j] = 1;
                flag = 1;
                if (!go(used1, used2)) {
                    return 0;
                }
                used1[i] = 0;
                used2[j] = 0;
            }
        }
    }
    return flag;
}

int ok(int x, const vector <string> &v)
{
    int n = v.size();
    FOR (i, 0, n) {
        FOR (j, 0, n) {
            if (v[i][j] - '0' == 1 && (x & 1) == 0) {
                return 0;
            }
            x /= 2;
        }
    }
    return 1;
}

int solve2(int t)
{
    int n;
    cin >> n;
    vector <string> v(n);
    GET(v, n);
    vector <int> a(n);
    vector <int> b(n);
    int res = INT_MAX;
    FOR (i, 0, 1 << (n * n)) {
        if (!ok(i, v)) {
            continue;
        }
        if (check(i, n)) {
            res = min(res, __builtin_popcount(i));
        }
    }
    int cnt = 0;
    FOR (i, 0, n) {
        cnt += count(IT(v[i]), '1');
    }
    CASE(t + 1, res - cnt);
    return 0;
}

int main()
{
    int n;
    cin >> n;
    FOR (i, 0, n) {
        cerr << "CASE " << i + 1 << endl;
        solve2(i);
    }
    return 0;
}

