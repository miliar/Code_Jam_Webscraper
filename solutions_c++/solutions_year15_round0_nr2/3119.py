#include<cstdio>
#include<cstring>
#include<map>
#include<set>
#include<vector>
#include<algorithm>
using namespace std;
int num[1005];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T,n,minx,times,maxx;
    scanf("%d",&T);
    for(int L=1;L<=T;++L)
    {
        minx=99999999;
        maxx=-1;
        scanf("%d",&n);
        for(int i=0;i<n;++i)
        {
            scanf("%d",&num[i]);
            if(num[i]>maxx)
                maxx=num[i];
        }
        for(int i=1;i<=maxx;++i)
        {
            times=0;
            for(int j=0;j<n;++j)
                  times+=(num[j]/i)-(num[j]%i==0?1:0);
            minx=min(minx,i+times);
        }
        printf("Case #%d: %d\n",L,minx);
    }
    return 0;
}
