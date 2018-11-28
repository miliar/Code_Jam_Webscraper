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

//typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
typedef pair<ld, ld> point;

const int N = 200;
const int INF = int(1e9) + 7;
const long long LINF = 1ll * INF * INF;
const int md = int(1e9) + 7;
const ld eps = 1e-9;
const ld PI = 3.1415926535897932384626433832795l;

int test, it;
int n, m, ans, i, j, k;
string a[N];
int cnt[N][N];
int dx[N], dy[N];

int check(int x, int y) {
    if ((dx[x] == 1) && (dy[y] == 1)) {
        return 0;
    }

    int i, j;
    if (a[x][y] == '^') {
        i = -1; j = 0;
    }
    if (a[x][y] == '>') {
        i = 0; j = 1;
    }
    if (a[x][y] == 'v') {
        i = 1; j = 0;
    }
    if (a[x][y] == '<') {
        i = 0; j = -1;
    }
    k = 1;
    while (true) {
        if (x + k * i < 0 || x + k * i >= n || y + k * j < 0 || y + k * j >= m) {
            cnt[x][y] = 0;
            break;
        }
        if (a[x + k * i][y + k * j] != '.') {
            cnt[x][y] = 1;
            break;
        }
        k++;
    }
    return 1;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
    cin >> test;
    for (it = 1; it <= test; it++) {
        cin >> n >> m;

        clr(dx, 0);
        clr(dy, 0);
        clr(cnt, 0);

        for (i = 0; i < n; i++) cin >> a[i];

        for (i = 0; i < n; i++)
            for (j = 0; j < m; j++) {
                if (a[i][j] != '.') {
                    dx[i]++;
                    dy[j]++;
                }
            }

        int ok = 1;
        ans = 0;
        for (i = 0; i < n; i++)
            for (j = 0; j < m; j++)
            if (a[i][j] != '.') {
                if (!check(i, j)) {
                    ok = 0;
                }
                if (!cnt[i][j]) {
                    ans++;
                    //cout << i << " " << j;
                }
            }

        if (!ok) {
            printf("Case #%d: ", it);
            printf("IMPOSSIBLE\n");
            continue;
        }

        printf("Case #%d: ", it);
        printf("%d\n", ans);
    }
    return 0;
}
