
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

double safe_sqrt(double x) {
    return sqrt(max((double)0.0,x));
}
int GI(ll& x) {
    return scanf("%lld", &x);
}

#define TWO(X) (1<<(X))
#define CONTAIN(S,X) (S & TWO(X))

int n;
int can[11][11];
int a[11][11];
char tmp[11][11];

int id[11];
int visited[22];

int check() {
    FOR(i,1,n) id[i] = i;

    do {
        memset(visited, 0, sizeof visited);
        visited[0] = 1;
        queue<int> qu; qu.push(0);

        while (!qu.empty()) {
            int u = qu.front(); qu.pop();
            int i = __builtin_popcount(u);
            if (i == n) continue;

            int worker = id[i+1];
            int good = 0;
            FOR(machine,1,n) if (a[worker][machine] && !CONTAIN(u,machine-1)) {
                int v = u + TWO(machine - 1);
                good = 1;
                if (!visited[v]) {
                    qu.push(v);
                    visited[v] = 1;
                }
            }
            if (!good) return 0;
        }
    } while (next_permutation(id+1, id+n+1));

    return 1;
}

#undef int
int main() {
#define int long long
    ios :: sync_with_stdio(0); cin.tie(0);
    cout << (fixed) << setprecision(9);
    int ntest; cin >> ntest;
    FOR(test,1,ntest) {
        cin >> n;
        FOR(i,1,n) FOR(j,1,n) {
            cin >> tmp[i][j];
            can[i][j] = tmp[i][j] - '0';
        }

        int cost = 1e9;
        REP(mask,TWO(n*n)) {
            int cur = 0, sum = 0;
            FOR(i,1,n) FOR(j,1,n) {
                int need = CONTAIN(mask,cur); ++cur;
                if (need && !can[i][j]) ++sum;

                a[i][j] = can[i][j];
                if (need) a[i][j] = 1;
            }
            if (sum > cost) continue;

            if (check()) {
                cost = sum;
            }
        }
        cout << "Case #" << test << ": " << cost << endl;
    }
}
