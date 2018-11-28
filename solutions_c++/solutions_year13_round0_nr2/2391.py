#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <utility>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>
#include <queue>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

#define pb push_back
#define mp make_pair
#define sz(a) int((a).size())
#define forn(i, n) for (int i=0; i<(n); ++i)

int a[105][105];
int n, m;


bool solve() {
    forn (x, n) forn (y, m) {
        int cnt1 = 0; forn (i, n) cnt1 += a[i][y] > a[x][y];
        int cnt2 = 0; forn (i, m) cnt2 += a[x][i] > a[x][y];
        if (cnt1 && cnt2) return false;
    }
    return true;
}

int main()
{
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);

    int tc; scanf("%d", &tc);
    for (int tt=1; tt<=tc; ++tt) {
        scanf("%d %d", &n, &m);
        forn (i, n) forn (j, m)
            scanf("%d", &a[i][j]);
        printf("Case #%d: %s\n", tt, solve() ? "YES" : "NO");
    }

    return 0;
}
