
#include <bits/stdc++.h>
#define int long long
#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; ++i)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; --i)
#define REP(i,a) for(int i=0,_a=(a); i < _a; ++i)

#define DEBUG(X) { cout << #X << " = " << (X) << endl; }
#define PR(A,n)  { cout << #A << " = "; FOR(_,1,n) cout << A[_] << ' '; cout << endl; }
#define PR0(A,n) { cout << #A << " = "; REP(_,n) cout << A[_] << ' '; cout << endl; }

#define sqr(x) ((x) * (x))
#define ll long long
#define __builtin_popcount __builtin_popcountll
#define SZ(x) ((int) (x).size())
using namespace std;

#undef int
int main() {
#define int long long
    ios :: sync_with_stdio(0); cin.tie(0);
    cout << (fixed) << setprecision(9);
    int ntest; cin >> ntest;
    FOR(test,1,ntest) {
        cout << "Case #" << test << ": ";
        int i; cin >> i;
        if (i == 0) {
            cout << "INSOMNIA" << endl;
            continue;
        }
        int mask = 0;
        for(int x = i; ; x += i) {
            int u = x;
            while (u > 0) {
                mask |= 1<< (u % 10);
                u /= 10;
            }

            if (mask == (1<<10)-1) {
                cout << x << endl;
                break;
            }
        }
    }
}
