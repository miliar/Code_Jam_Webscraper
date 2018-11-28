#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
int a[100000];
int cmp(const void *e,const void *f)
{
    return *(int *)e - *(int *)f;
}
int main()
{
    freopen("data1.in","r",stdin);
    freopen("data1.out","w",stdout);
    int i,j,n,m,s,t,min,k,pre;
    int T;
    scanf("%d",&t);
    T=1;
    while(t--)
    {
        scanf("%d %d",&n,&m);
        pre=n;
        for(i=0;i<=m-1;i++)
        {
            scanf("%d",&a[i]);
        }
        qsort(a,m,sizeof(a[0]),cmp);
        s=0; k=0;
        for(i=0;i<(1<<m);i++)
        {
            s=0;
            for(j=0;j<=m-1;j++)
            {
                if(i&(1<<j)&&n!=1)
                {
                    if(n>a[j])
                    {
                        n+=a[j];
                    }else
                    {
                        while(n<=a[j])
                        {
                            s+=1;
                            n=n+n-1;
                        }
                        n+=a[j];
                    }
                }else
                {
                    s+=1;
                }
            }
            if(k==0)
            {
                min=s;
                k=1;
            }else
            {
                if(min>s)
                {
                    min=s;
                }
            }
            n=pre;
        }
        printf("Case #%d: %d\n",T++,min);
    }
    return 0;
}
