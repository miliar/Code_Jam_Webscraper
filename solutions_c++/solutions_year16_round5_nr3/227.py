#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cassert>
#include <cmath>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <cstdlib>

using namespace std;

#define TASKNAME ""

void solve(int test_number);

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.setf(ios::fixed);
    cout.precision(9);
    cerr.setf(ios::fixed);
    cerr.precision(3);
#ifdef LOCAL
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
#else
#endif
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        solve(i);
    }
}

const int MAX_N = 1005;

struct point {
    int x, y, z;

    point(int x = 0, int y = 0, int z = 0): x(x), y(y), z(z) {}
};

int n, s;
point p[MAX_N];
vector<int> e[MAX_N];

long long sq(int x) {
    return (long long)x * x;
}

bool possible(int dist) {
    for (int i = 0; i < n; i++) {
        e[i].clear();
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i != j && sq(p[i].x - p[j].x) + sq(p[i].y - p[j].y) + sq(p[i].z - p[j].z) <= dist) {
                e[i].push_back(j);
            }
        }
    }
    bool vis[MAX_N] = {false};
    int q[MAX_N], size_q = 0;
    q[size_q++] = 0;
    vis[0] = true;
    for (int i = 0; i < size_q; i++) {
        int u = q[i];
        for (int v : e[u]) {
            if (!vis[v]) {
                q[size_q++] = v;
                vis[v] = true;
            }
        }
    }
    return vis[1];
}

void solve(int test_number) {
    cin >> n >> s;
    for (int i = 0; i < n; i++) {
        cin >> p[i].x >> p[i].y >> p[i].z;
        int tmp;
        cin >> tmp >> tmp >> tmp;
    }
    int lo = -1, hi = 1000000000;
    while (lo < hi - 1) {
        int mid = (lo + hi) / 2;
        if (possible(mid)) {
            hi = mid;
        } else {
            lo = mid;
        }
    }
    cout << "Case #" << test_number + 1 << ": " << sqrt(hi) << endl;
}
