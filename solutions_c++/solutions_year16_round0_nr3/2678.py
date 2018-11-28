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
    freopen(TASK".in","rt",stdin);
    //freopen("/Users/ramis/Downloads/B-large.in.txt","rt",stdin);
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
#define N 111
/* --------- END TEMPLATE CODE --------- */

vector<int> check(int x) {
    vector<int> res;
    for (int b = 2; b < 11; ++b) {
        int p = 1, s = 0;
        for (int y = x; y; y >>= 1, p *= b) if (y & 1) s += p;
        int d = 0;
        for (int i = 2; i * i <= s; ++i) if (s % i == 0) {
            d = i; break;
        }
        if (!d) return vector<int>();
        res.push_back(d);
    }
    return res;
}

void solve(int n, int m) {
    int k = n - 2;
    int mm = 1 << k;
    vector<pair<int, vector<int> > > res;
    forn(mask, mm) {
        int val = (((1 << k) + mask) << 1) + 1;
        vector<int> t = check(val);
        if (t.size()) {
            res.emplace_back(val, t);
            if ((int)res.size() == m)
                break;
        }
    }
    for (auto it : res) {
        cout << bitset<16>(it.first);
        for (auto i : it.second) cout << ' ' << i;
        cout << endl;
    }
    for (auto it : res) {
        cerr << bitset<16>(it.first);
        for (auto i : it.second) cerr << ' ' << i;
        cerr << endl;
    }
}

void smain() {
    int n, m;
    cin >> n;
    for (int cas = 1; cin >> n >> m; ++cas) {
        cout << "Case #" << cas << ":" << endl;
        solve(n, m);
        // cerr << "Case #" << cas << ": " << res << endl;
    }
}
