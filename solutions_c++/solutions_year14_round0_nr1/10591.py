#include<stdio.h>

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int i,j,cases,T,first,second;
    int G1[5][5],G2[5][5];
    int move,square;
    scanf("%d",&T);
    for(cases=1; cases<=T; cases++)
    {
        move=0;
        square=0;
        scanf("%d",&first);
        for(i=1; i<5; i++)
        {
            scanf("%d %d %d %d",&G1[i][1],&G1[i][2],&G1[i][3],&G1[i][4]);
        }
        scanf("%d",&second);
        for(i=1; i<5; i++)
        {
            scanf("%d %d %d %d",&G2[i][1],&G2[i][2],&G2[i][3],&G2[i][4]);
        }
        for(i=1; i<5; i++)
        {
            for(j=1; j<5; j++)
            {
                if(G1[first][i]==G2[second][j])
                {
                    move++;
                    square=G1[first][i];
                }
            }
        }
        if(move==1)
            printf("Case #%d: %d\n",cases,square);
        else if(move==0)
            printf("Case #%d: Volunteer cheated!\n",cases);

        else
            printf("Case #%d: Bad magician!\n",cases);
    }

}
