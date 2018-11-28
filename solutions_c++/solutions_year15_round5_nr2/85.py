
#include <bits/stdc++.h>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; i--)
#define REP(i,a) for(int i=0,_a=(a); i<_a; i++)
#define EACH(it,a) for(__typeof(a.begin()) it = a.begin(); it != a.end(); ++it)

#define DEBUG(x) { cout << #x << " = "; cout << (x) << endl; }
#define PR(a,n) { cerr << #a << " = "; FOR(_,1,n) cerr << a[_] << ' '; cerr << endl; }
#define PR0(a,n) { cout << #a << " = "; REP(_,n) cout << a[_] << ' '; cout << endl; }

#define sqr(x) ((x) * (x))
using namespace std;

int n, k, sum[1011];
struct Seg {
    int l, r;
} a[1011];

int mod(int a, int b) {
    int res = a % b;
    if (res < 0) res += b;
    return res;
}

int main() {
    ios :: sync_with_stdio(false);
    int ntest; cin >> ntest;
    FOR(test,1,ntest) {
        cin >> n >> k;
        FOR(i,1,n-k+1) cin >> sum[i];

        FOR(i,1,k) {
            int nn = 0, ln = 0;
            int cur = 0;
            for(int u = i; u+k <= n; u += k) {
                int diff = sum[u+1] - sum[u];
                cur += diff;

                nn = min(nn, cur);
                ln = max(ln, cur);
            }
            a[i].l = nn;
            a[i].r = ln;
        }
        // xep cac le trai = 0
        int aligned_sum = 0;
        FOR(i,1,k) aligned_sum -= a[i].l;

        int need = (mod(sum[1], k) - mod(aligned_sum, k) + k) % k;
        int biggest = 0;
        FOR(i,1,k) biggest = max(biggest, a[i].r - a[i].l);

        int can = 0;
        FOR(i,1,k) can += biggest - (a[i].r - a[i].l);
        
        int res = biggest;
        if (can < need) ++res;

        cout << "Case #" << test << ": " << res << endl;
    }
    return 0;
}

