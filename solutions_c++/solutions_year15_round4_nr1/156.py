#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <string>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <queue>
#include <assert.h>

using namespace std;

#define ll long long
#define ull unsigned long long
#define ld long double
#define mp make_pair
#define pb push_back
#define fst first
#define snd second

template<typename T>
T abs(T x) {
    return x > 0 ? x : -x;
}

template<typename T>
T sqr(T x) {
    return x * x;
}

const int dirs[5][2] = {
        0, 0,
        1, 0,
        -1, 0,
        0, 1,
        0, -1,
};

const int maxn = 105;

int a[maxn][maxn];

map<char, int> c2d( {
        mp('.', 0),
        mp('v', 1),
        mp('^', 2),
        mp('>', 3),
        mp('<', 4),
                    });


int n, m;

auto valid = [&](int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < m;
};

bool check(int i, int j) {
    if (!a[i][j]) {
        return true;
    }
    int x = i, y = j;
    int d = a[x][y];
    while (valid(x, y)) {
        x += dirs[d][0];
        y += dirs[d][1];

        if (valid(x, y) && a[x][y]) {
            break;
        }
    }

    return valid(x, y);
}


int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    int t;
    scanf("%d\n", &t);
    int tt = 0;
    while (t--) {
        tt++;

        scanf("%d %d\n", &n, &m);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                char c;
                scanf("%c", &c);
                assert(c2d.find(c) != c2d.end());
                a[i][j] = c2d[c];

            }

            scanf("\n");
        }

        bool imp = 0;
        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (check(i, j)) {
                    continue;
                }

                bool any = false;
                for (int nd = 1; nd <= 4; nd++) {
                    a[i][j] = nd;
                    if (check(i, j)) {
                        any = true;
                        break;
                    }
                }

                if (any) {
                    ans++;
                } else {
                    imp = 1;
                }
            }
        }

        printf("Case #%d: ", tt);

        if (imp) {
            printf("IMPOSSIBLE\n");
        } else {
            printf("%d\n", ans);
        }
    }

    return 0;
}