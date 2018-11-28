#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
#define sz(c) (int)(c).size()
#define ALL(c) (c).begin(), (c).end()

bool rec (int cur, int banned, const vi &can)
{
    if (cur == sz(can))
        return true;

    if ((banned & can[cur]) == can[cur])
        return false;

    bool ans = true;
    int cnt = 0;

    for (int j = 0; j < sz(can); j++)
    if (!((banned >> j) & 1))
    if ((can[cur] >> j) & 1)
    {
        cnt++;
        ans &= rec(cur + 1, banned | (1 << j), can);
        if (!ans)
            return false;
    }

    assert(cnt > 0);

    return ans;
}

bool always (vi can)
{
    const int n = sz(can);
    sort(ALL(can));

    do
    {
        if (!rec(0, 0, can))
            return false;
    }
    while (next_permutation(ALL(can)));
    return true;
}

void solve (int n, int test)
{
    vector<string> inp(n);
    vi can(n);

    for (int i = 0; i < n; i++)
    {
        cin >> inp[i];
        for (int j = 0; j < n; j++)
            can[i] |= ((inp[i][j] - '0') << j);
    }

    const int inf = (int)1e9;
    int ans = inf;
    for (int mask = 0; mask < (1 << (n * n)); mask++)
    {
        vi ncan = can;

        for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
        if ((mask >> (i * n + j)) & 1)
            ncan[i] |= (1 << j);

        if (always(ncan))
            ans = min(ans, __builtin_popcount(mask));
    }

    printf("Case #%d: %d\n", test, ans);
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

    int n, test = 1;
    while (cin >> n)
        solve(n, test), test++;
}
