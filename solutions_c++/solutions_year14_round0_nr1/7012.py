#include <cassert>
#include <cstdio>
#include <iostream>

int grid[2][4][4];
int guessNo[2];
bool occurance[4];
int finalAns = 0;

int answer()
{
    int checkArr[2][4];
    
    for (int i = 0; i < 4; i++) 
    {
        checkArr[0][i] = grid[0][guessNo[0]-1][i];
        checkArr[1][i] = grid[1][guessNo[1]-1][i];
    }
    
    for (int i = 0; i < 4; i++) occurance[i] = false;
    for (int i = 0; i < 4; i++)
    {
        if (checkArr[0][i] == checkArr[1][0] || 
            checkArr[0][i] == checkArr[1][1] ||
            checkArr[0][i] == checkArr[1][2] ||
            checkArr[0][i] == checkArr[1][3])
        {
            occurance[i] = true;
        }
    }

    int occCount = 0;

    for (int i = 0; i < 4; i++)
    {
        if (occurance[i] == true) 
        {
            finalAns = checkArr[0][i];
            occCount++;
        }
    }

    if (occCount == 1) return 1;
    if (occCount  > 1) return 2;
    if (occCount == 0) return 3;

    return -1;
}

int main()
{
    int testCases = 0;
    

    FILE* fp = fopen("test_in_small.txt", "r");
    fscanf(fp, "%d\n", &testCases);

    for (int i = 0; i < testCases; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            fscanf(fp, "%d\n", &guessNo[j]);
            for (int row = 0; row < 4; row++)
            {
                int col = 0;
                fscanf(fp, "\n");
                fscanf(fp, "%d ", &grid[j][row][col++]);
                fscanf(fp, "%d ", &grid[j][row][col++]);
                fscanf(fp, "%d ", &grid[j][row][col++]);
                fscanf(fp, "%d ", &grid[j][row][col++]);
            }
        }
        int ans = answer();

        if (ans == 1)      printf("Case #%d: %d\n", i+1, finalAns);
        else if (ans == 2) printf("Case #%d: Bad magician!\n", i+1);
        else if (ans == 3) printf("Case #%d: Volunteer cheated!\n", i+1);
        else (assert(0));
    }

    return 0;
}