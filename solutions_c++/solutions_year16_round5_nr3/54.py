#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
#define sz(c) (int)(c).size()
#define ALL(c) (c).begin(), (c).end()

struct dsu
{
    int n;
    vi par;
    vi rk;

    dsu (int n_)
    {
        n = n_;
        par.resize(n);
        iota(ALL(par), 0);
        rk.assign(n, 1);
    }

    int group (int x)
    {
        if (par[x] == x)
            return x;
        return par[x] = group(par[x]);
    }

    bool merge (int x, int y)
    {
        x = group(x);
        y = group(y);
        if (x == y)
            return false;

        if (rk[x] > rk[y])
            swap(x, y);
        rk[y] += rk[x];
        par[x] = y;

        return true;
    }
};

typedef double T;
void solve (int n, int test)
{
    int s;
    cin >> s;

    vi x(n), y(n), z(n);
    vi vx(n), vy(n), vz(n);
    for (int i = 0; i < n; i++)
    {
        cin >> x[i] >> y[i] >> z[i];
        cin >> vx[i] >> vy[i] >> vz[i];
    }

    auto dist = [&] (int i, int j) -> T
    {
        int dx = x[i] - x[j], dy = y[i] - y[j], dz = z[i] - z[j];
        return sqrt(dx * dx + dy * dy + dz * dz);
    };

    dsu graph(n);
    vector<pair<T, pair<int, int>>> edges;
    for (int i = 0; i < n; i++)
    for (int j = i + 1; j < n; j++)
        edges.pb(mp(dist(i, j), mp(i, j)));

    sort(ALL(edges));
    for (const auto &e : edges)
    {
        graph.merge(e.second.first, e.second.second);
        if (graph.group(0) == graph.group(1))
        {
            printf("Case #%d: %.12f\n", test, (double)e.first);
            return;
        }
    }

    assert(false);
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
