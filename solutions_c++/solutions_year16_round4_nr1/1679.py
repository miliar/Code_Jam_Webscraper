#include <algorithm>
#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <map>

using namespace std;

int a[1000111];
int n, m, r, p, s;

void writeAns()
{
    /*
    vector <pair<int, int> > b;
    b.clear();
    */

    for (int i = 1; i <= m; i++)
    {
        /*
        if (a[i * 2 - 1] > a[i * 2])
            swap(a[i * 2 - 1], a[i * 2]);
        */
        if (a[i] == 1) printf("P");
        if (a[i] == 2) printf("R");
        if (a[i] == 3) printf("S");
    }
    //sort(b.begin(), b.end());

    /*
    for (int i = 0; i < b.size(); i++)
        {
            if (b[i].first == 1) printf("P");
            if (b[i].first == 2) printf("R");
            if (b[i].first == 3) printf("S");
            if (b[i].second == 1) printf("P");
            if (b[i].second == 2) printf("R");
            if (b[i].second == 3) printf("S");
        }
    */
    printf("\n");
}

bool rec(int j, int k, int x, int y, int z)
{
    if (j == 0)
    {
        if (x != r ||
            y != p ||
            z != s) return false;
        return true;
    }

    x = y = z = 0;
    for (int i = k; i > 0; i--)
    {
        if (a[i] == 1)
        {
            y++;
            x++;
            a[2 * i - 1] = 1;
            a[2 * i] = 2;
        }
        else
        if (a[i] == 2)
        {
            x++;
            z++;
            if (j < 2)
            {
                a[2 * i - 1] = 2;
                a[2 * i] = 3;
            }
            else
            {
                a[2 * i - 1] = 3;
                a[2 * i] = 2;
            }
        }
        else
        if (a[i] == 3)
        {
            y++;
            z++;
            if (j < 3)
            {
                a[i * 2 - 1] = 1;
                a[i * 2] = 3;
            }
            else
            {
                a[i * 2 - 1] = 3;
                a[i * 2] = 1;
            }
        }
    }

    return rec(j - 1, 2 * k, x, y, z);
}

void solve()
{
    scanf("%d%d%d%d", &n, &r, &p, &s);
    m = 1 << n;

    a[1] = 1;
    if (rec(n, 1, 0, 1, 0))
    {
        writeAns();
        return;
    }
    a[1] = 2;
    if (rec(n, 1, 1, 0, 0))
    {
        writeAns();
        return;
    }
    a[1] = 3;
    if (rec(n, 1, 0, 0, 1))
    {
        writeAns();
        return;
    }

    printf("IMPOSSIBLE\n");
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int cntTests;
    scanf("%d", &cntTests);
    for (int i = 1; i <= cntTests; i++)
    {
        printf("Case #%d: ", i);
        solve();
    }
}
