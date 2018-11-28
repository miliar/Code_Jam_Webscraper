#include <bits/stdc++.h>

using namespace std;

const int Inf = 1e9 + 7;

int T, cas, n, m;

int a[20][20], f[505], v[55];

int getf(int x) {
    return f[x] == x ? x : f[x] = getf(f[x]);
}

void Merge(int x, int y) {
//    cout << x << ' ' << y << "~~" << endl;
    int fx = getf(x), fy = getf(y);
    f[fx] = fy;
}

inline int Get(int x, int y, int t) {
    return 4 * (x * m + y) + t;
}

bool Check() {
//    for (int i = 0; i < n; i ++) {
//        for (int j = 0; j < m; j ++)
//            cout << a[i][j];
//        cout << endl;
//    }
//    cout << "~~~~~~~~" << endl;
    for (int i = 0; i < 4 * n * m + 2 * (n + m); i ++)
        f[i] = i;
    for (int i = 0; i < m; i ++)
        Merge(Get(0, i, 0), 4 * n * m + i);
    for (int i = 0; i < m; i ++)
        Merge(Get(n - 1, i, 2), 4 * n * m + n + m + m - 1 - i);
    for (int i = 0; i < n; i ++)
        Merge(Get(i, m - 1, 1), 4 * n * m + m + i);
    for (int i = 0; i < n; i ++)
        Merge(Get(i, 0, 3), 4 * n * m + n + m + m + n - 1 - i);
    for (int i = 0; i < n; i ++)
    for (int j = 0; j < m; j ++) {
        if (a[i][j] == 0) {
            Merge(Get(i, j, 0), Get(i, j, 1));
            Merge(Get(i, j, 2), Get(i, j, 3));
        } else {
            Merge(Get(i, j, 0), Get(i, j, 3));
            Merge(Get(i, j, 1), Get(i, j, 2));
        }
    }
    for (int i = 0; i < n; i ++)
    for (int j = 0; j < m; j ++) {
        if (i != 0) Merge(Get(i, j, 0), Get(i - 1, j, 2));
        if (j != 0) Merge(Get(i, j, 3), Get(i, j - 1, 1));
    }
    set<int> S;
    for (int i = 0; i < 2 * n + 2 * m; i += 2) {
        int fx = getf(v[i]), fy = getf(v[i + 1]);
//        cout << i << ' ' << fx << ' ' << fy << ' ' << v[i] << ' ' << v[i+1] << endl;
        if (fx != fy) return false;
        S.insert(fx);
    }
    if (S.size() != n + m) return false;
    return true;
}

int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> T;
    while (T --) {
        cin >> n >> m;
        int res = -1;
        for (int i = 0; i < 2 * n + 2 * m; i ++) {
            cin >> v[i]; v[i] --;
            v[i] += 4 * n * m;
        }
        for (int i = 0; i < 1 << (n * m); i ++) {
            for (int j = 0; j < n * m; j ++) {
                a[j / m][j % m] = (i >> j & 1);
            }
            if (Check()) {
                res = i;
                break;
            }
        }
        printf("Case #%d:\n", ++ cas);
        if (res == -1) puts("IMPOSSIBLE");
        else {
            for (int i = 0; i < n; i ++) {
                for (int j = 0; j < m; j ++) {
                    if (res >> (i * m + j) & 1) printf("/");
                    else printf("\\");
                }
                puts("");
            }
        }
    }
}
