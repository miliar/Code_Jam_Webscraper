#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstdint>
#include <cstdio>
#include <algorithm>
#include <bitset>
#include <queue>
using namespace std;

struct my_test
{
    vector<set<int> > q;

    vector<int> cur;

    int w;
    bool find, find_ok;

    void dfs(int p, vector<int> & id)
    {
        if (p >= id.size())
        {
            set<int> t = q[w];
            set<int> tmp;
            bool is = true;
            for (auto & x : cur)
            {
                if (tmp.count(x))
                {
                    is = false;
                }
                tmp.insert(x);
            }
            if (!is)
                return;

            for (auto & x : cur)
            {
                t.erase(x);
            }
            if (t.empty())
                find = true;
            else
                find_ok = true;
            return;
        }
        int id_p = id[p];
        for (auto & x : q[id_p])
        {
            cur[p] = x;
            dfs(p + 1, id);
        }
    }

    bool check(vector<vector<char> > & g)
    {
        int n = g.size();
        q.clear();
        q.resize(n);
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                if (g[i][j])
                    q[i].insert(j);
            }
        }
        int ans = 0;
        for (int i = 0; i < n; ++i)
        {
            vector<int> id;
            for (int j = 0; j < n; ++j)
            {
                if (j == i)
                    continue;
                bool is = false;
                for (auto & x : q[j])
                {
                    if (q[i].count(x))
                        is = true;
                }
                if (is)
                    id.push_back(j);
            }
            w = i;
            cur.clear();
            cur.resize(id.size());
            find = false;
            find_ok = false;
            dfs(0, id);
            if (find == false && find_ok == true)
            {
                ++ans;
            }
        }
        return ans == n;
    }

    int operator()()
    {
        int n;
        cin >> n;
        int ans = n * n;
        vector<string> v(n);
        for (int i = 0; i < n; ++i)
        {
            cin >> v[i];
        }
        int mx = 1 << (n * n);
        for (int mask = 0; mask < mx; ++mask)
        {
            vector<vector<char> > g(n, vector<char>(n));
            int cnt = 0, res = 0;
            bool is = true;
            for (int i = 0; i < n; ++i)
            {
                for (int j = 0; j < n; ++j)
                {
                    if (mask & (1 << cnt))
                    {
                        g[i][j] = true;
                        if (v[i][j] == '0')
                           ++res;
                    }
                    else
                        g[i][j] = false;
                    if (v[i][j] == '1' && g[i][j] == false)
                        is = false;
                    ++cnt;
                }
            }

            if (is)
            {
                if (check(g))
                {
                    ans = min(ans, res);
                }
            }
        }
        return ans;
    }
};

void solve(int num_test = 0)
{
    my_test test;
    printf("Case #%d: %d\n", num_test, test());
}

int main(void)
{
#if 1
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    ios::sync_with_stdio(false);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        solve(i + 1);
    }
    return 0;
}