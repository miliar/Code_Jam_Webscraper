#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
#define M 100009
bool vis[20];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    int k = 0;
    while(T--)
    {
        k++;
        int a;
        scanf("%d",&a);
        printf("Case #%d: ",k);
        memset(vis,false,sizeof(vis));
        if(a == 0)
        {
            printf("INSOMNIA\n");
            continue;
        }
        bool ok = false;
        int ans = 0;
        for(int i = 1; ;i++)
        {
            int b = i*a;
            int tt = 1;
            int tmp = b;
            while(tmp)
            {
                tt = tmp%10;
                tmp = tmp/10;
                if(!vis[tt])
                {
                    vis[tt] = true;
                    ans++;
                    if(ans == 10)
                    {
                        ok = true;
                        break;
                    }
                }
            }
            if(ok)
            {
                printf("%d\n",b);
                break;
            }
        }
    }
    return 0;
}
