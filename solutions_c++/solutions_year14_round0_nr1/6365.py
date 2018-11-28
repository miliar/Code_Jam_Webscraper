#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#define inf 0x3f3f3f3f
#define ll __int64
using namespace std;

int t,ans,a,b,x,i,j,cnt,cas,vis[20],mp[10][10];

int main()
{
  //  freopen("tt.in","r",stdin);
  //  freopen("test.out","w",stdout);
    scanf("%d",&t);
    cas=0;
    while(t--)
    {
        cas++;
        scanf("%d",&a);
        memset(vis,0,sizeof vis);
        for(i=1;i<=4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%d",&x);
                if(i==a) vis[x]++;
            }
        }
        scanf("%d",&b);
        for(i=1;i<=4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%d",&x);
                if(i==b) vis[x]++;
            }
        }
        cnt=0;ans=0;
        for(i=1;i<=16;i++)
        {
            if(vis[i]==2)
            {
                ans=i;
                cnt++;
            }
        }
        printf("Case #%d: ",cas);
        if(cnt==0)
            printf("Volunteer cheated!\n");
        else if(cnt==1)
            printf("%d\n",ans);
        else printf("Bad magician!\n");
    }
    return 0;
}
