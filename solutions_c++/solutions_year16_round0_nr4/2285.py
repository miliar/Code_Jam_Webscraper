#include<iostream>
#include<cstring>
#include<cstdio>

int T, n, m, s;

int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("gcj4.out", "w", stdout);
    scanf("%d", &T);
    for(int i=1; i<=T; i++)
    {
        scanf("%d%d%d", &n, &m, &s);
        printf("Case #%d: ", i);
        for(int j=1; j<=n; j++) printf(" %d", j);
        printf("\n");
    }
    return 0;
}
