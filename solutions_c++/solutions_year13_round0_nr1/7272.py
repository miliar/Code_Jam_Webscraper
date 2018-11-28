#include<iostream>
#include<string>
#include<stdio.h>

using namespace std;


int main()
{
    int i,t;
    int sqX[4][4];
    int sqO[4][4];
    char var;
    bool matrixHasEmptyCoordinates = false;
    bool lastCaseEvaluated = false;
    // test cases
    cin>>t;
    i=0;
    NextTestCase:   i++;
    while(i<=t)
    {
        // Initialize array and variables
        matrixHasEmptyCoordinates=false;
        for(int r=0; r<4; r++)
        {
            for(int c=0; c<4; c++)
            {
                sqX[r][c]=sqO[r][c]=0;
            }
        }

        // Reading square and update square matrix
        for(int x=0; x<4; x++)
        {
            for(int y=0; y<4; y++)
            {
                cin>>var;
                if(var=='X')
                {
                    sqX[x][y]++;
                }
                else if(var=='O')
                {
                    sqO[x][y]++;
                }
                else if(var=='T')
                {
                    sqX[x][y]++;
                    sqO[x][y]++;
                }
                else if(var=='.')
                {
                    matrixHasEmptyCoordinates = true;
                }
            }
        }

        int sumX=0,sumO=0;
        // Who won ?
        // Sum row
        for(int c=0; c<4; c++)
        {
            sumX=0;
            sumX=sqX[0][c]+sqX[1][c]+sqX[2][c]+sqX[3][c];
            if(sumX==4)
            {
                printf("Case #%d: %s\r\n",i,"X won");
                goto NextTestCase;
            }
            sumO=0;
            sumO=sqO[0][c]+sqO[1][c]+sqO[2][c]+sqO[3][c];
            if(sumO==4)
            {
                printf("Case #%d: %s\r\n",i,"O won");
                goto NextTestCase;
            }
        }

        // Sum column
        for(int r=0; r<4; r++)
        {
            sumX=0;
            sumX=sqX[r][0]+sqX[r][1]+sqX[r][2]+sqX[r][3];
            if(sumX==4)
            {
                printf("Case #%d: %s\r\n",i,"X won");
                goto NextTestCase;
            }
            sumO=0;
            sumO=sqO[r][0]+sqO[r][1]+sqO[r][2]+sqO[r][3];
            if(sumO==4)
            {
                printf("Case #%d: %s\r\n",i,"O won");
                goto NextTestCase;
            }
        }
        // Sum 1st Diagonal
        sumO=sumX=0;
        sumX=sqX[0][0]+sqX[1][1]+sqX[2][2]+sqX[3][3];
        sumO=sqO[0][0]+sqO[1][1]+sqO[2][2]+sqO[3][3];
        if(sumX==4)
        {
            printf("Case #%d: %s\r\n",i,"X won");
            goto NextTestCase;
        }
        if(sumO==4)
        {
            printf("Case #%d: %s\r\n",i,"O won");
            goto NextTestCase;
        }
        // Sum 2nd diagonal
        sumO=sumX=0;
        sumX=sqX[0][3]+sqX[1][2]+sqX[2][1]+sqX[3][0];
        sumO=sqO[0][3]+sqO[1][2]+sqO[2][1]+sqO[3][0];
        if(sumX==4)
        {
            printf("Case #%d: %s\r\n",i,"X won");
            goto NextTestCase;
        }
        if(sumO==4)
        {
            printf("Case #%d: %s\r\n",i,"O won");
            goto NextTestCase;
        }
        if(matrixHasEmptyCoordinates==true)
        {
            printf("Case #%d: %s\r\n",i,"Game has not completed");
            goto NextTestCase;
        }
        else
        {
            printf("Case #%d: %s\r\n",i,"Draw");
            goto NextTestCase;
        }

    }
}
