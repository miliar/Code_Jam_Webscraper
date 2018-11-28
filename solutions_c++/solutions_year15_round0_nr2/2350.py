#include <iostream>
#include <cstdio>
#include <cstring>
#define MAXD 1015

using namespace std;

int t, d, p[MAXD], px;

int bst(int index)
{
    for (int i = index; i >= 1; i--)
        if (p[i])
            return i;
    return 0;
}
int sol;
void solve(int ind)
{
    sol = 0x7fffffff;
    int imp = 0;
    int k = bst(1009);
    for (int i = 1; i <= k; i++)
    {
        imp = 0;
        for (int j = 2; j <= k; j++)
        {
            if (p[j] != 0)
            {
                imp += p[j] * (j/i-!(j%i));
            }
        }
        sol = min(sol, i+imp);
    }
    printf("Case #%d: %d\n", ind, sol);
    memset(p, 0, sizeof(p));
}

int main()
{
    freopen("pancakes.in", "r", stdin);
    freopen("pancakes.out", "w", stdout);

    scanf("%d", &t);
    for (int i = 1; i <= t; i++)
    {
        scanf("%d", &d);
        for (int i = 0; i < d; i++)
        {
            scanf("%d", &px);
            p[px]++;
        }
        solve(i);
    }
    return 0;
}
