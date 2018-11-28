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

vector<char> ans;

void dfs(int v, char ch, int n)
{
    if (n == 0)
    {
        ans[v - 1] = ch;
        return;
    }

    if (ch == 'R')
    {
        dfs(2 * v - 1,'R', n - 1);
        dfs(2 * v,'S', n - 1);
    }

    if (ch == 'P')
    {
        dfs(2 * v - 1, 'P', n - 1);
        dfs(2 * v, 'R', n - 1);
    }

    if (ch == 'S')
    {
        dfs(2 * v - 1, 'P', n - 1);
        dfs(2 * v, 'S', n - 1);
    }
}

string foo(vector<char> & v)
{
    string tmp;
    for (int i = 0; i < (int)v.size(); ++i)
    {
        tmp.push_back(v[i]);
    }
    int len = 1;
    for (int len = 1; len <= (int)v.size() / 2; len *= 2)
    {
        for (int i = 0; i < (int)v.size(); i += 2 * len)
        {
            if (tmp.substr(i, len) >  tmp.substr(i + len, len))
            {
                for (int u = 0; u < len; ++u)
                {
                    swap(tmp[i + u], tmp[i + len + u]);
                }
            }
        }
    }
    return tmp;
}

void solve(int num_test = 0)
{
    int n, r, p, s; 
    cin >> n >> r >> p >> s;
    string u("RPS");
    string res;
    int mx = 1 << n;
    for (int i = 0; i < (int)u.size(); ++i)
    {
        ans.resize(mx);
        dfs(1, u[i], n);
        int mr = 0, mp = 0, ms = 0;
        for (int j = 0; j < (int)ans.size(); ++j)
        {
            if (ans[j] == 'R')
                ++mr;
            if (ans[j] == 'P')
                ++mp;
            if (ans[j] == 'S')
                ++ms;
        }

        if (mr == r && mp == p && ms == s)
        {
            string tmp = foo(ans);
            if (res.empty() || tmp < res)
                res = tmp;
        }
    }
    if (res.empty())
        res = "IMPOSSIBLE";
    cout << "Case #" << num_test << ": " << res << endl;
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