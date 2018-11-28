#include <iostream>
#include <iomanip>
#include <cstring>
#include <string>
#include <algorithm>
#include <queue>
#include <map>
#include <deque>
#include <set>
#include <vector>
#include <cstdlib>
#include <iomanip>
#include <ctime>
#include <fstream>

#define pb push_back
#define mp make_pair
#define F first
#define S second

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef long double ld;

const int INF = int(1e9);
const ll INFll = 1ll * INF * INF;
const int MOD = 1000000007;

int u[40000000], o, n, m, k, q, used[5][5], f[5][5], r[5][5];
queue<pii> Q;
bool F;

int get(int x, int y) {
    return 1 << ((x * m) + y);
}

int g(int x, int y) {
    if (x < 0 || y < 0 || x == n || y == m)
        return 0;
    return used[x][y];
}

void print(int x, int y) {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j)
            if (i == x && j == y)
                cout << 'c';
            else
                if (used[i][j] == 0)
                    cout << '.';
                else
                    cout << '*';
        cout << endl;
    }
}

void add(int x, int y) {
    if (x == n || y == m || x < 0 || y < 0 || used[x][y] == 1 || r[x][y])
        return;
    Q.push(mp(x, y));
    r[x][y] = 1;
}

void go(int x) {
    if (F || u[x] == o)
        return;
    u[x] = o;
    if (k == q) {
        int e = 0;
        int a = -1, b = -1;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                r[i][j] = 0, f[i][j] = g(i - 1, j) + g(i - 1, j - 1) + g(i - 1, j + 1) + g(i, j - 1) + g(i, j + 1) + g(i + 1, j) + g(i + 1, j + 1) + g(i + 1, j - 1);
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j) {
                if (used[i][j] == 0 && f[i][j] == 0)
                    a = i, b = j;
                e += (1 - used[i][j]);
            }
        if (e == 1) {
            F = 1;
            for (int i = 0; i < n; ++i)
                for (int j = 0; j < m; ++j)
                    if (used[i][j] == 0)
                        a = i, b = j;
            print(a, b);
            return;
        }
        if (e > 1 && a == -1)
            return;
        Q.push(mp(a, b));
        r[a][b] = 1;
        while (!Q.empty()) {
            int x1 = Q.front().F, y1 = Q.front().S;
            Q.pop();
            if (f[x1][y1])
                continue;
            add(x1 + 1, y1);
            add(x1 - 1, y1);
            add(x1, y1 + 1);
            add(x1, y1 - 1);
            add(x1 + 1, y1 + 1);
            add(x1 + 1, y1 - 1);
            add(x1 - 1, y1 + 1);
            add(x1 - 1, y1 - 1);
        }
        F = 1;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                if (used[i][j] == 0 && r[i][j] == 0)
                    F = 0;
        if (F)
            print(a, b);
        return;
    }
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            if (used[i][j] == 1) {
                if (i && g(i - 1, j) == 0) {
                    used[i - 1][j] = 1;
                    k++;
                    go(x | get(i - 1, j));
                    used[i - 1][j] = 0;
                    k--;
                }
                if (j && g(i, j - 1) == 0) {
                    k++;
                    used[i][j - 1] = 1;
                    go(x | get(i, j - 1));
                    k--;
                    used[i][j - 1] = 0;
                }
            }
}

int main() {
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    #ifdef LOCAL
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    int t;
    cin >> t;
    for (o = 1; o <= t; ++o) {
        cout << "Case #" << o << ":\n";
        cin >> n >> m >> q;
        F = 0;
        k = 0;
        if (q == 0)
            go(0);
        else {
            k = 1;
            used[n - 1][m - 1] = 1;
            go(get(n - 1, m - 1));
            used[n - 1][m - 1] = 0;
        }
        if (!F)
            cout << "Impossible\n";
    }
    return 0;
}

