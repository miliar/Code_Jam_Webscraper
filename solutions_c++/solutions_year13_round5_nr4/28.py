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

typedef long double LD;

LD dp[1 << 20];
bool vis[1 << 20];

int n;

LD calc(int mask) {
    if (vis[mask]) {
        return dp[mask];
    }
    vis[mask] = true;
    dp[mask] = 0;
    for (int i = 0; i < n; ++i) {
        int c = i;
        int cur = n;
        while ((mask >> c) & 1) {
            --cur;
            c = (c + 1) % n;
        }
        dp[mask] += (calc(mask ^ (1 << c)) + cur);
    }
    return dp[mask] /= n;
}

void alg() {
    string s;
    cin >> s;
    n = (int) s.size();
    ZERO(vis);
    int mask = 0;
    for (int i = 0; i < n; ++i) {
        if (s[i] == 'X') {
            mask |= 1 << i;
        }
    }
    vis[(1 << n) - 1] = true;
    dp[(1 << n) - 1] = 0;
    cout << fixed << setprecision(15);
    cout << calc(mask) << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    int d;
    cin >> d;
    for (int i = 1; i <= d; ++i) {
        cout << "Case #" << i << ": ";
        alg();
    }
}
