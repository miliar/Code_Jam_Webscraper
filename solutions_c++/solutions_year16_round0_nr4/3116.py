#include <cstdio>
#include <cmath>
using namespace std;
int k,c,s;
int a[110];
long long ans[110];
long long propagate()
{
    long long result[110];
    result[0]=a[0];
    for (int i=1;i<c;++i)
        result[i]=(result[i-1]-1)*k+a[i];
    return result[c-1];
}
int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    int testcase;
    scanf("%d",&testcase);
    for (int ii=1;ii<=testcase;++ii)
    {
        scanf("%d%d%d",&k,&c,&s);
        if (c*s<k)
        {
            printf("Case #%d: IMPOSSIBLE",ii);
            if (ii<testcase) printf("\n");
            continue;
        }
        for (int i=0;i<c;++i)
            a[i]=1;
        int top=0;
        int capacity=((k%s==0)?(k/s):(k/s)+1);
        int cc=0;
        for (int i=1;i<=k;++i)
        {
            a[cc++]=i;
            if (cc==capacity)
            {
                ans[top++]=propagate();
                cc=0;
            }
        }
        printf("Case #%d: %lld",ii,ans[0]);
        for (int i=1;i<top;++i)
            printf(" %lld",ans[i]);
        if (ii<testcase) printf("\n");
    }
    return 0;
}
