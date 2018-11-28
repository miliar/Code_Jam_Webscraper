#pragma comment (linker, "/STACK:128000000")
#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>
#include <cassert>

#define mp make_pair
#define pb push_back
#define sz(x) ((int)(x).size())
#define forn(i, n) for(int i=0;i<(n);++i)
#define clr(ar, val) memset(ar, val, sizeof(ar))

using namespace std;

typedef long double ld;
typedef vector<int> vi;
typedef pair<int, int> pii;

const int N = 1e5 + 200;
const int INF = int(1e9);
const long long LINF = 1ll * INF * INF;
const int md = int(1e9) + 7;
const ld eps = 1e-9;
const ld PI = 3.1415926535897932384626433832795l;

int test, it, n, m, cnt, ans;
int st[17][17];

int check() {
    int res = 0;
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++) {
            //printf("%d %d %d\n", i, i, st[i][j]);
            if (st[i][j] && st[i][j - 1]) res++;
            if (st[i][j] && st[i - 1][j]) res++;
        }
    return res;
}

void rec(int x, int y, int need) {
    if (y == m + 1) {
        x++;
        y = 1;
    }
    if ((n - x) * m + (m - y + 1) < need) return;
    if (x == n + 1) {
        ans = min(ans, check());
        return;
    }
    st[x][y] = 0;
    rec(x, y + 1, need);
    if (need) {
        st[x][y] = 1;
        rec(x, y + 1, need - 1);
    }
}

int main()
{
    //ios_base::sync_with_stdio(false);
    //cin.tie(0);
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
    scanf("%d", &test);
    for (it = 1; it <= test; it++) {
        scanf("%d %d %d", &n, &m, &cnt);
        memset(st, 0, sizeof(st));
        ans = INF;
        rec(1, 1, cnt);
        printf("Case #%d: ", it);
        printf("%d\n", ans);
    }
    return 0;
}
