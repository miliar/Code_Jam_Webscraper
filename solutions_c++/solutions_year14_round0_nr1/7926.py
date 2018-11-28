//Google Code Jam Qualification Round 2014 - Problem A. Magic Trick

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main()
{
    FILE * pFile;
    pFile = fopen ("a_output.txt" , "w");

    int square[4][4];
    bool card[17];
    int T, ans, tmp, findNum, finalAns;

    scanf("%d", &T);

    for(int testCase = 1; testCase <= T; testCase++)
    {
        memset(card, false, sizeof(card));

        scanf("%d", &ans);
        for(int i = 0; i < 4; i++)
            for(int j = 0; j < 4; j++)
                scanf("%d", &square[i][j]);

        for(int i = 0; i < 4; i++)
            card[ square[ans - 1][i] ] = true;

        scanf("%d", &ans);
        for(int i = 0; i < 4; i++)
            for(int j = 0; j < 4; j++)
                scanf("%d", &square[i][j]);

        findNum = 0;
        for(int i = 0; i < 4; i++)
            if(card[ square[ans - 1][i] ] == true)
            {
                findNum++;
                finalAns = square[ans - 1][i];
            }

        fprintf(pFile, "Case #%d: ", testCase);

        if(findNum == 1)
            fprintf(pFile, "%d\n", finalAns);
        else if(findNum > 1)
            fprintf(pFile, "Bad magician!\n");
        else if(findNum == 0)
            fprintf(pFile, "Volunteer cheated!\n");
    }
    fclose (pFile);
    return 0;
}
