#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <cmath>
#include <algorithm>
using namespace std;
int p[100001],o[1001];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int n,i,j,t,cas = 1,ans,x;
    scanf("%d",&t);
    while(t--)
    {
        memset(o,0,sizeof(o));
        scanf("%d%d",&n,&x);
        ans = 0;
        for(i = 1;i <= n;i ++)
        {
            scanf("%d",&j);
            o[j] ++;
        }
        for(i = x;i >= 1;i --)
        {
            while(o[i])
            {
                o[i] --;
                for(j = x-i;j >= 1;j --)
                {
                    if(o[j])
                    {
                        o[j] --;
                        break;
                    }
                }
                ans ++;
            }
        }
        printf("Case #%d: %d\n",cas++,ans);
    }
    return 0;
}
