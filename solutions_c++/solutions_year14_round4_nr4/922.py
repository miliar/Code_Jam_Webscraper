#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>

using namespace std;

int sta[5][9], len[5];
string s[9];
int m, n;
int result = 0, twice = 0;
bool used[9];

void dfs(int d_n, int last, int tot_use)
{
    if (last == m)
    {
        if (len[d_n] == 0)
            return;
        if (d_n == n - 1)
        {
            if (tot_use != m)
                return;
            int cnt = 0;
            for (int i = 0; i < n; ++i)
            {
                set<string> sss;
                for (int j = 0; j < len[i]; ++j)
                {
                    int idx = sta[i][j];
                    string ss = "";
                    for (int k = 0; k < s[idx].size(); ++k)
                    {
                        ss += s[idx][k];
                        sss.insert(ss);
                    }
                }
                cnt += sss.size() + 1;
            }
            if (cnt > result)
            {
                result = cnt;
                twice = 1;
            }
            else if (cnt == result)
                ++twice;
        }
        else
            dfs(d_n + 1, 0, tot_use);
        return;
    }
    if (!used[last])
    {
        used[last] = true;
        sta[d_n][len[d_n]] = last;
        ++len[d_n];
        dfs(d_n, last + 1, tot_use + 1);
        --len[d_n];
        used[last] = false;
    }
    dfs(d_n, last + 1, tot_use);
}

void Solved(int nT)
{
    cin >> m >> n;
    for (int i = 0; i < m; ++i)
        cin >> s[i];
    result = -1;
    memset(used, false, sizeof(used));
    memset(len, 0, sizeof(len));
    dfs(0, 0, 0);
    printf("Case #%d: %d %d\n", nT, result, twice);
}

int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);

    int T = 1;
    cin >> T;
    for (int nT = 1; nT <= T; ++nT)
    {
        Solved(nT);
    }

    return 0;
}