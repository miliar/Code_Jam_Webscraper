#include<cstdio>
#include<algorithm>
using namespace std;

int main()
{
    freopen("D_large.txt","r",stdin);
    freopen("D_large_out.txt","w",stdout);
    double a[1005],b[1005];
    bool a1[1005],b1[1005];
    int n,i,j,m1,m2,tmp,t,co=0;

    scanf("%d",&t);

    while(t--)
    {
    scanf("%d",&n);

    for(i=1;i<=n;i++)
    {
        scanf("%lf",&a[i]);
        a1[i]=false;
        b1[i]=false;
    }
    for(j=1;j<=n;j++) scanf("%lf",&b[j]);

    sort(a+1,a+n+1);
    sort(b+1,b+n+1);

    m1=0;m2=0;

    tmp=n;
    for(i=n;i>=1;i--)
    {
        for(j=tmp;j>=1;j--)
        {
            if(a[i]>b[j] && b1[j]==false)
            {
                b1[j]=true;
                m1++;
                tmp=j;
                break;
            }
        }
    }

    tmp=n;
    for(i=n;i>=1;i--)
    {
        for(j=tmp;j>=1;j--)
        {
            if(b[i]>a[j] && a1[j]==false)
            {
                a1[j]=true;
                m2++;
                tmp=j;
                break;
            }
        }
    }

    m2=n-m2;

    printf("Case #%d: %d %d\n",++co,m1,m2);
    }
    return 0;
}

