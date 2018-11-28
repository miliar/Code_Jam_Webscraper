
#include <bits/stdc++.h>
#define int long long
#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; ++i)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; --i)
#define REP(i,a) for(int i=0,_a=(a); i < _a; ++i)

#define DEBUG(X) { cerr << #X << " = " << (X) << endl; }
#define PR(A,n)  { cerr << #A << " = "; FOR(_,1,n) cerr << A[_] << ' '; cerr << endl; }
#define PR0(A,n) { cerr << #A << " = "; REP(_,n) cerr << A[_] << ' '; cerr << endl; }

#define sqr(x) ((x) * (x))
#define ll long long
#define __builtin_popcount __builtin_popcountll
#define SZ(x) ((int) (x).size())
using namespace std;

int GI(int& x) {
    return scanf("%lld", &x);
}

#undef int
int main() {
#define int long long
    ios :: sync_with_stdio(0); cin.tie(0);
    cout << (fixed) << setprecision(9);
    int ntest; cin >> ntest;
    FOR(test,1,ntest) {
        int k, c, s; cin >> k >> c >> s;
        int need = (k + c - 1) / c;

        cout << "Case #" << test << ": ";
        if (need > s) cout << "IMPOSSIBLE" << endl;
        else {
            int start = 1;
            FOR(i,1,need) {
                int u = start;
                FOR(j,start+1,start+c-1) {
                    u = (u-1) * k + min(j,k);
                }
                cout << u << ' ';
                start += c;
            }
            cout << endl;
        }
    }
}
