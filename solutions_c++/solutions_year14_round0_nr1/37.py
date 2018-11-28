#include <bits/stdc++.h>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; i--)
#define REP(i,a) for(int i=0,_a=(a); i<_a; i++)

#define DEBUG(x) { cout << #x << " = "; cout << (x) << endl; }
#define PR(a,n) { cout << #a << " = "; FOR(_,1,n) cout << a[_] << ' '; cout << endl; }
#define PR0(a,n) { cout << #a << " = "; REP(_,n) cout << a[_] << ' '; cout << endl; }
using namespace std;

int good[22];

int main() {
    ios :: sync_with_stdio(false);
    int ntest; cin >> ntest;
    FOR(test,1,ntest) {
        int r;
        memset(good, 0, sizeof good);
        REP(turn,2) {
            cin >> r;
            FOR(i,1,4) FOR(j,1,4) {
                int a; cin >> a;
                if (r == i) {
                    good[a]++;
                }
            }
        }
        int cnt = 0, save = -1;
        FOR(i,1,16) if (good[i] == 2) {
            ++cnt;
            save = i;
        }

        cout << "Case #" << test << ": ";
        if (cnt == 0) cout << "Volunteer cheated!\n";
        else if (cnt >= 2) cout << "Bad magician!\n";
        else cout << save << endl;
    }
    return 0;
}
