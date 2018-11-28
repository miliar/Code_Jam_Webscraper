#include <cstdio>
#include <algorithm>
using namespace std;
bool cmp (double a,double b)
{
    return a<b;
}
int main()
{
    freopen("D-large.in","r",stdin);
    freopen("1.txt","w",stdout);
    int i,j,cc,t,n,ans,k,ans0;
    double a[1010],b[1010];
    scanf("%d",&t);
    for (cc=1;cc<=t;cc++)
    {
        ans0=ans=0;
        scanf("%d",&n);
        for (i=1;i<=n;i++)
            scanf("%lf",&a[i]);
        for (i=1;i<=n;i++)
            scanf("%lf",&b[i]);
        sort(b+1,b+n+1,cmp);
        sort(a+1,a+n+1,cmp);
        /*for (i=1;i<=n;i++)
        printf("%f ",a[i]);
        printf("\n");
        for (i=1;i<=n;i++)
        printf("%f ",b[i]);
        printf("\n");*/
        for (i=1,j=1,k=n;i<=n;i++)
        {
            if (a[i]<=b[j])
            {
                k--;
            }
            else
            {
                j++;
                ans0++;
            }
        }
        printf("Case #%d: %d ",cc,ans0);
        for (i=n;i>=1;i--)
        {
            for (j=1;j<=n;j++)
            if (b[j]>a[i])
            {
                b[j]=0;
                //sort(b+1,b+n+1,cmp);
                break;
            }
            if (j==n+1)
                ans++;
        }
        printf("%d\n",ans);
    }
    return 0;
}
