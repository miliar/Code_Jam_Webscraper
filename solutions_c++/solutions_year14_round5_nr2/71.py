#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
#define MP make_pair
#define F first
#define S second

pii get(int hp, int p, int q)
{
    pii res(10000, 0);
    for (int cq = 0; cq <= 10; cq++)
    {
        if (cq * q >= hp)
            continue;
        int rem = hp - cq * q;
        int cp = rem / p;
        if (rem % p)
            cp++;
        if (res.S - res.F < cq - cp)
            res = pii(cp, cq);
    }
    return res;
}

const int INF = (int)1e9;
const int CNT = 111;
const int SUM = 2222;

int dp[CNT][SUM];

void solve(int test)
{
    int p, q, n;
    cin >> p >> q >> n;
    vector<int> h(n);
    vector<int> g(n);
    for (int i = 0; i < n; i++)
        cin >> h[i] >> g[i];
    vector<int> me(n);
    vector<int> tower(n);
    for (int i = 0; i < n; i++)
    {
        pii cur = get(h[i], p, q);
        me[i] = cur.F;
        tower[i] = cur.S;
    }
    for (int i = 0; i <= n; i++)
        for (int s = 0; s < SUM; s++)
            dp[i][s] = -INF;
    dp[0][1] = 0;
    for (int pos = 0; pos < n; pos++)
        for (int s = 0; s < SUM; s++)
        {
            if (dp[pos][s] == -INF)
                continue;
            int delta = tower[pos] - me[pos];
            //shoot it
            if (s + delta >= 0)
                dp[pos + 1][s + delta] = max(dp[pos + 1][s + delta], dp[pos][s] + g[pos]);
            //ingore it
            int add = h[pos] / q + (h[pos] % q ? 1 : 0);
            dp[pos + 1][s + add] = max(dp[pos + 1][s + add], dp[pos][s]);
        }
    int res = 0;
    for (int s = 0; s < SUM; s++)
        res = max(res, dp[n][s]);
    cout << "Case #" << test << ": ";
    cout << res << "\n";
}

int main()
{
    ios_base::sync_with_stdio(0);
    cout.setf(ios::fixed);
    cout.precision(12);
    cerr.setf(ios::fixed);
    cerr.precision(12);
    cin.tie(nullptr);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin >> t;
    for (int q = 1; q <= t; q++)
        solve(q);

    return 0;
}
