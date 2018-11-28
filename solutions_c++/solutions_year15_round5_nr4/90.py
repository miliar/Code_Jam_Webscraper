
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

#define TWO(X) (1<<(X))
#define CONTAIN(S,X) (S & TWO(X))

int p;
int n;
long long a[111], e[10111], f[10111];

int main() {
    ios :: sync_with_stdio(false);
    int ntest; cin >> ntest;
    FOR(test,1,ntest) {
        cin >> p;
        multiset<long long> all;
        FOR(i,1,p) cin >> e[i];
        FOR(i,1,p) {
            cin >> f[i];
            while (f[i]--) all.insert(e[i]);
        }

        int t = all.size();
        n = 0;
        while (t % 2 == 0) {
            ++n;
            t /= 2;
        }

        all.erase(all.find(0));
        REP(i,n) {
            a[i] = *all.begin();
            if (i == 0) all.erase(all.begin());
            if (i > 0) {
                REP(mask,TWO(i)) {
                    long long sum = 0;
                    REP(j,i) if (CONTAIN(mask,j)) sum += a[j];

                    all.erase(all.find(sum + a[i]));
                }
            }
        }
        cout << "Case #" << test << ": ";
        REP(i,n) cout << a[i] << ' '; cout << endl;
        cerr << test << endl;
    }
    return 0;
}

