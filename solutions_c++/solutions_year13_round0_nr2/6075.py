#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <ctime>
#include <queue>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;
int p[201][201],n,m;
int judge()
{
    int i,j,k,z;
    for(i = 1; i <= n; i ++)
    {
        for(j = 1; j <= m; j ++)
        {
            if(p[i][j] == 1)
            {
                z = 0;
                for(k = 1; k <= m; k ++)
                {
                    if(p[i][k] != 1)
                    break;
                }
                if(k == m+1) z = 1;
                for(k = 1;k <= n;k ++)
                {
                    if(p[k][j] != 1)
                    break;
                }
                if(k == n+1) z = 1;
                if(z == 0) return 0;
            }
        }
    }
    return 1;
}
int main()
{
    int t,cas = 1,i,j;
    freopen("B-small-attempt3.in","r",stdin);
    freopen("B-small-attempt3.out","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d",&n,&m);
        for(i = 1; i <= n; i ++)
        {
            for(j = 1; j <= m; j ++)
                scanf("%d",&p[i][j]);
        }
        printf("Case #%d: ",cas++);
        if(judge())
        printf("YES\n");
        else
        printf("NO\n");
    }
    return 0;
}
