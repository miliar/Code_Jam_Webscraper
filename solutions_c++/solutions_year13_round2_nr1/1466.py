#include <cstdio>
#include <algorithm>

using namespace std;

int main(void)
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t, n, i, tc=0, tmp, res;
    long long a, data[105];
    for (scanf("%d", &t);t--;)
    {
        scanf("%lld%d", &a, &n);
        for (i=0;i<n;i++)
            scanf("%lld", &data[i]);
        if (a!=1LL)
        {
           sort(data,data+n);
           res=0x7FFFFFFF;
           tmp=0;
           for (i=0;i<n;i++)
               if (a>data[i])
                  a+=data[i];
               else
               {
                  res=min(res,tmp+n-i);
                  for (;a<=data[i];a=(a<<1)-1LL,tmp++);
                  a+=data[i];
               }
           res=min(res,tmp);
        }
        else
           res=n;
        printf("Case #%d: %d\n", ++tc, res);
    }
    return 0;
}
