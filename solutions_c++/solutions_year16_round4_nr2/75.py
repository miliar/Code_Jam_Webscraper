
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

int n, k;
double tmp[222], p[222];
double f[222][222];

#undef int
int main() {
#define int long long
    ios :: sync_with_stdio(0); cin.tie(0);
    cout << (fixed) << setprecision(9);
    int ntest; cin >> ntest;
    FOR(test,1,ntest) {
        int n, k; cin >> n >> k;
        assert(k % 2 == 0);
        FOR(i,1,n) cin >> tmp[i];

        sort(tmp+1, tmp+n+1);

        double ans = 0.0;
        FOR(left,0,k) {
            int right = k - left;

            int cur = 0;
            memset(f, 0, sizeof f);
            FOR(i,1,left) {
                p[++cur] = tmp[i];
            }
            FOR(i,n-right+1,n) {
                p[++cur] = tmp[i];
            }

            f[0][0] = 1;
            FOR(i,0,k-1) {
                FOR(j,0,i) {
                    f[i+1][j+1] += f[i][j] * p[i+1];
                    f[i+1][j] += f[i][j] * (1 - p[i+1]);
                }
            }
            ans = max(ans, f[k][k/2]);
        }

        cout << "Case #" << test << ": " << ans << endl;
    }
}
