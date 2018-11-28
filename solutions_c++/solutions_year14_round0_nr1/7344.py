#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;
int mat[4][4];
int mat1[4][4];
int c[110],ele[110];
int main()
{
    int t;
    scanf("%d",&t);
    int i,j,k,n,m;
    for(i=1;i<=t;i++)
    {
        scanf("%d",&n);
        for(j=0;j<4;j++)
        {
            for(k=0;k<4;k++)
            {
                scanf("%d",&mat[j][k]);
            }
        }
        scanf("%d",&m);
        for(j=0;j<4;j++)
        {
            for(k=0;k<4;k++)
            {
                scanf("%d",&mat1[j][k]);
            }
        }
        c[i]=0;
        for(j=0;j<4;j++)
        {
            for(k=0;k<4;k++)
            {
                if(mat[n-1][j]==mat1[m-1][k])
                {
                    c[i]++;
                    ele[i] = mat[n-1][j];
                }
            }
        }
    }
    for(i=1;i<=t;i++)
    {
        if(c[i]==1)
        printf("Case #%d: %d\n",i,ele[i]);
        else if(c[i]>1)
        printf("Case #%d: Bad magician!\n",i);
        else if(c[i]<1)
        printf("Case #%d: Volunteer cheated!\n",i);
    }
    return 0;
}
