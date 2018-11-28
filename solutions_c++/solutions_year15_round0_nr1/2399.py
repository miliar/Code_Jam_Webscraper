#include <iostream>
#include <cstdio>
#define SMAX 1010

using namespace std;

int t, smax, a[SMAX];

void solve(int ind)
{
    int nr = 0;
    int ado = 0;
    for (int i = 0; i <= smax; i++)
    {
        if (nr < i)
        {
            ado += i-nr;
            nr += (i-nr);
        }
        nr += a[i];
    }
    printf("Case #%d: %d\n", ind+1, ado);
}

int main()
{
    freopen("ovation.in", "r", stdin);
    freopen("ovation.out", "w", stdout);

    scanf("%d", &t);
    char c;
    for (int i = 0; i < t; i++)
    {
        scanf("%d\n", &smax);
        for (int j = 0; j <= smax; j++)
        {
            scanf("%c", &c);
            a[j] = c-'0';
        }
        solve(i);
    }
    return 0;
}
