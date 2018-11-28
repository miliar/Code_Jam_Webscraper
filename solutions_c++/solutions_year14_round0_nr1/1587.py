#include <iostream>
#include <cstdio>
#include <cstring>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <functional>
#include <queue>
#include <vector>
#include <cstdlib>
#include <string>
#include <set>
using namespace std;

int a[10][10],vis[20];

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int T,cas=0;
    scanf("%d",&T);
    while(T--)
    {
        int i,j,x,num=0;
        scanf("%d",&x);
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                scanf("%d",&a[i][j]);
        memset(vis,0,sizeof(vis));
        for(i=1;i<=4;i++)
            vis[a[x][i]]++;
        scanf("%d",&x);
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                scanf("%d",&a[i][j]);
        for(i=1;i<=4;i++)
            vis[a[x][i]]++;
        for(i=1;i<=16;i++)
        {
            if(vis[i]==2)
                num++;
        }
        printf("Case #%d: ",++cas);
        if(num==0)
            printf("Volunteer cheated!\n");
        else if(num>1)
            printf("Bad magician!\n");
        else
        {
            for(i=1;i<=16;i++)
                if(vis[i]==2)
                    printf("%d\n",i);
        }
    }
    return 0;
}
