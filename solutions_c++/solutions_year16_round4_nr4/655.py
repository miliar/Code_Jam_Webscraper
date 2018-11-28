#include <bits/stdc++.h>

using namespace std;

char s[10];
int a[10][10];
int b[10], c[10];
int n, res;
bool found;

void duyet2(int vt)
{
    if (vt == n+1)
        return;
    for(int i=1; i<=n; i++)
    if (b[i] == 0)
    {
        b[i] = 1;
        bool flag = 0;
        for(int j=1; j<=n; j++)
        {
            if (c[j] == 0 && a[i][j] == 1)
            {
                flag = 1;
                c[j] = 1;
                duyet2(vt+1);
                if (found)
                    return;
                c[j] = 0;
            }
        }
        if (!flag)
        {
            found = 1;
            return;
        }
        if (found)
            return;
        b[i] = 0;
    }
}

void ktr(int rem)
{
    if (rem >= res)
        return;
    memset(b, 0, sizeof(b));
    memset(c, 0, sizeof(c));
    found = 0;
    duyet2(1);
    if (!found)
        res = rem;
}

void duyet(int i, int j, int rem)
{
    if (rem >= res)
        return;
    if (i == n+1)
    {
        ktr(rem);
        return;
    }
    if (j == n)
            duyet(i+1, 1, rem);
        else duyet(i, j+1, rem);
    if (a[i][j] == 0)
    {
        a[i][j] = 1;
        if (j == n)
            duyet(i+1, 1, rem+1);
        else duyet(i, j+1, rem+1);
        a[i][j] = 0;
    }
}

int main()
{
    freopen("ds.in", "r", stdin);
    freopen("testDs.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int t=1; t<=T; t++)
    {
        printf("Case #%d: ", t);
        scanf("%d\n", &n);
        for(int i=1; i<=n; i++)
        {
            gets(s);
            for(int j=1; j<=n; j++)
                a[i][j] = (s[j-1] - '0');
        }
        res = n*n;
        duyet(1, 1, 0);
        printf("%d\n", res);
    }
    return 0;
}
