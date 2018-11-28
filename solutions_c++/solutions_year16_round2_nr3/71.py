#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
#define sz(c) (int)(c).size()
#define ALL(c) (c).begin(), (c).end()

bool dfs (int x, const vvi &g, vector<char> &used, vi &mt)
{
    if (used[x])   return false;
    used[x] = true;

    for (int dest : g[x])
    if (mt[dest] == -1 || dfs(mt[dest], g, used, mt))
    {
        mt[dest] = x;
        return true;
    }

    return false;
}

void solve (int n, int test)
{
    map<string, int> fst, snd;
    vector<pair<string, string>> v(n);
    for (int i = 0; i < n; i++)
    {
        cin >> v[i].first >> v[i].second;
        if (!fst.count(v[i].first))
        {
            int h = sz(fst);
            fst[v[i].first] = h;
        }
        if (!snd.count(v[i].second))
        {
            int h = sz(snd);
            snd[v[i].second] = h;
        }
    }

    const int left = sz(fst), right = sz(snd);
    vvi g(left);
    for (int i = 0; i < n; i++)
        g[fst[v[i].first]].pb(snd[v[i].second]);

    int not_fake = sz(fst) + sz(snd);
    vector<char> used(left);
    vi mt(right, -1);
    for (int i = 0; i < left; i++)
    {
        fill(ALL(used), 0);
        not_fake -= dfs(i, g, used, mt);
    }

    assert(n >= not_fake && not_fake >= 0);
    printf("Case #%d: %d\n", test, n - not_fake);
}

int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "w", stdout);
    #endif // ONLINE_JUDGE

   // ios_base::sync_with_stdio(false);
   // cin.tie(0);

    int t;
    cin >> t;

    int test = 1;
    int n;
    while (cin >> n)
        solve(n, test), test++;
}
