#include <functional>
#include <algorithm>
#include <iostream>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <string>
#include <vector>
#include <ctime>
#include <queue>
#include <set>
#include <map>
using namespace std;
#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define fore(i, b, e) for (int i = (int)(b); i <= (int)(e); i++)
#define ford(i, n) for (int i = (int)(n)-1; i >= 0; i--)
#define mp make_pair
#define fi first
#define se second
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define eq(x, y) (abs((x)-(y))<eps)
#define lt(x, y) ((x)<(y)-eps)
#define le(x, y) ((x)<=(y)+eps)
#define gt(x, y) ((x)>(y)+eps)
#define ge(x, y) ((x)>=(y)-eps)
typedef long long i64;
typedef unsigned long long u64;
typedef unsigned int u32;
typedef double ld;
typedef pair<int, int> pii;
typedef vector<int> vi;
const int inf = 1e9+100500;
const int maxn = 150;

int n, m;
int a[maxn][maxn];
int b[maxn][maxn];

bool solve()
{
    cin >> n >> m;
    forn(i, n) forn(j, m) cin >> a[i][j];
    forn(i, n) forn(j, m) b[i][j] = 100;
    forn(i, n) {
        int mx = 0;
        forn(j, m) mx = max(mx, a[i][j]);
        forn(j, m) b[i][j] = min(b[i][j], mx);
    }
    forn(j, m) {
        int mx = 0;
        forn(i, n) mx = max(mx, a[i][j]);
        forn(i, n) b[i][j] = min(b[i][j], mx);
    }
    forn(i, n) forn(j, m) if (a[i][j] != b[i][j])
        return false;
    return true;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin >> t;
    forn(i, t)
        cout << "Case #" << i+1 << ": " << (solve() ? "YES" : "NO") << endl;

#ifdef HOME
    cerr << "time = " << clock()/1000 << " ms" << endl;
#endif
    return 0;
}
