#include <stdio.h>
#include <string.h>
#include <map>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

vector<int> sen[20];
int belong[20];
map<string, int> dict;
char s[10000];
int b[3000][2];
int index = 0;

void dfs(int cur, int n, int &ans)
{
    if (cur == n)
    {
        int temp = 0;
        for (int i = 1; i <= index; i++)
        if (b[i][0] * b[i][1] > 0) { temp++; }
        ans = min(ans, temp);
        return;
    }

    int m = sen[cur].size();
    for (int i = 0; i < m; i++)
    {
        b[sen[cur][i]][0]++;
    }
    belong[cur] = 0;
    dfs(cur + 1, n, ans);
    belong[cur] = 1;
    for (int i = 0; i < m; i++)
    {
        b[sen[cur][i]][0]--;
        b[sen[cur][i]][1]++;
    }
    dfs(cur + 1, n, ans);
    for (int i = 0; i < m; i++)
    {
        b[sen[cur][i]][1]--;
    }
}

int main()
{
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small-attempt1.out", "w", stdout);
    int test;
    scanf("%d", &test);
    for (int t = 1; t <= test; t++)
    {
        printf("Case #%d: ", t);
        int n;
        scanf("%d", &n);
        belong[0] = 0;
        belong[1] = 1;gets(s);
        dict.clear();
        index = 0;
        for (int i = 0; i < n; i++)
        {
            sen[i].clear();
            gets(s);
            int l = strlen(s);
            int h = 0;
            while (h < l)
            {
                string temp = "";
                while ((s[h] != ' ') && (h < l)) { temp += s[h++]; }
                h++;
                if (dict.find(temp) == dict.end())
                {
                    dict[temp] = ++index;
                }
                sen[i].push_back(dict[temp]);
            }
        }
        memset(b, 0, sizeof(b));
        int m = sen[0].size();
        for (int i = 0; i < m; i++)
        {
            b[sen[0][i]][0]++;
        }
        m = sen[1].size();
        for (int i = 0; i < m; i++)
        {
            b[sen[1][i]][1]++;
        }
        int ans = 1e9;
        dfs(2, n, ans);
        printf("%d\n", ans);
        fflush(stdout);
    }
    return 0;
}
