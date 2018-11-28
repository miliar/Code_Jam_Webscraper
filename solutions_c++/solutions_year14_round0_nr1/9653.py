#include <stdio.h>

int T, card[4][4],newcard[4][4],chosen1,chosen2,resp;
int possible[4];
int main()
{
    scanf(" %d",&T);
    for(int t = 1; t <= T; t++)
    {
        printf("Case #%d: ",t);
        scanf(" %d",&chosen1);
        for(int i = 0; i < 4; i++)
        {
            for(int j = 0; j < 4; j++)
            {
                scanf(" %d",&card[i][j]);
            }
            if(i+1==chosen1)
            {
                for(int k = 0; k < 4; k++)
                    possible[k] = card[i][k];
            }

        }
        scanf(" %d",&chosen2);
        int numresp = 0;
        int resp;
        for(int i = 0; i < 4; i++)
        {
            for(int j = 0; j < 4; j++)
            {
                scanf(" %d",&newcard[i][j]);
            }
            if(i+1==chosen2)
            {
                for(int k = 0; k < 4; k++)
                {
                    for(int l = 0; l < 4; l++)
                    {

                        if(possible[k]==newcard[i][l])
                        {
                            numresp++;
                            resp = possible[k];
                        }
                    }
                }
            }

        }
        if(numresp==0)
            printf("Volunteer cheated!\n");
        else if(numresp>1)
            printf("Bad magician!\n");
        else printf("%d\n",resp);
    }
}
