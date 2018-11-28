#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
#define MP make_pair
#define F first
#define S second

const int N = 16;
const string NO = "CRIME TIME";

bool dp[N][1 << N];

void solve(int test)
{
    int n;
    cin >> n;
    vector<int> was;
    vector<string> t(n);
    vector<int> id(n);
    for (int i = 0; i < n; i++)
    {
        cin >> t[i] >> id[i];
        if (id[i])
            was.push_back(id[i]);
    }
    sort(was.begin(), was.end());
    was.resize(unique(was.begin(), was.end()) - was.begin());
    for (int i = 0; i < n; i++)
        if (id[i])
            id[i] = lower_bound(was.begin(), was.end(), id[i]) - was.begin();
        else
            id[i] = -1;
    cout << "Case #" << test << ": ";
    int cnt = n;
        for (int p = 0; p <= n; p++)
            for (int mask = 0; mask < (1 << cnt); mask++)
                if (p == 0)
                    dp[p][mask] = true;
                else
                    dp[p][mask] = false;
        for (int p = 0; p < n; p++)
            for (int mask = 0; mask < (1 << cnt); mask++)
            {
                if (!dp[p][mask])
                    continue;
                if (t[p] == "E" && id[p] >= 0)
                    if (!(mask & (1 << id[p])))
                        dp[p + 1][mask ^ (1 << id[p])] = true;
                if (t[p] == "L" && id[p] >= 0)
                    if (mask & (1 << id[p]))
                        dp[p + 1][mask ^ (1 << id[p])] = true;
                if (t[p] == "E" && id[p] == -1)
                    for (int b = 0; b < cnt; b++)
                        if (!(mask & (1 << b)))
                            dp[p + 1][mask ^ (1 << b)] = true;
                if (t[p] == "L" && id[p] == -1)
                    for (int b = 0; b < cnt; b++)
                        if (mask & (1 << b))
                            dp[p + 1][mask ^ (1 << b)] = true;
            }
    int res = n + 1;
    for (int mask = 0; mask < (1 << cnt); mask++)
        if (dp[n][mask])
            res = min(res, __builtin_popcount(mask));
    if (res == n + 1)
        cout << NO << "\n";
    else
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
