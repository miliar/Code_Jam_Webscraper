#include <stdio.h>
#include <string.h>
int main()
{
    int times;
    scanf("%d",&times);

    int ok[times];
    int result[times];
    int temp[2][4];

    for(int i=0; i<times; i++)
    {
        for(int w=0; w<2; w++)
        {
            int cube[4][4];

            int row;
            scanf("%d",&row);

            for(int x=0; x<4; x++)
                for(int y=0; y<4; y++)
                {
                    scanf("%d",&cube[x][y]);
                    if(x==row-1)
                        temp[w][y] = cube[x][y];
                }
        }

        int n = 0;
        for(int j = 0; j<4; j++)
            for(int z = 0; z<4; z++)
            {
                if(temp[0][j]==temp[1][z])
                {
                    n++;
                    result[i]  = temp[0][j];
                }
            }
        if(n==1)
            ok[i]=1;
        else if(n>1)
            ok[i]=0;
        else if(n==0)
            ok[i]=-1;

    }
//-----------------------------------------------------------------------------------

    for(int i=1; i<=times; i++)
    {
        if(ok[i-1]==1)
        {
            printf("Case #%d: %d\n",i,result[i-1]);
        }
        else if(ok[i-1]==0)
        {
            printf("Case #%d: Bad magician!\n",i);
        }
        else if(ok[i-1]==-1)
        {
            printf("Case #%d: Volunteer cheated!\n",i);
        }
    }
    return 0;
}
