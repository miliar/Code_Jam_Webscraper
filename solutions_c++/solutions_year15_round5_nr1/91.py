#include <iostream>
#include <vector>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <iomanip>
#include <algorithm>
#include <utility>

using namespace std;

int n, d;
vector< int > par, sal;
vector< vector< int > > g;
vector< int > used;
int ans, cur;
int from, to;
vector< int > q;

void
add_vertex(int w)
{
    int qt = 0, qh = 0;
    q[qt++] = w;
    while (qh < qt) {
        int v = q[qh++];
        if (!used[v] && from <= sal[v] && sal[v] <= to && (!v || used[par[v]])) {
            used[v] = 1;
            cur++;
            for (auto u : g[v]) {
                q[qt++] = u;
            }
        }
    }
}

void
del_vertex(int w)
{
    int qt = 0, qh = 0;
    q[qt++] = w;
    while (qh < qt) {
        int v = q[qh++];
        if (used[v]) {
            used[v] = 0;
            --cur;
            for (auto u : g[v]) {
                q[qt++] = u;
            }
        }
    }
}

void
process(int id)
{
    cin >> n >> d;
    par.assign(n, 0);
    sal.assign(n, 0);
    int as, cs, rs, am, cm, rm;
    cin >> sal[0] >> as >> cs >> rs;
    cin >> par[0] >> am >> cm >> rm;
    for (int i = 1; i < n; ++i) {
        sal[i] = (1ll * sal[i - 1] * as + cs) % rs;
        par[i] = (1ll * par[i - 1] * am + cm) % rm;
    }
    par[0] = 0;
    g.assign(n, vector< int >());
    for (int i = 1; i < n; ++i) {
        par[i] %= i;
        g[par[i]].push_back(i);
    }
    used.assign(n, 0);
    q.assign(n, 0);
    vector< pair< int, int > > indices(n);
    for (int i = 0; i < n; ++i) {
        indices[i] = make_pair(sal[i], i);
    }
    sort(indices.begin(), indices.end());
    ans = cur = 0;
    int l = 0, r = 0;
    while (l < n) {
        while (r < n && indices[r].first - indices[l].first <= d) {
            // insert vertex
            from = indices[l].first;
            to = from + d;
            add_vertex(indices[r].second);
            ++r;
        }
        ans = max(ans, cur);
        del_vertex(indices[l].second);
        ++l;
    }
    cout << "Case #" << id << ": " << ans << '\n';
}

int
main()
{
    ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        process(i + 1);
    }
    return 0;
}
