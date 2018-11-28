// vim:set sw=4 et smarttab:
// Round 2 2016

#include <cstdio>
#include <vector>
#include <list>
#include <algorithm>
#include <utility>

typedef std::pair<int, int> pi;

int n;
std::vector<std::list<int>> adj;
std::vector<std::list<int>> rev_adj;
std::vector<bool> visit_a;
std::vector<bool> visit_b;
int edge_count;

pi dfs(int u);

pi dfs_b(int v)
{
    visit_b[v] = true;
    pi ret(0, 1);
    for (auto const &u : rev_adj[v])
    {
        if (!visit_a[u])
        {
            pi t = dfs(u);
            ret.first += t.first;
            ret.second += t.second;
        }
    }
    return ret;
}

pi dfs(int u)
{
    visit_a[u] = true;
    pi ret(1, 0);
    for (auto const &v : adj[u])
    {
        ++edge_count;
        if (!visit_b[v])
        {
            pi t = dfs_b(v);
            ret.first += t.first;
            ret.second += t.second;
        }
    }
    return ret;
}

int select(const std::vector<pi> &v, std::vector<pi> &selected, std::vector<pi> &not_selected, int a, int b, int st)
{
    if (st == (int)v.size())
    {
        if (selected.empty() || a != b)
            return n * n;
        int ret = 0;
        for (auto const &p : selected)
            ret += p.first * (b - p.second);
        std::vector<pi> temp1;
        std::vector<pi> temp2;
        if (!not_selected.empty())
            ret += select(not_selected, temp1, temp2, 0, 0, 0);
        return ret;
    }
    not_selected.push_back(v[st]);
    int ret1 = select(v, selected, not_selected, a, b, st + 1);
    not_selected.pop_back();
    selected.push_back(v[st]);
    int ret2 = select(v, selected, not_selected, a + v[st].first, b + v[st].second, st + 1);
    selected.pop_back();
    return std::min(ret1, ret2);
}

int solve()
{
    int ret = 0;
    std::vector<pi> v;
    visit_a.clear();
    visit_a.resize(n);
    visit_b.clear();
    visit_b.resize(n);
    for (int i = 0; i < n; ++i)
        if (!visit_a[i])
        {
            edge_count = 0;
            pi t = dfs(i);
            v.push_back(t);
            ret += t.first * t.second - edge_count;
        }
    for (int j = 0; j < n; ++j)
        if (!visit_b[j])
            v.push_back(pi(0, 1));
    std::vector<pi> temp1;
    std::vector<pi> temp2;
    ret += select(v, temp1, temp2, 0, 0, 0);
    return ret;
}

int main()
{
    int ntc;
    scanf("%d", &ntc);
    for (int tc = 1; tc <= ntc; ++tc)
    {
        scanf("%d", &n);
        adj.clear();
        adj.resize(n);
        rev_adj.clear();
        rev_adj.resize(n);
        for (int i = 0; i < n; ++i)
        {
            char temp[30];
            scanf("%s", temp);
            for (int j = 0; j < n; ++j)
                if (temp[j] == '1')
                {
                    adj[i].push_back(j);
                    rev_adj[j].push_back(i);
                }
        }
        int answer = solve();
        printf("Case #%d: %d\n", tc, answer);
    }
}
