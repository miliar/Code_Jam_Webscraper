#include <iostream>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <queue>
#include <cassert>
#include <map>
#include <set>
#include <ctime>
#include <iomanip>

using namespace std;

#define x first
#define y second
#define mp make_pair
#define pb push_back
#define sz(X) ((int)((X).size()))

const double eps = 1e-10;
const int inf = 1000000000;

const int N = 1000005;
const int mo = 1000000000 + 7;

int x[N], y[N], z[N], xx[N], yy[N], zz[N];
int v[N];
double d[N];

double dis(int i, int j) {
    double dx = x[i] - x[j];
    double dy = y[i] - y[j];
    double dz = z[i] - z[j];
    return sqrt(dx * dx + dy * dy + dz * dz);
}

void work() {
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; ++i) {
        cin >> x[i] >> y[i] >> z[i] >> xx[i] >> yy[i] >> zz[i];
        v[i] = 0;
        d[i] = dis(0, i);
    }
    v[0] = 1;
    double ans = 0;
    while (!v[1]) {
        int j = 0;
        for (int i = 0; i < n; ++i) {
            if (v[i]) continue;
            if (j == 0 || d[i] < d[j]) {
                j = i;
            }
        }
        v[j] = 1;
        ans = max(ans, d[j]);
        for (int i = 0; i < n; ++i) {
            if (v[i]) continue;
            d[i] = min(d[i], dis(j, i));
        }
    }
    printf("%.10f\n", ans);
}

int main()
{
    #ifdef LOCAL_TEST
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; ++i) {
        printf("Case #%d: ", i);
        work();
    }
    return 0;
}
