#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
#define sz(c) (int)(c).size()
#define ALL(c) (c).begin(), (c).end()

typedef long double T;

T work (const vector<T> &what)
{
    int k = sz(what);
    assert(k % 2 == 0);

    vector<vector<T>> dp(k + 1, vector<T>(k + 1));
    dp[0][0] = 1.0;
    for (int i = 0; i < k; i++)
    for (int j = 0; j <= i; j++)
    {
        dp[i + 1][j + 1] += dp[i][j] * what[i];
        dp[i + 1][j] += dp[i][j] * (1.0 - what[i]);
    }

    return dp[k][k / 2];
}

void solve (int n, int test)
{
    vector<T> p(n);

    int k = 200;
    cin >> k;

    for (int i = 0; i < n; i++)
    {
        double curp;
        cin >> curp;
        p[i] = curp;
    }

    sort(ALL(p));

    T ans = 0;
    for (int fst = 0; fst <= k; fst++)
    {
        int lst = k - fst;
        vector<T> what;
        for (int i = 0; i < fst; i++)
            what.pb(p[i]);
        for (int i = 1; i <= lst; i++)
            what.pb(p[n - i]);
        ans = max(ans, work(what));
    }

    printf("Case #%d: %.15f\n", test, (double)ans);
}

int main()
{
    #ifndef ONLINE_JUDGE
    freopen("output.txt", "w", stdout);
    freopen("input.txt", "rt", stdin);
    #endif // ONLINE_JUDGE

   // ios_base::sync_with_stdio(false);
   // cin.tie(0);

    int t;
    cin >> t;

    int n = 200, test = 1;
    while (cin >> n)
        solve(n, test), test++;
}
