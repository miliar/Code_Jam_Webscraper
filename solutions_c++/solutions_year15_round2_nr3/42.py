
#include <bits/stdc++.h>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; i--)
#define REP(i,a) for(int i=0,_a=(a); i<_a; i++)
#define EACH(it,a) for(__typeof(a.begin()) it = a.begin(); it != a.end(); ++it)

#define DEBUG(x) { cout << #x << " = "; cout << (x) << endl; }
#define PR(a,n) { cout << #a << " = "; FOR(_,1,n) cout << a[_] << ' '; cout << endl; }
#define PR0(a,n) { cout << #a << " = "; REP(_,n) cout << a[_] << ' '; cout << endl; }

#define sqr(x) ((x) * (x))
using namespace std;

const int MN = 500111;
int n;
long long d[MN], t[MN];
bool need[MN];

int solve() {
    if (n < 2) return 0;
    
    int res = 10;

    FOR(i,1,n) {
        int cur = 0;
        FOR(j,1,n) if (j != i) {
            long long a = d[i], b = d[j];
            long long ta = t[i], tb = t[j];

            if ((360LL - a) * ta >= (360LL - b) * tb) {
                // B finish 1 lap first --> need to see if required to pass A
                FOR(t,2,12)
                    if ((360LL*t - b) * tb <= (360LL - a) * ta) ++cur;
            }
            else {
                ++cur;
            }
        }
        res = min(res, cur);
    }
    return res;
}

int main() {
    ios :: sync_with_stdio(false);
    int ntest; cin >> ntest;
    FOR(test,1,ntest) {
        int nGroup; cin >> nGroup;
        n = 0;
        FOR(i,1,nGroup) {
            int cur_d, cur_h, cur_m; cin >> cur_d >> cur_h >> cur_m;
            while (cur_h--) {
                ++n;
                d[n] = cur_d;
                t[n] = cur_m;
                ++cur_m;
            }
        }

        printf("Case #%d: %d\n", test, solve());
    }
    return 0;
}

