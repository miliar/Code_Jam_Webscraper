#include<stdio.h>

int a[200][200];

int main()
{
    int T,cases=1,i,j,N,M,k,flag;
    freopen("B-small-attempt1.in","r",stdin);
    freopen("sub-2.out","w",stdout);
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d %d",&N,&M);
        for(i=0;i<N;i++)
        {
            for(j=0;j<M;j++)
            {
                scanf("%d",&a[i][j]);
            }
        }
        flag=0;
        for(i=0;i<N;i++)
        {
            for(j=0;j<M;j++)
            {
                if(a[i][j]==1)
                {
                    for(k=0;k<N;k++)
                    {
                        if(a[k][j]==2) break;
                    }
                    if(k==N) flag=1;
                    else flag=2;
                    if(flag==2)
                    {
                        for(k=0;k<M;k++)
                        {
                            if(a[i][k]==2) break;
                        }
                        if(k==M) flag=1;
                    }
                }
                if(flag==2) break;
            }
            if(flag==2) break;
        }
        printf("Case #%d: ",cases++);
        if(flag==1 || flag==0)
        {
            printf("YES\n");
        }
        else printf("NO\n");
    }
    return 0;
}
