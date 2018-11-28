#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <stack>
#include <bitset>
#define INF 0x3f3f3f3f
#define eps 1e-8
#define FI first
#define SE second
using namespace std;
typedef long long ll;

int n, m;

int a[305];

inline void getxy(int s, int &x, int &y) {
    if(s <= m) {
        x = 0; y = s - 1;
    } else if(s <= n + m) {
        x = s - m - 1;
        y = m - 1;
    } else if(s <= m + n + m) {
        x = n - 1;
        y = s - n - m;
        y = m - y;
    } else {
        y = 0;
        x = s - n - m - m;
        x = n - x;
    }
}

inline bool in(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < m;
}

inline void go(int x, int y, int &nx, int &ny, int t, int &d) {
    nx = x; ny = y;
    if(d == 0) {
        if(t) {
            d = 3;
            ++ ny;
        } else {
            d = 1;
            -- ny;
        }
    } else if(d == 1) {
        if(t) {
            d = 2;
            -- nx;
        } else {
            d = 0;
            ++ nx;
        }
    } else if(d == 2) {
        if(t) {
            d = 1;
            -- ny;
        } else {
            d = 3;
            ++ ny;
        }
    } else {
        if(t) {
            d = 0;
            ++ nx;
        } else {
            d = 2;
            -- nx;
        }
    }
}

inline bool connect(int s, int t, int st) {
    int x, y;
    getxy(s, x, y);
    int dir;
    if(s <= m)
        dir = 0;
    else if(s <= n + m)
        dir = 1;
    else if(s <= n + m + m)
        dir = 2;
    else dir = 3;
    while(true) {
        int p = x * m + y;
        int nx, ny;
        go(x, y, nx, ny, st >> p & 1, dir);
        x = nx; y = ny;
        if(!in(nx, ny)) break;
    }
    int tt;
    if(x < 0) {
        tt = y + 1;
    } else if(y >= m) {
        tt = m + x + 1;
    } else if(x >= n) {
        tt = m + n + (m - y);
    } else {
        tt = m + m + n + (n - x);
    }
    return t == tt;
}

bool check(int s) {
    for(int i = 0; i < 2 * (n + m); i += 2) {
        int x = a[i], y = a[i + 1];
        if(!connect(x, y, s)) return false;
    }
    return true;
}

int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("Cs.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; ++ cas) {
        scanf("%d%d", &n, &m);
        for(int i = 0; i < 2 * (n + m); ++ i) {
            scanf("%d", a + i);
        }
        printf("Case #%d:\n", cas);
        int tot = n * m, ans = -1;
        for(int i = 0; i < 1 << tot; ++ i) {
            if(check(i)) {
                ans = i;
                break;
            }
        }
        if(ans == -1) {
            puts("IMPOSSIBLE");
        } else {
            for(int i = 0; i < n; ++ i) {
                for(int j = 0; j < m; ++ j) {
                    int p = i * m + j;
                    putchar(ans >> p & 1 ? '\\' : '/');
                }
                puts("");
            }
        }
    }
    return 0;
}
