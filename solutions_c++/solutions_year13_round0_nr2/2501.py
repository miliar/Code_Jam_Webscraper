#include <iostream>
#include<cstdio>
int hitesh(int matrix[][102],int i,int j, int r, int c)
{
    int l,x=0;
    for(l=0;l<r;l++)
    {
        if(matrix[l][j]>matrix[i][j])
        {
            x=1;
            break;
        }
    }
    if(x==1)
   {
       for(l=0;l<c;l++)
        {
            if(matrix[i][l]>matrix[i][j])
            return 1;
        }
   }
    return 0;
}
int main()
{
    int tt, t=1;
    scanf("%d",&tt);
    while(t<=tt)
    {
        int n,m,i,j,matrix[102][102],flag=0;
        scanf("%d%d",&n,&m);
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            scanf("%d",&matrix[i][j]);
        }
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                if(hitesh(matrix,i,j,n,m)==1)
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
