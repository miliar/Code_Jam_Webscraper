#include<cstdio>
#include<algorithm>
#define N 100010
using namespace std;
int ii,test,i,f[N],h[N],ans,sum,n,tt,o,q,j,a[N];
int z,zz;
char s[N];
int main()
{
freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&test);
    f[1]=0;
    for (i=2;i<=1000;i++)
    {
    f[i]=0x37373737;
    for (j=1;j<=i-1;j++)
    f[i]=min(f[j]+f[i-j]+1,f[i]);
    }
    for (ii=1;ii<=test;ii++)
    {
        scanf("%d",&n);
        for (i=1;i<=n;i++)
        scanf("%d",&a[i]);
        q=0x37373737;
        for (j=1;j<=1000;j++)
        {
            if (j>q)  break;
            ans=0;
            for (i=1;i<=n;i++)
            if (a[i]>j)
            {
                       z=a[i]/j;
                       if (a[i]%j) z++;
                       ans=ans+f[z];
            }
            if (ans+j<q) q=ans+j;
        }
        printf("Case #%d: %d\n",ii,q);
    }
   
}
