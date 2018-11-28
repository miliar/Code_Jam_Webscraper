#include<iostream>
#include<string.h>
#include <algorithm>
#include<stdio.h>
#include<vector>
using namespace std;
char Board[109][109];
main()
{
    int Kase,DimensionX,DimensionY,isdere,Victory;
        scanf("%d",&Kase);
        for(int i=0;i<Kase;i++)
        {
                DimensionX=-1;DimensionY=-1;isdere=0;
                for(int j=0;j<4;j++)
                {
                        scanf("%s",&Board[j]);
                }
                for(int j=0;j<4;j++) 
                {
                        Victory=0;
                        for(int k=0;k<4;k++)
                                if(Board[j][k]==Board[j][0] || Board[j][k]=='T')
                                        Victory++;
                        if(Victory==4 && Board[j][0]!='.')
                        {
                                isdere=1;
                                DimensionX=j;
                                DimensionY=0;
                                break;
                        }
                }
                if(isdere==1)
                {
                        printf("Case #%d: %c won\n",i+1,Board[DimensionX][DimensionY]);
                        continue;
                }
                for(int j=0;j<4;j++) 
                {
                        Victory=0;
                        for(int k=0;k<4;k++)
                                if(Board[k][j]==Board[0][j] || Board[k][j]=='T')
                                        Victory++;
                        if(Victory==4 && Board[0][j]!='.')
                        {
                                isdere=1;
                                DimensionX=0;
                                DimensionY=j;
                                break;
                        }
                }
                if(isdere==1)
                {
                        printf("Case #%d: %c won\n",i+1,Board[DimensionX][DimensionY]);
                        continue;
                }
                Victory=0;
                for(int j=0;j<4;j++)
                {
                        if(Board[j][j]==Board[0][0] || Board[j][j]=='T')
                        {
                                Victory++;
                        }
                }
                if(Victory==4 &&  Board[0][0]!='.')
                {
                        printf("Case #%d: %c won\n",i+1,Board[0][0]);
                        continue;
                }
                Victory=0;
                for(int j=0;j<4;j++)
                {
                        if(Board[j][3-j]==Board[0][3] || Board[j][3-j]=='T')
                        {
                                Victory++;
                        }
                }
                if(Victory==4 && Board[0][3]!='.')
                {
                        printf("Case #%d: %c won\n",i+1,Board[0][3]);
                        continue;
                }
                isdere=0;
                for(int j=0;j<4;j++)
                        for(int k=0;k<4;k++)
                                if(Board[j][k]=='.')
                                {
                                        isdere=1;
                                        break;
                                }
                                (isdere==1)?printf("Case #%d: Game has not completed\n",i+1):printf("Case #%d: Draw\n",i+1);
        }
        return 0;
 
}
 