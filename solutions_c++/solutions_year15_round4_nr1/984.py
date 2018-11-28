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

vector <string> v;

int check(int x, int y)
{
    int c = 4;
    vector <int> a(4);
    FOR (i, x + 1, int(v.size())) {
        if (v[i][y] != '.') {
            --c;
    //        cout << "COT1" << endl;
            a[0] = 1;
            break;
        }
    }
    FORR (i, x - 1, -1) {
        if (v[i][y] != '.') {
            --c;
    //        cout << "COT2 " << i << ":" << y << endl;
            a[1] = 1;
            break;
        }
    }
    FOR (i, y + 1, int(v[0].size())) {
        if (v[x][i] != '.') {
            --c;
    //        cout << "COT3" << endl;
            a[2] = 1;
            break;
        }
    }
    FORR (i, y - 1, -1) {
        if (v[x][i] != '.') {
            --c;
    //        cout << "COT4" << endl;
            a[3] = 1;
            break;
        }
    }
    if (c == 4) {
        return -1;
    }
    //cout << x << ":" << y << endl;
    //DEBA(a);
    if (a[0] == 1 && v[x][y] == 'v') {
        return 0;
    }
    if (a[1] == 1 && v[x][y] == '^') {
        return 0;
    }
    if (a[2] == 1 && v[x][y] == '>') {
        return 0;
    }
    if (a[3] == 1 && v[x][y] == '<') {
        return 0;
    }
    return 1;
}

int main()
{
    int t;
    cin >> t;
    FOR (l, 0, t) {
        int r, c;
        cin >> r >> c;
        v.resize(0);
        v.resize(r);
        GET(v, r);
        int res = 0;
        FOR (i, 0, r) {
            FOR (j, 0, c) {
                if (v[i][j] != '.') {
                    int t = check(i, j);
                    if (t == -1) {
                        CASE(l + 1, "IMPOSSIBLE");
                        goto X;
                    }
                    res += t;
                }
            }
        }
        CASE(l + 1, res);
X:;
    }
}
