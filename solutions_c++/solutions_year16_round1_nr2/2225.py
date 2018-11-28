#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <array>

using namespace std;

int n;
vector<vector<int>> a;
vector<vector<int>> m;

bool operator==(vector<int> &a, vector<int> &b)
{
    if (a.size() != b.size()) {
        return false;
    }
    for (int i = 0; i < a.size(); i++) {
        if (a[i] != b[i]) {
            return false;
        }
    }
    return true;
}

void check(vector<int> &v)
{
    // for (int i = 0; i < v.size(); i++) {
    //     cerr << v[i] << " ";
    // }
    // cerr << endl;
    // return;
    // !

    vector<char> used(2 * n - 1, 0);
    for (int i = 0; i < v.size(); i++) {
        used[v[i]] = 1;
        for (int j = 0; j < n; j++) {
            m[i][j] = a[v[i]][j];
        }
    }
    vector<int> cand;
    for (int j = 0; j < n; j++) {
        vector<int> c(n, 0);
        for (int i = 0; i < n; i++) {
            c[i] = m[i][j];
        }
        bool ok = false;
        for (int u = 0; u < used.size(); u++) {
            if (used[u] == 0 && a[u] == c) {
                used[u] = 1;
                ok = true;
            }
        }
        if (!ok) {
            if (cand.size() == 0) {
                cand = c;
            } else {
                return;
            }
        }
    }
    for (const auto& x: cand) {
        cout << x << " ";
    }
    cout << endl;
    v.resize(0);
}

bool can_be(int prev, int cur)
{
    if (prev == -1) {
        return true;
    }
    for (int i = 0; i < n; i++) {
        if (a[prev][i] >= a[cur][i]) {
            return false;
        }
    }
    return true;
}

void gen(vector<char> &u, vector<int> &v, int pos, int prev)
{
    if (v.size() == 0) {
        return;
    }
    if (pos == n) {
        check(v);
        return;
    }
    for (int i = 0; i < 2 * n - 1; i++) {
        if (!can_be(prev, i) || u[i] == 1) {
            continue;
        }
        // if (prev == 1 && i == 3) {
        //     cerr << "??" << can_be(prev, i) << endl;
        // }
        u[i] = 1;
        v[pos] = i;
        gen(u, v, pos + 1, i);
        u[i] = 0;
    }
}

void solve()
{
    m.assign(n, vector<int>(n, -1));
    vector<int> v(n, 0);
    vector<char> u(2 * n - 1, 0);
    gen(u, v, 0, -1);
}

int main()
{
    int t;
    scanf("%d", &t);

    for (int i = 0; i < t; i++) {
        scanf("%d", &n);
        a.resize(2 * n - 1);
        for (int x = 0; x < 2 * n - 1; x++) {
            a[x].resize(n);
            for (int y = 0; y < n; y++) {
                scanf("%d", &a[x][y]);
            }
        }
        printf("Case #%d: ", i + 1);
        solve();
    }
    return 0;
}