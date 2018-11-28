#include <cstdio>
#include <memory.h>

int main() 
{
    int t;
    scanf("%d", &t);
    char input;
    scanf("%c", &input);
    short scoreMap[4][4][2][4]; // 2: 0 -> X, 1 -> O
    for (int caseNum = 1; caseNum <= t; ++caseNum)
    {
        bool completed = true;
        for (int i = 0; i < 4; ++i)
        {
            for (int j = 0; j < 4; ++j)
            {
                scanf("%c", &input);
                if (input == '.') 
                {
                    completed = false;
                    scoreMap[i][j][0][0] = 0;
                    scoreMap[i][j][0][1] = 0;
                    scoreMap[i][j][0][2] = 0;
                    scoreMap[i][j][0][3] = 0;
                    scoreMap[i][j][1][0] = 0;
                    scoreMap[i][j][1][1] = 0;
                    scoreMap[i][j][1][2] = 0;
                    scoreMap[i][j][1][3] = 0;
                }
                else if (input == 'O') 
                {
                    scoreMap[i][j][0][0] = 0;
                    scoreMap[i][j][0][1] = 0;
                    scoreMap[i][j][0][2] = 0;
                    scoreMap[i][j][0][3] = 0;
                    if (i == 0) 
                    {
                        scoreMap[i][j][1][0] = 1;
                        scoreMap[i][j][1][1] = 1;
                        scoreMap[i][j][1][2] = 1;
                        if (j == 0)
                            scoreMap[i][j][1][3] = 1;
                        else
                            scoreMap[i][j][1][3] = scoreMap[i][j - 1][1][3] + 1;
                    }
                    else 
                    {
                        scoreMap[i][j][1][1] = scoreMap[i - 1][j][1][1] + 1;
                        if (j != 3)
                            scoreMap[i][j][1][2] = scoreMap[i - 1][j + 1][1][2] + 1;
                        else 
                            scoreMap[i][j][1][2] = 1;
                        if (j == 0)
                        {
                            scoreMap[i][j][1][0] = 1;
                            scoreMap[i][j][1][3] = 1;
                        }
                        else
                        {
                            scoreMap[i][j][1][0] = scoreMap[i - 1][j - 1][1][0] + 1;
                            scoreMap[i][j][1][3] = scoreMap[i][j - 1][1][3] + 1;
                        }
                    }
                }
                else if (input == 'X') 
                {
                    scoreMap[i][j][1][0] = 0;
                    scoreMap[i][j][1][1] = 0;
                    scoreMap[i][j][1][2] = 0;
                    scoreMap[i][j][1][3] = 0;
                    if (i == 0) 
                    {
                        scoreMap[i][j][0][0] = 1;
                        scoreMap[i][j][0][1] = 1;
                        scoreMap[i][j][0][2] = 1;
                        if (j == 0)
                            scoreMap[i][j][0][3] = 1;
                        else
                            scoreMap[i][j][0][3] = scoreMap[i][j - 1][0][3] + 1;
                    }
                    else 
                    {
                        scoreMap[i][j][0][1] = scoreMap[i - 1][j][0][1] + 1;
                        if (j != 3)
                            scoreMap[i][j][0][2] = scoreMap[i - 1][j + 1][0][2] + 1;
                        else
                            scoreMap[i][j][0][2] = 1;
                        if (j == 0)
                        {
                            scoreMap[i][j][0][0] = 1;
                            scoreMap[i][j][0][3] = 1;
                        }
                        else
                        {
                            scoreMap[i][j][0][0] = scoreMap[i - 1][j - 1][0][0] + 1;
                            scoreMap[i][j][0][3] = scoreMap[i][j - 1][0][3] + 1;
                        }
                    }
                }
                else if (input == 'T') 
                {
                    if (i == 0) 
                    {
                        scoreMap[i][j][1][0] = 1;
                        scoreMap[i][j][1][1] = 1;
                        scoreMap[i][j][1][2] = 1;
                        if (j == 0)
                            scoreMap[i][j][1][3] = 1;
                        else
                            scoreMap[i][j][1][3] = scoreMap[i][j - 1][1][3] + 1;
                    }
                    else 
                    {
                        scoreMap[i][j][1][1] = scoreMap[i - 1][j][1][1] + 1;
                        if (j != 3)
                            scoreMap[i][j][1][2] = scoreMap[i - 1][j + 1][1][2] + 1;
                        else
                            scoreMap[i][j][1][2] = 1;
                        if (j == 0)
                        {
                            scoreMap[i][j][1][0] = 1;
                            scoreMap[i][j][1][3] = 1;
                        }
                        else
                        {
                            scoreMap[i][j][1][0] = scoreMap[i - 1][j - 1][1][0] + 1;
                            scoreMap[i][j][1][3] = scoreMap[i][j - 1][1][3] + 1;
                        }
                    }
                    if (i == 0) 
                    {
                        scoreMap[i][j][0][0] = 1;
                        scoreMap[i][j][0][1] = 1;
                        scoreMap[i][j][0][2] = 1;
                        if (j == 0)
                            scoreMap[i][j][0][3] = 1;
                        else
                            scoreMap[i][j][0][3] = scoreMap[i][j - 1][0][3] + 1;
                    }
                    else 
                    {
                        scoreMap[i][j][0][1] = scoreMap[i - 1][j][0][1] + 1;
                        if (j != 3)
                            scoreMap[i][j][0][2] = scoreMap[i - 1][j + 1][0][2] + 1;
                        else
                            scoreMap[i][j][0][2] = 1;
                        if (j == 0)
                        {
                            scoreMap[i][j][0][0] = 1;
                            scoreMap[i][j][0][3] = 1;
                        }
                        else
                        {
                            scoreMap[i][j][0][0] = scoreMap[i - 1][j - 1][0][0] + 1;
                            scoreMap[i][j][0][3] = scoreMap[i][j - 1][0][3] + 1;
                        }
                    }
                }
            }
            scanf("%c", &input);
        }
        /*
        for (int i = 0; i < 4; ++i)
        {
            for (int j = 0; j < 4; ++j) 
            {
                for (int l = 0; l < 4; ++l)
                {
                    printf("i[%d]j[%d][X]l[%d]:%i\n", i, j, l, scoreMap[i][j][0][l]);
                    printf("i[%d]j[%d][O]l[%d]:%i\n", i, j, l, scoreMap[i][j][1][l]);
                }
            }
        }
        */

        bool found = false;
        for (int i = 0; i < 4; ++i)
        {
            if (found)
                break;
            for (int j = 0; j < 4; ++j) 
            {
                if (found)
                    break;
                for (int l = 0; l < 4; ++l)
                {
                    if (scoreMap[i][j][0][l] >= 4) 
                    {
                        printf("Case #%d: X won\n", caseNum);
                        found = true;
                        break;
                    }
                    if (scoreMap[i][j][1][l] >= 4)
                    {
                        printf("Case #%d: O won\n", caseNum);
                        found = true;
                        break;
                    }
                }
            }
        }
        if (!found) 
            if (completed)
                printf("Case #%d: Draw\n", caseNum);
            else
                printf("Case #%d: Game has not completed\n", caseNum);
        scanf("%c", &input);
    }
    return 0;
}
