#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>

#include <vector>
#include <set>
#include <map>
#include <bitset>
#include <queue>
#include <stack>
#include <list>

#include <ctime>
#include <cassert>

using namespace std;

typedef long double ldb;
typedef long long int64;
typedef pair <int, int> pii;
typedef pair <double, double> pdd;

#define y0 wwwwwww
#define y1 qqqqqqq
#define next NEXT
#define prev PREV
#define forn(i, n) for (int i = 0; i < (int) n; i++)
#define ford(i, n) for (int i = (int) n - 1; i >= 0; i--)
#define seta(a, b) memset(a, b, sizeof(a))
#define pb push_back
#define all(a) (a).begin(), (a).end()
#define last(a) a[a.size() - 1]
#define mp make_pair
#define fs first
#define sc second

template <class T> T sqr(T x) { return x * x; }

double const pi = 3.1415926535897932384626433832795;
int const inf = (int) 1e9;
int64 const inf64 = (int64) 4e18;

int64 a, b, k, d[33][2][2][2];

void move(int i, int x, int y, int z) {
    int64 a0, b0, a1, b1;
    int ok, xx, yy, zz;
    a0 = (1 << (i - 1));
    if (x == 1 && !(a & (1 << (i - 1)))) a0 = a & ((1 << i) - 1);
    b0 = (1 << (i - 1));
    if (y == 1 && !(b & (1 << (i - 1)))) b0 = b & ((1 << i) - 1);
    a1 = 1 << (i - 1);
    if (x == 1) {
        if (a & (1 << (i - 1))) a1 = a & ((1 << i) - 1);
        else a1 = 0;
    }
    b1 = 1 << (i - 1);
    if (y == 1) {
        if (b & (1 << (i - 1))) b1 = b & ((1 << i) - 1);
        else b1 = 0;
    }

    cerr << i << " " << x << " " << y << " " << z << " | " << d[i][x][y][z] << endl;
    cerr << a0 << " " << a1 << " " << b0 << " " << b1 << endl;

    // 0 0
    ok = 1;
    xx = x;
    if (a & (1 << (i - 1))) xx = 0;
    yy = y;
    if (b & (1 << (i - 1))) yy = 0;
    zz = z;
    if (k & (1 << (i - 1))) zz = 0;
    if (ok || !zz) d[i - 1][xx][yy][zz] += a0 * b0;

    // 0 1
    xx = x;
    if (a & (1 << (i - 1))) xx = 0;
    yy = y;
    if (!(b & (1 << (i - 1)))) ok = 0;
    zz = z;
    if (!(k & (1 << (i - 1)))) ok = 0;
    if (ok || !zz) d[i - 1][xx][yy][zz] += a0 * b1;

    // 1 0
    xx = x;
    if (!(a & (1 << (i - 1)))) ok = 0;
    yy = y;
    if (b & (1 << (i - 1))) yy = 0;
    zz = z;
    if (!(k & (1 << (i - 1)))) ok = 0;
    if (ok || !zz) d[i - 1][xx][yy][zz] += a1 * b0;

    // 1 1
    xx = x;
    if (!(a & (1 << (i - 1)))) ok = 0;
    yy = y;
    if (!(b & (1 << (i - 1)))) ok = 0;
    zz = z;
    if (k & (1 << (i - 1))) zz = 0;
    if (ok || !zz) d[i - 1][xx][yy][zz] += a1 * b1;
}

void solve() {
    cin >> a >> b >> k;
    seta(d, 0);
    d[30][1][1][1] = a * b;
    for (int i = 30; i > 0; --i)
        forn(x, 2)
            forn(y, 2)
                forn(z, 2)
                    move(i, x, y, z);
    int64 ans = 0;
    forn(x, 2)
        forn(y, 2)
            forn(z, 2)
                ans += d[0][x][y][z];
    cout << ans << endl;
}

void triv_solve() {
    int a, b, k, cnt = 0;
    cin >> a >> b >> k;
    forn(i, a)
        forn(j, b)
            if ((i & j) < k) cnt++;
    cout << cnt << endl;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

    int tst;
    cin >> tst;
    forn(i, tst) {
        cout << "Case #" << i + 1 << ": ";
        triv_solve();
    }

	return 0;
}
