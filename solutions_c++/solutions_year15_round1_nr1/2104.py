#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string>

using namespace std;

int t,n,a[1005],cases=0,cnt0,cnt,dis,s,now;

int main()
{
    freopen("in2.in","r",stdin);
    freopen("fuck.out","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        cnt0=0,cnt=0;
        for(int i=1;i<=n;i++)
            scanf("%d",&a[i]);
        for(int i=2;i<=n;i++)
            if(a[i]<a[i-1])
                cnt0+=(a[i-1]-a[i]);
        dis=0;
        for(int i=2;i<=n;i++)
            if(a[i]<a[i-1])
                dis=max(dis,a[i-1]-a[i]);
        now=a[1];
        for(int i=2;i<=n;i++)
        {
            if(dis<=now)
            {
                cnt+=dis;
            }
            else
            {
                cnt+=now;
            }
            now=a[i];
        }
        printf("Case #%d: %d %d\n",++cases,cnt0,cnt);
    }
    return 0;
}
