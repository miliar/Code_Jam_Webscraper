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
int main() {
    ios_base::sync_with_stdio(0);
#ifdef TASK
    //freopen(TASK".in","rt",stdin);
    freopen("/Users/ramis/Downloads/A-large.in.txt","rt",stdin);
    freopen(TASK".out","wt",stdout);
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
#define LL long long
#define int long long
#define mp(a,b) make_pair(a,b)
#define INF 2305843009213693951LL
#define MOD 1000000007
#define EPS 1E-8
#define N 1000002
/* --------- END TEMPLATE CODE --------- */
int n, k;
char s[N];

void smain() {
    cin >> n;
    for (int cas = 1; cin >> s >> k; ++cas) {
        n = strlen(s);
        int res = 0;
        for (int i = 0; i + k <= n; ++i) if (s[i] == '-') {
            res += 1;
            for (int j = i; j < i + k; ++j) s[j] = s[j] == '-' ? '+' : '-';
        }
        forn(i, n) if (s[i] == '-') res = -1;
        cout << "Case #" << cas << ": " << (res == -1 ? "IMPOSSIBLE" : to_string(res)) << '\n';

    }
}

