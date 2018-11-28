#include <iostream>
#include <cstdio>
#include <cstring>

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A.out","w",stdout);
    int T;int cnt;
    long long r,t;
    scanf("%d",&T);
    for (int ca = 1; ca <= T; ++ca)
    {
        scanf("%lld%lld",&r,&t);
        cnt = 0;
        while(1)
        {
            if (t >= 2*r + 1)
            {
                t -= 2*r + 1;
                cnt++;
                r += 2;
            }else break;
        }
        printf("Case #%d: %d\n",ca,cnt);
    }
    return 0;
}
