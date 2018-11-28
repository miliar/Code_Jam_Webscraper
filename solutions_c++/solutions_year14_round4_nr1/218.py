#include <bits/stdc++.h>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; i--)
#define REP(i,a) for(int i=0,_a=(a); i<_a; i++)

#define DEBUG(x) { cout << #x << " = "; cout << (x) << endl; }
#define PR(a,n) { cout << #a << " = "; FOR(_,1,n) cout << a[_] << ' '; cout << endl; }
#define PR0(a,n) { cout << #a << " = "; REP(_,n) cout << a[_] << ' '; cout << endl; }
using namespace std;

int a[10111], n, x;
bool used[10111];

int main() {
    ios :: sync_with_stdio(false);
    int ntest; cin >> ntest;
    FOR(test,1,ntest) {
        int res = 0;
        cin >> n >> x;
        FOR(i,1,n) cin >> a[i];

        sort(a+1, a+n+1);

        memset(used, false, sizeof used);
        FORD(i,n,1) if (!used[i]) {
            used[i] = true;
            ++res;
            FORD(j,i-1,1) if (a[i] + a[j] <= x && !used[j]) {
                used[j] = true;
                break;
            }
        }

        cout << "Case #" << test << ": " << res << endl;
        cerr << test << endl;
    }
    return 0;
}
