#include<stdio.h>
int main()
{
    int caset=0,i,j,n,m,t,a[101][101],b=0,temp,k;
    scanf("%d",&t);
    while(t--)
    {   b=0;
        caset++;
        scanf("%d%d",&n,&m);
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                scanf("%d",&a[i][j]);
            }
        }
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                printf("%d ",a[i][j]);
            }
            printf("\n");
        }
        for(i=0;i<n && b!=1;i++)
        {
            for(j=0;j<m && b!=1;j++)
            {
                temp=a[i][j];
                for(k=0;k<n && b!=1;k++)
                {
                    if(a[k][j]>temp)
                    {    b=1;
                        break;
                    }
                }
                if(b!=0)
                {   b=0;
                    for(k=0;k<m && b!=1;k++)
                    {
                        if(a[i][k]>temp)
                        {    b=1;
                            break;
                        }
                    }
                }                
            }
        }
        if(b!=1)
            printf("Case #%d: YES",caset);
        else
            printf("Case #%d: NO",caset);
    }
    return 0;
}