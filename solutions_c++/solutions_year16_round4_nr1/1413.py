#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

int n, r, p, s;

int p1[3][20], r1[3][20], s1[3][20];
string ans[3][20];
int n1;

void init()
{
    p1[0][0] = 0, r1[0][0] = 0, s1[0][0] = 1;
    p1[1][0] = 1, r1[1][0] = 0, s1[1][0] = 0;
    p1[2][0] = 0, r1[2][0] = 1, s1[2][0] = 0;
    n1 = 1;
}

void solve(int v)
{
    ans[0][n] = "P";
    ans[1][n] = "R";
    ans[2][n] = "S";
    for (int i = n - 1; i >= 0; i--)
    {
        if (ans[0][i + 1] <= ans[1][i + 1])
        {
            ans[0][i] = ans[0][i + 1] + ans[1][i + 1];
        }
        else
        {
            ans[0][i] = ans[1][i + 1] + ans[0][i + 1];
        }
        if (ans[1][i + 1] <= ans[2][i + 1])
        {
            ans[1][i] = ans[1][i + 1] + ans[2][i + 1];
        }
        else
        {
            ans[1][i] = ans[2][i + 1] + ans[1][i + 1];
        }
        if (ans[0][i + 1] <= ans[2][i + 1])
        {
            ans[2][i] = ans[0][i + 1] + ans[2][i + 1];
        }
        else
        {
            ans[2][i] = ans[2][i + 1] + ans[0][i + 1];
        }
    }
    if (p1[v][0] == 1)
    {
        printf("%s\n", ans[0][0].c_str());
    }
    if (r1[v][0] == 1)
    {
        printf("%s\n", ans[1][0].c_str());
    }
    if (s1[v][0] == 1)
    {
        printf("%s\n", ans[2][0].c_str());
    }
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int q;
    scanf("%d", &q);
    for (int t = 1; t <= q; ++t)
    {
        printf("Case #%d: ", t);
        scanf("%d%d%d%d", &n, &r, &p, &s);
        init();
        while (n1 <= n)
        {
            for (int i = 0; i < 3; i++)
            {
                p1[i][n1] = s1[i][n1 - 1] + p1[i][n1 - 1];
                r1[i][n1] = r1[i][n1 - 1] + p1[i][n1 - 1];
                s1[i][n1] = (1 << (n1)) - p1[i][n1] - r1[i][n1];
            }
            n1++;
        }
        bool b = false;
        for (int i = 0; i < 3; i++)
        {
            if (p == p1[i][n] && r == r1[i][n] && s == s1[i][n])
            {
                b = true;
                solve(i);
            }
        }
        if (!b)
        {
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}