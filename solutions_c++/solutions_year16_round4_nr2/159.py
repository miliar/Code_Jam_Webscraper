// Template {{{
#include <bits/stdc++.h>
#define REP(i,n) for(int i=0; i<(int)(n); ++i)
using namespace std;
typedef long long LL;

#ifdef LOCAL
#include "contest.h"
#else
#define dump(x) 
#endif

const int dx[4] = {1, 0, -1, 0};
const int dy[4] = {0, 1, 0, -1};
inline bool valid(int x, int w) { return 0 <= x && x < w; }

void iostream_init() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.setf(ios::fixed);
    cout.precision(12);
}
//}}}

double calc(const vector<double>& P) {
    const int N = P.size();
    assert(N % 2 == 0);
    const int L = N/2 + 1;
    double dp[2][L];
    double* cur = dp[0];
    double* next = dp[1];
    REP(i, L) cur[i] = 0;
    cur[0] = 1.0;
    REP(i, N) {
        REP(k, L) {
            next[k] = cur[k] * (1 - P[i]) + (k-1 >= 0 ? cur[k-1] * P[i] : 0);
        }
        swap(cur, next);
    }
    return cur[N/2];
}
double small(int N, int K, vector<double> P) {
    double ans = 0;
    int goodS = -1;
    REP(s, 1 << N) if(__builtin_popcount(s) == K) {
        vector<double> dp(N+1);
        dp[0] = 1.0;
        REP(i, N) if(s >> i & 1) {
            vector<double> ndp(N + 1);
            REP(k, N+1) {
                ndp[k] = dp[k] * (1 - P[i]) + (k - 1 >= 0 ? dp[k-1] * P[i] : 0);
            }
            dp.swap(ndp);
        }
        if(ans < dp[K/2]) {
            ans = dp[K/2];
            goodS = s;
        }
    }
    return ans;
}
double large(int N, int K, vector<double> P) {
    sort(P.begin(), P.end());
    vector<double> PS(K);
    double ans = 0;
    for(int A = 0; A <= K; A++) {
        for(int B = 0; A + B <= K; B++) {
            int C = K - A - B;
            const int b = A;
            const int e = N - B - C;
            for(int x = b; x <= e; x++) {
                int idx = 0;
                for(int i = 0; i < A; i++) PS[idx++] = P[i];
                for(int i = x; i < x + B; i++) PS[idx++] = P[i];
                for(int i = N-C; i < N; i++) PS[idx++] = P[i];
                // cout << A << " " << B << " " << C << endl;
                // cout << x << " " << b << " " << e << endl;
                // cout << idx << endl;
                assert(idx == K);
                double opt = calc(PS);
                if(ans < opt){
                    ans = opt;
                }
            }
        }
    }
    // for(int b1 = 0; b1 <= 0; b1++) {
    // for(int e1 = b1; e1 <= N; e1++) {
    // for(int b2 = e1; b2 <= N; b2++) {
    // for(int e2 = b2; e2 <= N; e2++) {
    // for(int b3 = e2; b3 <= N; b3++) {
    // for(int e3 = N; e3 <= N; e3++) {
    //     int cnt = e1 + (e2 - b2) + (e3 - b3);
    //     if(cnt != K) continue;
    //     int idx = 0;
    //     double opt = calc(PS);
    //     if(ans < opt){
    //         ans = opt;
    //     }
    // }}}}}}
    return ans;
}
void solve() {
    int N, K;
    cin >> N >> K;
    vector<double> P(N);
    REP(i, N) {
        cin >> P[i];
    }
    sort(P.begin(), P.end());
    double ans = large(N, K, P);
    cout << ans << endl;
}

int main(){
    iostream_init();
    int T;
    cin >> T;
    REP(casenum, T) {
        cout << "Case #" << casenum + 1 << ": ";
        solve();
    }

    return 0;
}

