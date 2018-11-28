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

const int N = 1005;

int n, S;

int x[N], y[N], z[N];

int vx[N], vy[N], vz[N];

inline double sqr(double x) { return x * x; }

inline double dis(int a, int b) {
    return sqrt(sqr(x[a] - x[b]) + sqr(y[a] - y[b]) + sqr(z[a] - z[b]));
}

int F[N];

int findrt(int x) {
    return F[x] == x ? x : F[x] = findrt(F[x]);
}

void unite(int u, int v) {
    F[findrt(u)] = findrt(v);
}

bool check(double m) {
    for(int i = 0; i < n; ++ i) F[i] = i;
    for(int i = 0; i < n; ++ i) {
        for(int j = i + 1; j < n; ++ j) {
            if(dis(i, j) <= m)
                unite(i, j);
        }
    }
    return findrt(0) == findrt(1);
}

int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; ++ cas) {
        scanf("%d%d", &n, &S);
        for(int i = 0; i < n; ++ i) {
            scanf("%d%d%d%d%d%d", x + i, y + i, z + i, vx + i, vy + i, vz + i);
        }
        double l = 0, r = 1e9;
        for(int i = 0; i < 60; ++ i) {
            double m = (l + r) / 2;
            check(m) ? r = m : l = m;
        }
        printf("Case #%d: %.10f\n", cas, r);
    }
    return 0;
}
