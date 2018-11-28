#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>

int cmp(const void *a,const void *b)
{
    return (*(double *)a)>(*(double *)b)?1:-1;
}
int main()
{
    freopen("E:\\D-large.in","r",stdin);
    freopen("E:\\D-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int l=1;l<=t;l++)
    {
        int s;
        double a[1001],b[1001],c[1001];
        memset(a,0,sizeof(a));
        memset(b,0,sizeof(b));
        memset(c,0,sizeof(c));
        scanf("%d",&s);
        int i,j;
        for(i=0;i<s;i++)
        scanf("%lf",&a[i]);
        for(i=0;i<s;i++)
        scanf("%lf",&b[i]);
        int sum=0,num=0;
        qsort(a,s,sizeof(a[0]),cmp);
        qsort(b,s,sizeof(b[0]),cmp);
//        for(i=0;i<s;i++)
//        printf("%lf ",a[i]);
//        printf("\n");
//        for(i=0;i<s;i++)
//        printf("%lf ",b[i]);
//        printf("\n");
        for(i=0;i<s;i++)
        c[i]=b[i];
        j=0;
        for(i=0;i<s;i++)
        {
            for(j=0;j<s;j++)
            {
                if(c[j]>a[i])
                {
                    sum++;
                    c[j]=-1;
                    break;
                }
            }
        }
        for(i=0;i<s;i++)
        {
            for(j=s-1;j>=0;j--)
            {
                if(a[i]>b[j])
                {
                    num++;
                    b[j]=1.1;
                    break;
                }
            }
        }
        printf("Case #%d: %d %d\n",l,num,s-sum);
    }
    return 0;
}
