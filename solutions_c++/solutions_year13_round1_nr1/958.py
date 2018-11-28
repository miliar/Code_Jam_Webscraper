#include <cstdio>
#include <algorithm>

using namespace std;

int main(void)
{
    int t, tc=0;
    long long r, p, l, h, m, tmp, res;
    for (scanf("%d", &t);t--;)
    {
        scanf("%lld%lld", &r, &p);
        r<<=1;
        res=0;
        for (l=1,h=p;l<=h;)
        {
            m=(l+h)>>1;
            tmp=(m<<1)+r-1LL;
            if (tmp>p/m)
               h=m-1LL;
            else
            {
               tmp*=m;
               if (tmp>p)
                  h=m-1LL;
               else
               {
                  res=m;
                  l=m+1LL;
               }
            }
        }
        printf("Case #%d: %lld\n", ++tc, res);
    }
    return 0;
}
