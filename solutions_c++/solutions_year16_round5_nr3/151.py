#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
#include <memory.h>
#include <string>
#include <sstream>
#include <cstdlib>
#include <ctime>
#include <cassert>

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;

#define MP make_pair
#define PB push_back
#define FF first
#define SS second

#define FORN(i, n) for (int i = 0; i <  (int)(n); i++)
#define FOR1(i, n) for (int i = 1; i <= (int)(n); i++)
#define FORD(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define FOREACH(i, c) for (typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)

#define MOD 1000000007
#define INF 2000000000

const int MAXN = 1010;
LL x[MAXN], y[MAXN], z[MAXN], d2[MAXN][MAXN], visited[MAXN]; LL trash;

int T, N, S;

LL sq(LL x) {
    return x * x;
}

LL getdist(int i, int j) {
    return sq(x[i]-x[j]) + sq(y[i]-y[j]) + sq(z[i]-z[j]);
}

void dfs(int u, LL x) {
    visited[u] = 1;

    FORN(v, N) {
        if (!visited[v] && d2[u][v] <= x) {
            dfs(v, x);
        }
    }
}

bool check(LL x) {
    memset(visited, 0, sizeof visited);
    dfs(0, x);
    return (visited[1] == 1);
}

void solve() {
    cin >> N >> S;

    FORN(i, N) {
        cin >> x[i] >> y[i] >> z[i] >> trash >> trash >> trash;
    }

    FORN(i, N) {
        FORN(j, N) {
            d2[i][j] = getdist(i, j);
        }
    }

    LL lo = 0; LL hi = 10000000; LL res = -1;

    while (lo <= hi) {
        LL mid = (lo + hi) / 2;

        if (check(mid)) {
            res = mid;
            hi = mid - 1;
        }
        else {
            lo = mid + 1;
        }
    }

    cout << setprecision(12) << sqrt(res) << "\n";
}

int main() {
    scanf("%d", &T);

    for (int tc = 1; tc <= T; tc++) {
        printf("Case #%d: ", tc);
        solve();
    }
    
    return 0;
}
