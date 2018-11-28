#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
    int N;
    char line[4][5];
    scanf("%d",&N);
    int t = 0;
    while(t < N)
    {
        for(int i=0;i<4;i++)
            scanf("%s",line[i]);
        char temp;
        int f = 0;
        int d = 0;
        for(int i=0;i<4;i++)
        {
            temp = line[i][0];
            if(temp == 'T')
                temp = line[i][1];
            int j;
            int y = 0;
            for(j=0;j<4;j++)
            {
                if(line[i][j] == '.')
                {
                    f = 1;
                    y = 1;
                }
                if(temp != line[i][j] && line[i][j] != 'T')
                    break;
            }
            if(j == 4 && !d && !y)
            {
                if(line[i][0] != 'T')
                printf("Case #%d: %c won\n",t+1,temp);
                else
                printf("Case #%d: %c won\n",t+1,line[i][1]);
                d = 1;
            }
        }
        for(int i=0;i<4;i++)
        {
            temp = line[0][i];
            if(temp == 'T')
                temp = line[1][i];
            int j;
            int y = 0;
            for(j=0;j<4;j++)
            {
                if(line[j][i] == '.')
                {
                    f = 1;
                    y = 1;
                }
                if(temp != line[j][i] && line[j][i] != 'T')
                    break;
            }
            if(j == 4 && !d && !y)
            {
                if(line[0][i] != 'T')
                printf("Case #%d: %c won\n",t+1,temp);
                else
                printf("Case #%d: %c won\n",t+1,line[1][i]);
                d = 1;
            }
        }
        int i = 0,j = 0;
        int y = 0;
        for(i=0,j=0;i<4 && j<4;i++,j++)
        {
            if(line[i][j] == '.')
            {
                f = 1;
                y = 1;
            }
            if(line[i][j] != line[0][0] && line[0][0] != 'T' && line[i][j] != 'T')
                break;
            else
                if((line[i][j] != line[0][0] && line[0][0] == 'T') && (line[i][j] != line[1][1] && line[i][j] != 'T'))
                    break;
        }
        if(i == 4 && j == 4 && !d && !y)
        {
            if(line[0][0] != 'T')
            printf("Case #%d: %c won\n",t+1,line[0][0]);
            else
            printf("Case #%d: %c won\n",t+1,line[1][1]);
            d = 1;
        }
        y = 0;
        for(i=0,j=3;i<4 && j>=0;i++,j--)
        {
            if(line[i][j] == '.')
            {
                f = 1;
                y = 1;
            }
            if(line[i][j] != line[0][3] && line[0][3] != 'T' && line[i][j] != 'T')
                break;
            else
                if((line[i][j] != line[0][3] && line[0][3] == 'T') && (line[i][j] != line[1][2] && line[i][j] != 'T'))
                    break;
        }
        if(i == 4 && j == -1 && !d && !y)
        {
            if(line[0][3] != 'T')
            printf("Case #%d: %c won\n",t+1,line[0][3]);
            else
            printf("Case #%d: %c won\n",t+1,line[1][2]);
            d = 1;
        }
        if( f && !d )
        {
            printf("Case #%d: Game has not completed\n",t+1);
        }
        else
        if(!d)
        {
            printf("Case #%d: Draw\n",t+1);
        }
        t++;
    }
    return 0;
}
