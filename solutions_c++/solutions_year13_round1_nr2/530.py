#include <cstdio>
const int MAXN = 10000;
int ge, r, n, v[MAXN];
int min(int a, int b)
{
    if(a <= b)
        return a;
    return b;
}
int gain(int e, int p)
{
    int i, temp, m = 0;
    if(p == n)
        return 0;
    for(i = 0;  i <= e; i++)
    {
        temp = i * v[p] + gain(min(ge, e - i + r), p + 1);
        if(m < temp)
            m = temp;
    }
    return m;
}
int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int t, i, j;
    scanf("%d", &t);
    for(i = 1; i <= t; i++)
    {
        scanf("%d%d%d", &ge, &r, &n);
        for(j = 0; j < n; j++)
            scanf("%d", &v[j]);
        printf("Case #%d: %d\n", i, gain(ge, 0));
    }
    return 0;
}
