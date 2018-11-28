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
using namespace std;

void smain();
int main(){
#ifdef TASK
    // freopen(TASK".in","rt",stdin);
    freopen("/Users/ramis/Downloads/A-large.in.txt","rt",stdin);
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
#define EPS 1E-6
#define N 333
/* --------- END TEMPLATE CODE --------- */

inline int get_mask(int x) {
    int res = 0;
    for (; x > 0; x /= 10) res |= 1 << (x % 10);
    return res;
}

int f(int x) {
    int mask = 0, res = 0;
    for (; mask != (1 << 10) - 1; res += 1) {
        mask |= get_mask((res + 1) * x);
    }
    return res * x;
}


void smain() {
    int n;
    cin >> n;
    for (int cas = 1; cin >> n; ++cas) {
        if (n == 0) {
            cout << "Case #" << cas << ": INSOMNIA" << '\n';
            cerr << "Case #" << cas << ": INSOMNIA" << '\n';
            continue;
        }
        int res = f(n);
        cout << "Case #" << cas << ": " << res << '\n';
        cerr << "Case #" << cas << ": " << res << '\n';
    }
}
