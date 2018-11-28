#include <bits/stdc++.h>
using namespace std;
int main()
{
    freopen("d.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int tt = 1; tt <= t; tt++)
    {
        long long k, c, s;
        scanf("%lld %lld %lld", &k, &c, &s);
        long long go = 1;
        for (int i = 1; i < c; i++)
        {
            go *= k;
        }
        long long pos = 1;
        printf("Case #%d: ", tt);
        for (int i = 1; i <= s; i++)
        {
            printf("%lld ", pos);
            pos += go;
        }
        printf("\n");
    }
}
