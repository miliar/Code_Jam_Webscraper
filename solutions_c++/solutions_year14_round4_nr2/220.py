#include <bits/stdc++.h>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; i--)
#define REP(i,a) for(int i=0,_a=(a); i<_a; i++)

#define DEBUG(x) { cout << #x << " = "; cout << (x) << endl; }
#define PR(a,n) { cout << #a << " = "; FOR(_,1,n) cout << a[_] << ' '; cout << endl; }
#define PR0(a,n) { cout << #a << " = "; REP(_,n) cout << a[_] << ' '; cout << endl; }
using namespace std;

int n, a[1011];

int main() {
    ios :: sync_with_stdio(false);
    int ntest; cin >> ntest;
    FOR(test,1,ntest) {
        cin >> n; FOR(i,1,n) cin >> a[i];

        int l = 1, r = n, res = 0;
        while (l + 1 < r) {
            int nn = l;
            FOR(t,l,r) if (a[t] < a[nn]) nn = t;

            int toLeft = nn - l, toRight = r - nn;
            if (toLeft < toRight) {
                FORD(t,nn,l+1) {
                    swap(a[t], a[t-1]);
                    ++res;
                }
                ++l;
            }
            else {
                FOR(t,nn,r-1) {
                    swap(a[t], a[t+1]);
                    ++res;
                }
                --r;
            }
        }
        cout << "Case #" << test << ": " << res << endl;
    }
    return 0;
}
