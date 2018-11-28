#include<stdio.h>
int check(int a[][102],int i,int j, int n, int m)
{
    int l,x=0;
    for(l=0;l<n;l++)
    {
        if(a[l][j]>a[i][j])
        {
            x=1;
            break;
        }
    }
    if(x==1)
   {
       for(l=0;l<m;l++)
        {
            if(a[i][l]>a[i][j])
            return 1;
        }
   }
    return 0;
}
int main()
{
    int test , t=1;
    scanf("%d",&test);
    while(t<=test)
    {
        int n,m,i,j,a[102][102],flag=0;
        scanf("%d%d",&n,&m);
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            scanf("%d",&a[i][j]);
        }
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                if(check(a,i,j,n,m)==1)
                {
                    flag=1;
                    break;
                }
            }
            if(flag==1)
            break;
        }
        if(flag!=1)
        printf("Case #%d: YES\n",t);
        else
        printf("Case #%d: NO\n",t);
        t++;
    }
    return 0;
}