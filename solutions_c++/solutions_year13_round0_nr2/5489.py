#include <stdio.h>
int judge(int h,int l,int n,int m);

int a[105][105];
int main()
{
    freopen("B-large (2).in","r",stdin);
    freopen("sum.out","w",stdout);
    int b,count=0;
    scanf("%d",&b);
    while(b--)
    {
        int m,n,i,j,sign=1;
        ++count;
        scanf("%d%d",&n,&m);
        for(i=1; i<=n; i++)
            for(j=1; j<=m; j++)
                scanf("%d",&a[i][j]);
        for(i=1; i<=n; i++)
        {
            for(j=1; j<=m; j++)
                if(!judge(i,j,n,m))
                {
                    sign=0;
                    break;
                }
            if(!sign)
                break;
        }
        if(sign)
            printf("Case #%d: YES\n",count);
        else
            printf("Case #%d: NO\n",count);
    }
    return 0;
}
int judge(int h,int l,int n,int m)
{
    int sign1=1,sign2=1,i;
    for(i=1; i<=m; i++)
        if(a[h][i]>a[h][l])
        {
            sign1=0;
            break;
        }
    for(i=1; i<=n; i++)
        if(a[i][l]>a[h][l])
        {
            sign2=0;
            break;
        }
    if(sign1==0&&sign2==0) return 0;
    return 1;
}
