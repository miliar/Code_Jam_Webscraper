#include <bits/stdc++.h>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; i--)
#define REP(i,a) for(int i=0,_a=(a); i<_a; i++)

#define DEBUG(x) { cout << #x << " = "; cout << (x) << endl; }
#define PR(a,n) { cout << #a << " = "; FOR(_,1,n) cout << setw(5) << a[_] << ' '; cout << endl; }
#define PR0(a,n) { cout << #a << " = "; REP(_,n) cout << a[_] << ' '; cout << endl; }
using namespace std;

const int MN = 1011;
double a[MN], b[MN];
int n;

bool check(int k) {
    int j = 0;
    FOR(i,k+1,n) {
        ++j;
        if (a[i] < b[j]) return false;
    }
    return true;
}

int main() {
    ios :: sync_with_stdio(false);
    int ntest; cin >> ntest;
    FOR(test,1,ntest) {
        cin >> n;
        FOR(i,1,n) cin >> a[i];
        FOR(i,1,n) cin >> b[i];
        sort(a+1, a+n+1);
        sort(b+1, b+n+1);

        cout << "Case #" << test << ": ";
        FOR(k,0,n) if (check(k)) {
            cout << n - k << ' ';
            break;
        }
        int cnt = 0;
        set<double> allb;
        FOR(i,1,n) allb.insert(b[i]);

        FOR(i,1,n) {
            if (!allb.empty()) {
                __typeof(allb.begin()) it = allb.upper_bound(a[i]);
                if (it != allb.end()) {
                    allb.erase(it);
                    continue;
                }
            }
            ++cnt;
        }
        cout << cnt << endl;
    }
    return 0;
}
