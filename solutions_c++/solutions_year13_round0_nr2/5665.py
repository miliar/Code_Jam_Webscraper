#include<stdio.h>
#include<stdlib.h>

int check_lawn(int row,int col,int **lawn,int n,int m)
{

    int x = lawn[row][col];
    int i;
    int c1=1,c2=1;
    for(i=0; i<n; i++)
    {
        if(x != lawn[i][col])
        {
            c1=0;
            break;
        }
    }
    for(i=0; i<m; i++)
    {
        if(x != lawn[row][i])
        {
            c2=0;
            break;
        }
    }

    return (c1+c2>0?1:0);
}

int main()
{
    int t,n,m,i,j,k,nn;
    scanf("%d",&t);
    for(nn=1; nn<=t; nn++)
    {
        scanf("%d %d",&n,&m);
        int **lawn;
        lawn = (int **)malloc(n*m*sizeof(int));
        for(i=0; i<n; i++)
        {
            lawn[i] = (int *)malloc(m*sizeof(int));
        }
        for(j=0; j<n; j++)
        {
            for(k=0; k<m; k++)
            {
                scanf("%d",&lawn[j][k]);
            }
        }
        int c=1;
        for(i=0; i<n; i++)
        {
            for(j=0; j<m; j++)
            {
                if(lawn[i][j]==1)
                {
                    if(check_lawn(i,j,lawn,n,m)==0)
                    {
                        c=0;
                        break;
                    }
                }
            }

        }
        if(n==1 && m==1)
        {
            printf("Case #%d: %s\n",nn,"YES");
        }
        else{
        if(c==0)
        {
            printf("Case #%d: %s\n",nn,"NO");
        }
        else if(c==1)
        {
            printf("Case #%d: %s\n",nn,"YES");
        }
        }
    }
return 0;
}
