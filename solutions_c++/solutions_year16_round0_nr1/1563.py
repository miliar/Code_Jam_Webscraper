#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int t,n,m;
    scanf("%d",&t);
    for (int cas=1;cas<=t;++cas)
    {
        scanf("%d",&n);
        m=n;
        printf("Case #%d: ",cas);
        if (n==0) puts("INSOMNIA");
        else
        {
            int cnt[10]={0};
            int tot=10;
            while (1)
            {
                for (int tmp=n;tmp;tmp/=10)
                    if (++cnt[tmp%10]==1)
                        --tot;
                if (tot==0) break;
                n+=m;
            }
            printf("%d\n",n);
        }
    }
    return 0;
}
