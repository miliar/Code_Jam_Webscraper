#include<stdio.h>
int main()
{
    int t,n,m,i,j,k,flag,a[101][101];
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        scanf("%d%d",&n,&m);
        for(i=0;i<m;i++)
            a[n][i]=0;
        for(i=0;i<n;++i)
        {
            for(j=a[i][m]=0;j<m;++j)
            {
                scanf("%d",&a[i][j]);
                if(a[i][j]>a[i][m])
                    a[i][m]=a[i][j];
                if(a[i][j]>a[n][j])
                    a[n][j]=a[i][j];
            }
        }
        for(i=flag=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                if(a[i][j]<a[i][m]&&a[i][j]<a[n][j])
                {
                    flag=1;
                    break;
                }
            }
            if(flag)
                break;
        }
        if(!flag)
            printf("Case #%d: YES\n",k);
        else
            printf("Case #%d: NO\n",k);
    }
    return 0;
}
