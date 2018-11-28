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
#include <unordered_map>
#include <iomanip>

using namespace std;

#define x first
#define y second
#define mp make_pair
#define pb push_back
#define sz(X) ((int)((X).size()))

const double eps = 1e-10;
const int inf = 1000000000;

const int N = 205;
const int mo = 1000000000 + 7;

double a[N], f[N][N];
double ans = 0;
int n, m;

double cal(vector<double> b) {
    memset(f, 0, sizeof f);
    f[m][100] = 1;
    for (int j = m - 1; j >= 0; --j)
        for (int k = 0; k <= 200; ++k) {
            if (k - 1 >= 0)
                f[j][k - 1] += f[j + 1][k] * b[j];
            if (k + 1 <= 200)
                f[j][k + 1] += f[j + 1][k] * (1 - b[j]);
    }
    return f[0][100];
}

void work()
{
    cin >> n >> m;
    for (int i = 0; i < n; ++i)
        cin >> a[i];
    sort(a, a + n);
    ans = 0;
    for (int i = 0; i < m; ++i) {
        vector<double> b;
        for (int j = 0; j <= i; ++j)
            b.pb(a[j]);
        for (int j = n - 1; j >= 0; --j) {
            if (sz(b) <= m)
                b.pb(a[j]);
        }
        ans = max(ans, cal(b));
    }
    for (int i = 0; i < n; ++i) {
        vector<double> b;
        for (int j = i; j < n; ++j) {
            if (sz(b) <= m)
                b.pb(a[j]);
        }
        if (sz(b) == m)
            ans = max(ans, cal(b));
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
