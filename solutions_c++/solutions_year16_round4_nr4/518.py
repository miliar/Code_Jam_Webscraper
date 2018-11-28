#include <iostream>
#include <cstring>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <bitset>
#define _USE_MATH_DEFINES
#include <math.h>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <assert.h>
#include <stdlib.h>
using namespace std;

void smain();
int main(){
#ifdef TASK
    //freopen(TASK".in","rt",stdin);
    freopen("/Users/ramis/Downloads/D-small-attempt0.in.txt","rt",stdin);
    freopen("out.txt","wt",stdout);
    const clock_t start = clock();
#endif
    smain();
#ifdef TASK
    cerr << "\nTotal Execution Time: " << float( clock () - start ) /  CLOCKS_PER_SEC << endl;
#endif
    return 0;
}

#ifndef M_PI
#define M_PI 3.14159265358979311599796346854418516
#endif
#define forn(i,n) for (int i=0;i<n;i++)
#define rforn(i,n) for (int i=n-1;i>=0;i--)
#define int long long
#define LL long long
#define mp(a,b) make_pair(a,b)
#define INF 2305843009213693951LL
#define MOD 1000000007
#define EPS 1E-9
#define N 5
/* --------- END TEMPLATE CODE --------- */

int n, p[N];
char g[N][N];
bool f[N][N];

inline int bit(int mask, int i, int j) {
    int k = n * i + j;
    return (mask >> k) & 1;
}

bool used[N];
bool dfs(int i) {
    if (i == n) {
        forn(j, n) if (!used[j]) 
            return false;
        return true;
    }
    bool ok = false;
    forn(j, n) if (!used[j] && f[p[i]][j]) {
        ok = true;
        used[j] = 1;
        if (!dfs(i + 1)) return false;
        used[j] = 0;
    }
    return ok;
}

inline bool check(int mask) {
    forn(i, n) p[i] = i;
    forn(i, n) forn(j, n) f[i][j] = bit(mask, i, j);
    //cerr << "-------" << endl;
    //forn(i, n) { forn(j, n) cerr << f[i][j]; cerr << endl;}
    //forn(i, n) { forn(j, n) cerr << char(g[i][j] + '0'); cerr << endl;}
    do {
        memset(used, 0, sizeof(used));
        if (!dfs(0)) return false;
    } while(next_permutation(p, p + n));
    return true;
}

int naive() {
    int res = INF;
    int mm = 1 << (n * n);
    int orig = 0;
    forn(i, n) forn(j, n) if (g[i][j]) orig |= 1 << (n * i + j);
    forn(mask, mm) {
        if ((orig & mask) != orig) continue;
        int val = __builtin_popcount(orig ^ mask);
        if (val >= res) continue;
        if (check(mask)) res = val;
    }
    return res;
}

void smain() {
    cin >> n;
    for (int cas = 1; cin >> n; ++cas) {
        forn(i, n) cin >> g[i];
        forn(i, n) forn(j, n) g[i][j] -= '0';
        int res = naive();
        cout << "Case #" << cas << ": " << res << endl;
        cerr << "Case #" << cas << ": " << res << endl;
    }
}
