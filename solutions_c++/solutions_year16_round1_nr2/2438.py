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

int mp[60][60], n;
int rows[120][60];
bool used[120];
int temp[60];
bool filledRow[60], filledColon[60];

bool check()
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (mp[i][j] == 0)
                continue;
            if (mp[i + 1][j] != 0 && mp[i + 1][j] <= mp[i][j])
                return false;
            if (mp[i][j + 1] != 0 && mp[i][j + 1] <= mp[i][j])
                return false;
        }
    }
    return true;
}

bool fitsInRow(int to, int from)
{
    for (int i = 0; i < n; i++)
    {
        if (mp[to][i] != 0 && mp[to][i] != rows[from][i])
        {
            return false;
        }
    }
    for (int i = 0; i < n; i++)
    {
        temp[i] = mp[to][i];
        mp[to][i] = rows[from][i];
    }
    bool ch = check();
    for (int i = 0; i < n; i++)
    {
        mp[to][i] = temp[i];
    }
    return ch;
}

bool fitsInColon(int to, int from)
{
    for (int i = 0; i < n; i++)
    {
        if (mp[i][to] != 0 && mp[i][to] != rows[from][i])
        {
            return false;
        }
    }
    for (int i = 0; i < n; i++)
    {
        temp[i] = mp[i][to];
        mp[i][to] = rows[from][i];
    }
    bool ch = check();
    for (int i = 0; i < n; i++)
    {
        mp[i][to] = temp[i];
    }
    return ch;
}

void fillInRow(int to, int from)
{
    for (int i = 0; i < n; i++)
    {
        mp[to][i] = rows[from][i];
    }
}

void fillInColon(int to, int from)
{
    for (int i = 0; i < n; i++)
    {
        mp[i][to] = rows[from][i];
    }
}

bool checkAns()
{
    memset(filledRow, false, sizeof(filledRow));
    memset(filledColon, false, sizeof(filledColon));
    for (int i = 0; i < 2 * n - 1; i++)
    {
        bool good = false;
        for (int j = 0; j < n && !good; j++)
        {
            if (!filledRow[j] && fitsInRow(j, i))
            {
                good = true;
            }
        }
        for (int j = 0; j < n && !good; j++)
        {
            if (!filledColon[j] && fitsInColon(j, i))
            {
                good = true;
            }
        }
        if (!good)
            return false;
    }
    return true;
}

int ans[120];

bool rec(int v)
{
    if (v == n)
        return true;
    int tmp[60], tmp2[60];
    int num = -1, num2 = -1, cnt = 0;
    int val = 3000;
    for (int i = 0; i < 2 * n - 1; i++)
    {
        if (!used[i] && (val == rows[i][v]))
        {
            num2 = i;
            cnt++;
        }
        if (!used[i] && (val > rows[i][v]))
        {
            val = rows[i][v];
            num = i;
            cnt = 1;
        }
    }
    if (cnt == 0)
        return false;
    if (cnt == 1)
    {
        if (fitsInRow(v, num))
        {
            ans[num] = v;
            for (int i = 0; i < n; i++)
            {
                tmp[i] = mp[v][i];
            }
            fillInRow(v, num);
            used[num] = true;
            if (rec(v + 1))
            {
                return true;
            }
            used[num] = false;
            for (int i = 0; i < n; i++)
            {
                mp[v][i] = tmp[i];
            }
        }
        if (fitsInColon(v, num))
        {
            ans[num] = n + v;
            for (int i = 0; i < n; i++)
            {
                tmp[i] = mp[i][v];
            }
            fillInColon(v, num);
            used[num] = true;
            if (rec(v + 1))
            {
                return true;
            }
            used[num] = false;
            for (int i = 0; i < n; i++)
            {
                mp[i][v] = tmp[i];
            }
        }
        return false;
    }
    if (fitsInRow(v, num) && fitsInColon(v, num2))
    {
        ans[num] = v;
        ans[num2] = n + v;
        for (int i = 0; i < n; i++)
        {
            tmp[i] = mp[v][i];
            tmp2[i] = mp[i][v];
        }
        fillInRow(v, num);
        fillInColon(v, num2);
        used[num] = used[num2] = true;
        if (rec(v + 1))
        {
            return true;
        }
        used[num] = used[num2] = false;
        for (int i = 0; i < n; i++)
        {
            mp[v][i] = tmp[i];
            mp[i][v] = tmp2[i];
        }
    }
    swap(num, num2);
    if (fitsInRow(v, num) && fitsInColon(v, num2))
    {
        ans[num] = v;
        ans[num2] = n + v;
        for (int i = 0; i < n; i++)
        {
            tmp[i] = mp[v][i];
            tmp2[i] = mp[i][v];
        }
        fillInRow(v, num);
        fillInColon(v, num2);
        used[num] = used[num2] = true;
        if (rec(v + 1))
        {
            return true;
        }
        used[num] = used[num2] = false;
        for (int i = 0; i < n; i++)
        {
            mp[v][i] = tmp[i];
            mp[i][v] = tmp2[i];
        }
    }
    return false;
}


void solve()
{
    memset(used, false, sizeof(used));
    memset(mp, 0, sizeof(mp));
    memset(filledRow, false, sizeof(filledRow));
    memset(filledColon, false, sizeof(filledColon));
    rec(0);
    for (int i = 0; i < 2 * n - 1; i++)
    {
        if (ans[i] < n)
        {
            fillInRow(ans[i], i);
            filledRow[ans[i]] = true;
        }
        else
        {
            fillInColon(ans[i] - n, i);
            filledColon[ans[i] - n] = true;
        }
    }
    for (int i = 0; i < n; i++)
    {
        if (!filledRow[i])
        {
            for (int j = 0; j < n; j++)
            {
                printf(" %d", mp[i][j]);
            }
            printf("\n");
            return;
        }
        if (!filledColon[i])
        {
            for (int j = 0; j < n; j++)
            {
                printf(" %d", mp[j][i]);
            }
            printf("\n");
            return;
        }
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
        printf("Case #%d:", t);
        scanf("%d", &n);
        for (int i = 0; i < 2 * n - 1; ++i)
        {
            for (int j = 0; j < n; j++)
            {
                scanf("%d", &rows[i][j]);
            }
        }
        solve();
    }
    return 0;
}