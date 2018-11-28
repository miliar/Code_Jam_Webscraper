#include <bits/stdc++.h>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; i--)
#define REP(i,a) for(int i=0,_a=(a); i<_a; i++)

#define DEBUG(x) { cout << #x << " = "; cout << (x) << endl; }
#define PR(a,n) { cout << #a << " = "; FOR(_,1,n) cout << a[_] << ' '; cout << endl; }
#define PR0(a,n) { cout << #a << " = "; REP(_,n) cout << a[_] << ' '; cout << endl; }
using namespace std;

const int MN = 1000111;

int n, a[MN];
long long p, q, r, s, sum[MN];

int main() {
    ios :: sync_with_stdio(false);
    int ntest; cin >> ntest;
    cout << (fixed) << setprecision(10);
    FOR(test,1,ntest) {
        cin >> n >> p >> q >> r >> s;

        FOR(i,1,n) {
            a[i] = (((i-1) * p + q) % r + s);
        }
        // PR(a, n);
        FOR(i,1,n) sum[i] = sum[i-1] + a[i];

        long double best = 0.0;
        FOR(b,1,n) {
            int l = 1, r = b, res = 0;
            while (l <= r) {
                int a = (l + r) >> 1;
                if (sum[a] + sum[a] > sum[b]) {
                    r = a - 1;
                }
                else {
                    l = a + 1;
                    res = a;
                }
            }

            FOR(a,max(res-5,1),min(res+5,b)) {
                long long cur = max(sum[a], max(sum[b] - sum[a], sum[n] - sum[b]));
                best = max(best, (sum[n] - cur) / (long double) sum[n]);
            }
        }
        cout << "Case #" << test << ": " << best << endl;
        cerr << test << endl;
    }
    return 0;
}
