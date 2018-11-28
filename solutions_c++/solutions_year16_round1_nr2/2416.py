#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <map>
#include <string>
#include <cstdlib>
#include <limits>
#include <algorithm>
#include <cstring>
#include <cassert>
using namespace std;

const int maxn = 60;
vector<vector<int> > matrix;
vector<vector<int> > g;
vector<int> cur_stck, answer;

bool ans_founded = false;

bool check(int n)
{
    answer.clear();
    answer.resize(n, 0);
    vector<int> vt;
    for (int i = 0; i < 2 * n - 1; i++)
        if (find(cur_stck.begin(), cur_stck.end(), i) == cur_stck.end())
            vt.push_back(i);

    sort(vt.begin(), vt.end(), [](int first, int last) {return matrix[first][0] < matrix[last][0]; });

    int lefted = -1, offs = 0;
    for (int i = 0; i < n; i++)
    {
        if (i + offs < vt.size() && matrix[vt[i + offs]][0] != matrix[cur_stck[0]][i])
        {
            if (lefted != -1)
                return false;
            lefted = i;
            offs = -1;
        }
    }
    offs = 0;
    if (lefted == -1)
        lefted = n - 1;
    for (int i = 0; i < n; i++)
    {
        if (i == lefted)
        {
            offs = -1;
            continue;
        }
        if (i > 0)
        {
            for (int rw = 0; rw < n; rw++)
            {
                if (i - 1 != lefted && matrix[vt[i + offs]][rw] <= matrix[vt[i - 1 + offs]][rw])
                    return false;
                else if (i - 1 == lefted && matrix[vt[i + offs]][rw] <= matrix[cur_stck[rw]][i - 1])
                    return false;

                if (matrix[vt[i + offs]][rw] != matrix[cur_stck[rw]][i])
                    return false;
            }
        }
        if (i < n - 1)
        {
            for (int rw = 0; rw < n; rw++)
            {
                if (i + 1 != lefted && matrix[vt[i + offs]][rw] >= matrix[vt[i + 1 + offs]][rw])
                    return false;
                else if (i + 1 == lefted && matrix[vt[i + offs]][rw] >= matrix[cur_stck[rw]][i + 1])
                    return false;
                if (matrix[vt[i + offs]][rw] != matrix[cur_stck[rw]][i])
                    return false;
            }
        }
    }

    for (int i = 0; i < n; i++)
        answer[i] = matrix[cur_stck[i]][lefted];

    return true;
}
void dfs(int vertex, int n, int len = 1)
{
    cur_stck.push_back(vertex);
    if (len == n)
    {
        if (check(n))
            ans_founded = true;
        cur_stck.pop_back();
        return;
    }
    for (int i = 0; i < (int)g[vertex].size(); i++)
    {
        dfs(g[vertex][i], n, len + 1);
        if (ans_founded)
            return;
    }
    cur_stck.pop_back();
}

void solve()
{
    matrix.clear();
    g.clear();
    cur_stck.clear();
    answer.clear();
    ans_founded = false;

    int n, f, tn;
    cin >> n;

    tn = 2 * n - 1;

    matrix.resize(tn, vector<int>(n, 0));
    g.resize(tn, vector<int>());

    for (int i = 0; i < tn; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> f;
            matrix[i][j] = f;
        }
    }

    bool is_ok;
    for (int i = 0; i < tn; i++)
    {
        for (int j = 0; j < tn; j++)
        {
            is_ok = true;
            if (i == j)
                continue;

            for (int p = 0; p < n; p++)
            {
                if (matrix[i][p] >= matrix[j][p])
                {
                    is_ok = false;
                    break;
                }
            }

            if (is_ok)
                g[i].push_back(j);
        }
    }

    for (int i = 0; i < tn; i++)
    {
        dfs(i, n);
        if (ans_founded)
            break;
    }
    for (int i = 0; i < n; i++)
        cout << answer[i] << ' ';
    cout << endl;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cout << "Case #" << to_string(i + 1) << ": ";
        solve();
    }


    fclose(stdin);
    fclose(stdout);
    return 0;
}