#include<stdio.h>
int table[11][11];
int jum[11];

void check(int k,int m,int n)
{
    int count;
    for(int i=0;i<11;i++) jum[i]=0;
    for(int i=0;i<m;i++)
    {
        count=0;
        for(int j=0;j<n;j++) count+=table[i][j];
        if(count==n)
        {
            jum[i]=1;
            for(int j=0;j<n;j++)
            {
                table[i][j]=2;
            }
        }
    }

    for(int i=0;i<n;i++)
    {
        count=0;
        for(int j=0;j<m;j++)
        {
            if(jum[j]!=1) count+=table[j][i];
            else count+=1;
        }
        if(count==m)
        {
            for(int j=0;j<m;j++)
            {
                table[j][i]=2;
            }
        }
    }

    for(int i=0;i<m;i++) for(int j=0;j<n;j++)
    {
        if(table[i][j]==1)
        {
            printf("Case #%d: NO\n",k);
            return;
        }
    }
    printf("Case #%d: YES\n",k);

}
int main()
{
    int i,j,k,m,n,t;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        scanf("%d %d",&m,&n);
        for(i=0;i<m;i++) for(j=0;j<n;j++) scanf("%d",&table[i][j]);
        check(k,m,n);
    }

    return 0;
}

