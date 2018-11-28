#include <cassert>
#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <climits>
#include <cstddef>
#include <cctype>
#include <cmath>
#include <cstring>
#include <fstream>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <numeric>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <vector>
#include <bitset>
#include <list>
#include <string>
#include <functional>
#include <utility>
using namespace std;
typedef long long llint;
int const M = 8;
int const N = 4;
int const L = 10;
int m, n;
char words[M][L + 10];
int a[M];
int cnt[N];
void readin()
{
    scanf("%d%d", &m, &n);
    for (int i = 0; i < m; ++i)
    {
        scanf("%s", words[i]);
    }
}
void gao(int &ans, int &num_ways)
{
    for (int i = 0; i < n; ++i)
    {
        if (cnt[i] == 0)
        {
            return;
        }
    }
    vector <set <string> > tries(n);
    for (int i = 0; i < m; ++i)
    {
        string buff = "";
        for (int j = 0; words[i][j]; ++j)
        {
            buff.push_back(words[i][j]);
            tries[a[i]].insert(buff);
        }
    }
    int cur = 0;
    for (int i = 0; i < n; ++i)
    {
        cur += tries[i].size() + 1;
    }
    if (cur > ans)
    {
        ans = cur;
        num_ways = 1;
    }
    else if (cur == ans)
    {
        ++num_ways;
    }
}
void dfs(int pos, int &ans, int &num_ways)
{
    if (pos == m)
    {
        gao(ans, num_ways);
        return;
    }
    for (int i = 0; i < n; ++i)
    {
        a[pos] = i;
        ++cnt[i];
        dfs(pos + 1, ans, num_ways);
        --cnt[i];
    }
}
pair <int, int> solve()
{
    int ans = -1, num_ways = 0;
    dfs(0, ans, num_ways);
    return make_pair(ans, num_ways);
}
int main()
{
    int tc;
    scanf("%d", &tc);
    for (int cc = 1; cc <= tc; ++cc)
    {
        readin();
        pair <int, int> ans = solve();
        printf("Case #%d: %d %d\n", cc, ans.first, ans.second);
    }
    return 0;
}
