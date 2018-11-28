#include <stdio.h>


int main()
{
    int c,n, i, j, xCount, tCount, oCount, dotCount;
    int colXCount, colTCount, colOCount, colDotCount;
    char in[5][5], winner;
    bool dotExist;
    FILE *fp;

    fp = fopen("out.txt", "w");


    scanf("%d", &n);
    getchar();

    c = 1;
    while(c <= n)
    {
        for (i=0; i<5;i++)
        {
            gets(in[i]);
        }

        winner = '.';
        dotExist = false;

        for (i=0; i<4; i++)
        {
            tCount = xCount = oCount = dotCount = 0;
            colTCount = colXCount = colOCount = colDotCount = 0;
            for (j=0;j<4;j++)
            {
                if (in[i][j] == 'X')
                {
                    xCount++;
                }
                else if (in[i][j] == 'O')
                {
                    oCount++;
                }
                else if (in[i][j] == 'T')
                {
                    tCount++;
                }
                else if (in[i][j] == '.')
                {
                    dotCount++;
                    dotExist = true;
                }

                if (in[j][i] == 'X')
                {
                    colXCount++;
                }
                else if (in[j][i] == 'O')
                {
                    colOCount++;
                }
                else if (in[j][i] == 'T')
                {
                    colTCount++;
                }
                else if (in[j][i] == '.')
                {
                    colDotCount++;
                    dotExist = true;
                }
            }

            if (tCount + xCount == 4 && dotCount == 0)
            {
                winner =  'X';
            }
            else if (oCount + tCount == 4 && dotCount == 0){
                winner = 'O';
            }

            if(colTCount + colXCount == 4 && colDotCount == 0)
            {
                winner = 'X';
            }
            else if (colTCount + colOCount == 4 && colDotCount == 0)
            {
                winner = 'O';
            }

            if (winner == 'X' || winner == 'O')
            {
                break;
            }
        }

        if (winner != 'X' && winner != 'O')
        {
            tCount = xCount = oCount = dotCount = 0;
            for(i=0;i<4;i++)
            {
                if (in[i][i] == 'X')
                {
                    xCount ++;
                }
                else if(in[i][i] == 'O')
                {
                    oCount ++;
                }
                else if (in[i][i] == 'T')
                {
                    tCount ++;
                }
                else if (in[i][i] == '.')
                {
                    dotCount ++;
                    dotExist = true;
                }
            }

            if (tCount + xCount == 4 && dotCount == 0)
            {
                winner =  'X';
            }
            else if (oCount + tCount == 4 && dotCount == 0){
                winner = 'O';
            }
        }

        if (winner != 'X' && winner != 'O')
        {
            tCount = xCount = oCount = dotCount = 0;
            for(i=0;i<4;i++)
            {
                if (in[3-i][i] == 'X')
                {
                    xCount ++;
                }
                else if(in[3-i][i] == 'O')
                {
                    oCount ++;
                }
                else if (in[3-i][i] == 'T')
                {
                    tCount ++;
                }
                else if (in[3-i][i] == '.')
                {
                    dotCount ++;
                    dotExist = true;
                }
            }

            if (tCount + xCount == 4)
            {
                winner =  'X';
            }
            else if (oCount + tCount == 4){
                winner = 'O';
            }
        }

        if (winner == 'X')
        {
            fprintf(fp, "Case #%d: X won", c);
        }
        else if (winner == 'O')
        {
            fprintf(fp, "Case #%d: O won", c);
        }
        else
        {
            if (dotExist)
            {
                fprintf(fp, "Case #%d: Game has not completed", c);
            }
            else
            {
                fprintf(fp, "Case #%d: Draw", c);
            }
        }

        c++;

        if (c <= n)
        {
            fputs("\n", fp);
        }
    }


    fclose(fp);

    return 0;
}
