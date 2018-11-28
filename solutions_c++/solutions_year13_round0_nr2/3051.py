#include <iostream>
#include <cstring>
#include <cstdio>
#include <queue>
#include <cmath>
#include <algorithm>
using namespace std;
int g[101][101], n, m;
bool check()
{
    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++) {
            bool isr=true, isc=true;
            for(int i2=0;i2<n;i2++)
                if (g[i2][j]>g[i][j]) isr=false;
            for(int j2=0;j2<m;j2++)
                if (g[i][j2]>g[i][j]) isc=false;
            if (!isr && !isc) return false;
        }
    return true;
}
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int Case;
    scanf("%d", &Case);
    for(int ca=1;ca<=Case;ca++) {
        printf("Case #%d: ", ca);
        scanf("%d%d", &n, &m);
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                scanf("%d", &g[i][j]);
        if (check()) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
