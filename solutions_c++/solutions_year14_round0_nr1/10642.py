#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
    freopen("A-small-attempt2.in", "r", stdin);
    freopen("A-small-attempt2.out", "w", stdout);
    int t;
    scanf("%d",&t);
    int r=1;
    while(r<=t)
    {
        int a[4][4],b[4][4],sra,srb,c=-1;
        scanf("%d",&sra);
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                scanf("%d",&a[i][j]);
            }
        }
        scanf("%d",&srb);
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                scanf("%d",&b[i][j]);
            }
        }
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(a[sra-1][i]==b[srb-1][j])
                {
                    if(c==-1)
                    {
                        c=j;
                    }
                    else if(c>=0)
                    {
                        c=-2;
                    }
                }
            }
        }
        if(c>=0)
        {
            printf("Case #%d: %d\n",r,b[srb-1][c]);
        }
        else if(c==-1)
        {
            printf("Case #%d: Volunteer cheated!\n",r);
        }
        else
        {
            printf("Case #%d: Bad magician!\n",r);
        }
        r++;
    }

    return 0;
}
