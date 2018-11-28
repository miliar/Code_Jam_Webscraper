#include <iostream>
#include <stdio.h>
#include <string>
#include <cstring>
#include <cmath>


using namespace std;
int vis[12];

int main()
{
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);

    int T;
    scanf("%d",&T);

    int ca=1;
    int n;
    while(T--)
    {
        scanf("%d",&n);
        memset(vis,0,sizeof vis);

        printf("Case #%d: ",ca++);
        if(n==0)
        {
            puts("INSOMNIA");
            continue;
        }
        int cnt=0;
        int ans=0;
        for(int i=1;i<=100;i++)
        {
            int t=n*i;
            while(t)
            {
                int a=t%10;
                if(vis[a]==0)
                {
                    vis[a]=1;
                    cnt++;
                }
                t/=10;
                if(cnt==10)
                {
                    ans=n*i;
                    break;
                }
            }
            if(ans)
                break;
        }
        printf("%d\n",ans);

    }
    return 0;
}
