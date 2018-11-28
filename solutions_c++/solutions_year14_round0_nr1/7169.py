#include<cstdio>
#include<iostream>
using namespace std;

int mat1[4][4];
int mat2[4][4];
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int tests=0;tests<t;tests++)
    {
        int r1,r2;
        scanf("%d",&r1);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                scanf("%d",&mat1[i][j]);

        scanf("%d",&r2);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                scanf("%d",&mat2[i][j]);

        int i1=r1-1,i2=r2-1,c=0,ans;
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                if(mat1[i1][j]==mat2[i2][k])
                {
                    ans=mat1[i1][j];
                    c++;
                }
            }
        }

        if(c==1)
            printf("Case #%d: %d\n",tests+1,ans);
        else if(c>1)
            printf("Case #%d: Bad magician!\n",tests+1);
        else
            printf("Case #%d: Volunteer cheated!\n",tests+1);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
