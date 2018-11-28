#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int cmp(const void *a,const void *b)
{
    return *(double *)a>*(double *)b?1:-1;
}
int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    double a[1010],b[1010];
    int i,j,k,t,n,l=1,sum1,sum2;
    int hash1[1010],hash2[1010];
    scanf("%d",&t);
    while(l<=t)
    {
        scanf("%d",&n);
        memset(hash1,0,sizeof(hash1));
        memset(hash2,0,sizeof(hash2));
        for(i=0;i<n;i++)
        {
            scanf("%lf",&a[i]);
        }
        for(i=0;i<n;i++)
        {
            scanf("%lf",&b[i]);
        }
        qsort(a,n,sizeof(a[0]),cmp);
        qsort(b,n,sizeof(b[0]),cmp);
        for(i=0,sum1=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(b[j]>a[i]&&hash1[i]==0&&hash2[j]==0)
                {
                    hash1[i]=1;
                    hash2[j]=1;
                    sum1++;
                    break;
                }
            }
        }
        memset(hash1,0,sizeof(hash1));
        memset(hash2,0,sizeof(hash2));
        for(i=0,k=0,sum2=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(a[j]>b[i]&&hash1[i]==0&&hash2[j]==0)
                {
                    hash1[i]=1;
                    hash2[j]=1;
                    sum2++;
                    break;
                }
            }
        }
        printf("Case #%d: %d %d\n",l++,sum2,n-sum1);
    }
    return 0;
}
