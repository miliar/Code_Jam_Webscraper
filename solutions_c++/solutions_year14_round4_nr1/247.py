#include <iostream>
#include <cstdio>
#include <cstring>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <queue>
#include <vector>
#include <cstdlib>
#include <string>
#include <set>
using namespace std;

int a[10010],q[10010],vis[10010];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T,cas=0;
    scanf("%d",&T);
    while(T--)
    {
        int n,x,i,j;
        scanf("%d%d",&n,&x);
        for(i=1;i<=n;i++)
            scanf("%d",&a[i]);
        sort(a+1,a+1+n);
        int now=1,ans=0,rear=0;
        memset(vis,0,sizeof(vis));
        for(i=n;i>=1;i--)
        {
            if(vis[i]==1)
                continue;
            vis[i]=1;
            for(j=now;j<i;j++)
            {
                if(a[i]+a[j]<=x)
                {
                    q[rear++]=a[j];
                    vis[j]=1;
                }
                else
                {
                    now=j;
                    break;
                }
            }
            ans++;
            if(rear)
                rear--;
        }
        ans=ans+(rear+1)/2;
        printf("Case #%d: %d\n",++cas,ans);
    }
    return 0;
}
