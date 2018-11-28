#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <vector>
#include <string>
#include <string.h>
#include <ctime>
#include <queue>
#include <map>
#include <set>
#include <stack>
#include <iomanip>
#include <assert.h>
#include <deque>
#include <sstream>

#ifdef WIN32
    #define I64 "%I64d"
#else
    #define I64 "%lld"
#endif // WIN32

#define INF (1LL << 30)
#define md 1000000007
#define F first
#define S second
#define ll long long
#define mp make_pair
#define pb push_back
#define next(i) (i) + ((i) & (-i))
#define prev(i) (i) - ((i) & (-i))

using namespace std;
char a[2000][2000];
int n, m;

bool check(int x, int y) {
    if (a[x][y] == '.') {
        return true;
    }

    bool f = false;
    for (int i = 0; i < n; i++) {
        if (i != x && a[i][y] != '.') {
            f = true;
        }
    }

    for (int i = 0; i < m; i++) {
        if (i != y && a[x][i] != '.') {
            f = true;
        }
    }

    return f;
}

bool checkifalready(int x, int y) {
    if (a[x][y] == '^') {
        if (x == 0) {
            return false;
        }
        for (int i = 0; i < x; i++) {
            if (a[i][y] != '.') {
                return true;
            }
        }
    }
    if (a[x][y] == '>') {
        if (y == m - 1) {
            return false;
        }
        for (int i = y + 1; i < m; i++) {
            if (a[x][i] != '.') {
                return true;
            }
        }
    }
    if (a[x][y] == 'v') {
        if (x == n - 1) {
            return false;
        }
        for (int i = x + 1; i < n; i++) {
            if (a[i][y] != '.') {
                return true;
            }
        }
    }
    if (a[x][y] == '<') {
        if (y == 0) {
            return false;
        }
        for (int i = 0; i < y; i++) {
            if (a[x][i] != '.') {
                return true;
            }
        }
    }
    return false;
}

void modify(int x, int y, int &ans) {
    if (checkifalready(x, y)) {
        return;
    }
    ans++;
    char p[] = {'<', '>', '^', 'v'};
    for (int i = 0; i < 4; i++) {
        a[x][y] = p[i];
        if (checkifalready(x, y)) {
            return;
        }
    }
}

void solve(int num) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%c", &a[i][j]);
        }
        scanf("\n");
    }
    int ans = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (a[i][j] != '.') {
                if (!check(i, j)) {
                    printf("Case #%d: IMPOSSIBLE\n", num);
                    return;
                }
                modify(i, j, ans);
            }
        }
    }
    printf("Case #%d: %d\n", num, ans);
}

int main() {
    #ifndef ONLINE_JUDGE
            freopen("input.txt", "r", stdin);
            freopen("output.txt", "w", stdout);
    #else
            //freopen("input.txt", "r", stdin);
            //freopen("output.txt", "w", stdout);
    #endif //
    int t;
    scanf("%d\n", &t);

    for (int z = 0; z < t; z++) {
        scanf("%d %d\n", &n, &m);
        solve(z + 1);
    }

    return 0;
}


