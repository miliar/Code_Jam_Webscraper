#include <iostream>
#include <string.h>
#include <algorithm>
#include <stdio.h>
#define maxn 10010
using namespace std;
int a[maxn],vis[710];
int main()
{
    freopen("dd.in","r",stdin);
    freopen("out.txt","w+",stdout);
    int ncase,T=0;
    scanf("%d",&ncase);
    while(ncase--)
    {
        printf("Case #%d: ",++T);
        int n,X,x;
        scanf("%d%d",&n,&X);
        memset(vis,0,sizeof(vis));
        for(int i=0;i<n;i++)
        {
            scanf("%d",&x);
            vis[x]++;
        }
        int ans=0;
        for(int i=700;i>=1;i--)
        {
            while(vis[i]--)
            {
               // printf("%d %d %d %d %d\n",vis[10],vis[20],vis[30],vis[40],vis[60]);
                int tt=i;
                ans++;
                for(int j=min(X-tt,tt);j>=1;j--)
                {
                    if(vis[j]>0)
                    {
                        vis[j]--;
                        break;
                    }
                }
            }
        }
        printf("%d\n",ans);
    }
    return 0;
}
