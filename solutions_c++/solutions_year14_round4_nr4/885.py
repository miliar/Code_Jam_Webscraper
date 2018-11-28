#include <cmath>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <iostream>
using namespace std;

struct TreeNode
{
    int next[26];
} node[10000 + 10];
int nodeNum;

int clearNode()
{
    memset(node[nodeNum].next, -1, sizeof(node[nodeNum].next));
    return nodeNum++;
}

int n, m, ans, cnt;
char s[10][100];

int divf[10];

void addNode(int index, char *s)
{
    if (*s == 0) return;
    if (node[index].next[*s - 'A'] == -1)
    {
        node[index].next[*s - 'A'] = clearNode();
    }
    addNode(node[index].next[*s - 'A'], s + 1);
}

void dfs(int index)
{
    if (index == m)
    {
        int temp = 0;
        for (int i = 0; i < n; ++i)
        {
            nodeNum = 0;
            clearNode();
            int cntt = 0;
            for (int j = 0; j < m; ++j)
            {
                if (divf[j] == i)
                {
                    addNode(0, s[j]);
                    ++cntt;
                }
            }
            if (cntt == 0)
            {
                nodeNum = 0;
            }
            temp += nodeNum;
        }
        if (temp > ans)
        {
            ans = temp;
            cnt = 1;
        }
        else if (temp == ans)
        {
            ++cnt;
        }
        return;
    }
    for (int i = 0; i < n; ++i)
    {
        divf[index] = i;
        dfs(index + 1);
    }
}

int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t)
    {
        cnt = 0, ans = 0;
        scanf("%d%d", &m, &n);
        for (int i = 0; i < m; ++i)
        {
            scanf("%s", s[i]);
        }
        dfs(0);
        printf("Case #%d: %d %d\n", t, ans, cnt);
    }
    return 0;
}
