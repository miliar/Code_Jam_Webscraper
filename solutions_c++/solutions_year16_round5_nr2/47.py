#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
#define sz(c) (int)(c).size()
#define ALL(c) (c).begin(), (c).end()

int dfs (int x, const vvi &sons, vi &subtree)
{
    int ans = 1;
    for (int dest : sons[x])
        ans += dfs(dest, sons, subtree);
    return subtree[x] = ans;
}

void solve (int n, int test)
{
    vi par(n);
    vvi g(n);
    for (int i = 0; i < n; i++)
    {
        cin >> par[i];
        --par[i];
        if (par[i] != -1)
            g[par[i]].pb(i);
    }

    vi subtree(n);
    for (int i = 0; i < n; i++)
    if (par[i] == -1)
        dfs(i, g, subtree);

    string code;
    cin >> code;

    int m;
    cin >> m;

    vector<string> words(m);
    for (int i = 0; i < m; i++)
        cin >> words[i];

    const int iters = 5000;
    mt19937 rng(24);

    vi cnt(m);

    for (int it = 0; it < iters; it++)
    {
        set<int> can_first;

        for (int i = 0; i < n; i++)
        if (par[i] == -1)
            can_first.insert(i);

        string res;
        for (int i = 0; i < n; i++)
        {
            int sum = 0;
            for (int x : can_first)
                sum += subtree[x];

            assert(sum >= 1);
            int pos = rng() % sum;

            int nx = -1;
            for (int x : can_first)
            {
                pos -= subtree[x];
                if (pos < 0)
                {
                    res += code[x];
                    nx = x;
                    break;
                }
            }

            assert(pos < 0 && nx != -1);
            can_first.erase(nx);
            for (int dest : g[nx])
                can_first.insert(dest);
        }

        for (int i = 0; i < m; i++)
            cnt[i] += (res.find(words[i]) != string::npos);
    }

    printf("Case #%d:", test);
    for (int i = 0; i < m; i++)
        printf(" %.2f", (double)cnt[i] / (double)iters);
    printf("\n");
}

int main()
{
    #ifndef ONLINE_JUDGE
    freopen("output.txt", "w", stdout);
    freopen("input.txt", "rt", stdin);
    #endif // ONLINE_JUDGE

    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    int test = 1;
    int n;
    while (cin >> n)
        solve(n, test), test++;
}
