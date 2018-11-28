#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
#include <climits>
using namespace std;
#define PB push_back
#define MP make_pair
#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

int t, n, m, h[128][128], C[128], R[128];

void solve() {
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            scanf("%d", &h[i][j]);
    for (int i = 0; i < n; ++i) {
        R[i] = 0;
        for (int j = 0; j < m; ++j) {
            R[i] = max(R[i], h[i][j]);
        }
    }
    for (int j = 0; j < m; ++j) {
        C[j] = 0;
        for (int i = 0; i < n; ++i) {
            C[j] = max(C[j], h[i][j]);
        }
    }
    bool ok = true;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (min(R[i], C[j]) != h[i][j])
                ok = false;
        }
    }
    printf("Case #%d: %s\n", ++t, ok ? "YES" : "NO");
}

int main() {
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        solve();
    }
    return 0;
}
