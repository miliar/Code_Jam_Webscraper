#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;
#define MP make_pair
#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i) __typeof(i) v=(i)
#define FORE(i,c) for(__typeof(c.begin()) i=(c.begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second
#define SZ(x) (int)(x).size()
#define ALL(c) c.begin(),c.end()
#define ZERO(x) memset(x,0,sizeof(x))

double alg() {
    int n, x, y;
    cin >> n >> x >> y;
    int sum = 0;
    int levs = 0;
    while (sum + 4 * levs + 1 <= n) {
        sum += 4 * levs + 1;
        ++levs;
    }
    x = abs(x);
    if (x + y <= 2 * (levs - 1)) {
        return 1.0;
    }
    if (x + y > 2 * levs) {
        return 0.0;
    }
    if (x == 0) {
        return 0.0;
    }
    int needed = y + 1;
    n -= sum;
    if (n < needed) {
        return 0.0;
    }
    vector<double> dp(2 * levs + 1, 0.0);
    dp[0] = 1;
    for (int i = 0; i < n; ++i) {
        int mn = max(0, i - 2 * levs);
        for (int k = 2 * levs - 1; k >= mn; --k) {
            dp[k + 1] += dp[k] / 2;
            if (k == i - 2 * levs) {
                dp[k + 1] += dp[k] / 2;
                dp[k] = 0;
            } else {
                dp[k] /= 2;
            }
        }
    }
    double p = 0;
    for (int i = 0; i <= n - needed; ++i) {
        p += dp[i];
    }
    return p;
}

int main() {
    ios_base::sync_with_stdio(false);
    int d;
    cin >> d;
    for (int i = 1; i <= d; ++i) {
        cout << "Case #" << i << ": " << fixed << setprecision(9) << alg() << endl;
    }
}
