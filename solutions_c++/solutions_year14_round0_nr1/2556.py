#include <stdio.h>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
int vis[20];
int main()
{
    int cas;
  //  freopen("A-small-attempt2.in","r",stdin);
  //  freopen("out.out","w",stdout);
    scanf("%d",&cas);
    int ca=1;

    while(cas--)
    {
        memset(vis,0,sizeof(vis));
        int w,a;
        scanf("%d",&w);
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                scanf("%d",&a);
                if(i==w)
                {
                    vis[a]++;
                }
            }
        }
        scanf("%d",&w);
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                scanf("%d",&a);
                if(i==w)
                {
                    vis[a]++;
                }
            }
        }
        int ok=0;
        int ans;
        for(int i=1;i<=16;i++)
        {
            if(vis[i]>=2)
            {
                ok++;
                ans=i;
            }
        }printf("Case #%d: ",ca++);
        if(ok==0)
        {
            puts("Volunteer cheated!");
        }
        else if(ok==1)
        {
            printf("%d\n",ans);
        }
        else
        {
            puts("Bad magician!");
        }
    }
    return 0;
}
