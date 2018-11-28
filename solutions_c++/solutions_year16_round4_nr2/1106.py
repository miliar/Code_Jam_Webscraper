#include "stdafx.h"

int N, K;
const int MAXN = 16;
double p[MAXN];

const int MAXS = 1 << MAXN;
int S;

double pVotes[MAXS][MAXN+1];

double ans;

double solve()
{
    S = 1 << N;
    ZERO(pVotes);
    ans = 0;
    FOR(n, N)
    {
        int s = 1 << n;
        pVotes[s][0] = 1-p[n];
        pVotes[s][1] = p[n];
        DBG(1, V(s) << V(pVotes[s][1]));
    }
    FOR(s, S)
    {
        int n = __popcnt(s);
        if (n <= 1) continue;
        int s1 = s & (s - 1);
        int s0 = s - s1;
        assertdbg(__popcnt(s0) == 1 && __popcnt(s1) == n-1, V(s)<<V(s0)<<V(s1)<<V(n));
        pVotes[s][0] = pVotes[s1][0] * pVotes[s0][0];
        pVotes[s][n] = pVotes[s1][n-1] * pVotes[s0][1];
        FOR2(i, 1, n) {
            pVotes[s][i] = pVotes[s1][i] * pVotes[s0][0] + pVotes[s1][i-1] * pVotes[s0][1];
        }
        DBG(1, V(s) << V(pVotes[s][n]) << V(pVotes[s][K/2]));
        if (n == K) ans = max(ans, pVotes[s][K / 2]);
    }
    return ans;
}

int main() {
    int T;
    cin >> T;

    FOR(tt, T)
    {
        cout << "Case #" << (tt + 1) << ": ";
        cin >> N >> K;
        FOR(i, N) cin >> p[i];
        //DBG(1, V(N) << V(cnt));
        double ans = solve();
        cout << ans << endl;
    }
    return 0;
}
