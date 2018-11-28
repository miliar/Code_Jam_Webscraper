#include<stdio.h>
#include<stdlib.h>
/*
int get_min(int rc,int rc1,int **lawn,int n,int m)
{
    int x=-1;
    int minn;
    if(rc==1)
    {
        //check row
        minn = 101;
        for(int i=0; i<n; i++)
        {
            if(minn > lawn[rc1][i])
            {
                minn = lawn[rc1][i];
                x = i;
            }
        }
        //printf("found min at row,%x\n",x+1);
        return x;
    }
    else
    {
        //check column
        minn = 101;
        for(int i=0; i<m; i++)
        {
            if(minn > lawn[i][rc1])
            {
                minn = lawn[i][rc1];
                x= i;
            }
        }
        return x;
    }
}
*/
int check(int row,int col,int **lawn,int n,int m)
{
    //return 0 if it fails
    int x = lawn[row][col];
    //printf("checking at %d %d for %d\n",row+1,col+1,x);
    int i;
    int c1=1,c2=1;
    for(i=0; i<n; i++)
    {
        //check vertically
        if(x != lawn[i][col])
        {
            c1=0;
            break;
        }
    }
    for(i=0; i<m; i++)
    {
        //check horizontally
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
                    if(check(i,j,lawn,n,m)==0)
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
