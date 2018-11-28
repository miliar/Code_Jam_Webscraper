#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;

#define mp make_pair

typedef long long ll;
typedef pair<int, int> pii;


const int mod = 1e9 + 7;
const int MN = 1e6 + 50;

bool deleted[MN];
bool deleted2[MN];
vector<vector<int>> G;

int ans;

void enable(int v, int p, int mx, vector<int>& s)
{
    if (deleted2[v])
        return;
    if (!deleted[v])
        return;
    if (deleted[p] && v != 0)
        return;
    deleted[v] = false;
    ++ans;
    for (int i = 0; i < G[v].size(); ++i)
    {
        if (deleted[G[v][i]] && s[G[v][i]] <= mx)
            enable(G[v][i], v, mx, s);
    }
}

void disable(int v)
{
    if (deleted2[v])
        return;
    if (!deleted[v])
        --ans;
    deleted2[v] = true;
    for (int i = 0; i < G[v].size(); ++i)
        disable(G[v][i]);
}

void solve()
{
    ans = 0;
    int n, d;
    cin >> n >> d;
    fill(deleted, deleted + n, true);
    fill(deleted2, deleted2 + n, false);
    vector<int> m(n);
    vector<int> s(n);
    int as, cs, rs;
    cin >> s[0] >> as >> cs >> rs;
    int am, cm, rm;
    cin >> m[0] >> am >> cm >> rm;
    for (int i = 1; i < n; ++i)
    {
        s[i] = (s[i - 1] * as + cs) % rs;
        m[i] = (m[i - 1] * am + cm) % rm;
        m[i - 1] %= max((i - 1), 1);
    }
    m[n - 1] %= max(n - 1, 1);
    G = vector<vector<int>>(n);
    for (int i = 1; i < n; ++i)
    {
        G[m[i]].push_back(i);
    }

    vector<pii> order(n);
    for (int i = 0; i < n; ++i)
    {
        order[i] = mp(s[i], i);
    }
    sort(order.begin(), order.end());
    int l = 0;
    int r = 0;

    int ba = 0;
    m[0] = 0;
    for (; r < n; ++r)
    {
        while (l < r && order[l].first < order[r].first - d)
            disable(order[l++].second);
        int v = order[r].second;
        enable(v, m[v], s[v], s);
        ba = max(ba, ans);
    }
    cout << ba;

}

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i)
    {
        cout << "Case #" << i << ": ";
        solve();
        cout << endl;
    }
    return 0;
}