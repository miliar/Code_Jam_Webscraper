// ProjectA.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#define _CRT_SECURE_NO_WARNINGS
#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <Windows.h>


#define MAX_CASE    1000

typedef struct _tagMagSet
{
    int nSelect;
    int nCardArray[4][4];
}MAG_SET, *PMAG_SET;

typedef struct _tagCaseSet
{
    int     nNumOfCases;
    struct  
    {
        MAG_SET FirstSelection;
        MAG_SET SecondSelection;
    }Case[1];
}CASE_SET, *PCASE_SET;

void MagicTrick(PCASE_SET pCaseSet)
{
    int nCnt        = 0;
    int nLastValue  = 0;

    for (int nCase = 0; nCase < pCaseSet->nNumOfCases; nCase++)
    {
        nCnt = 0;

        for (int b = 0; b < 4; b++)
        for (int c = 0; c < 4; c++)
        if (pCaseSet->Case[nCase].FirstSelection.nCardArray[pCaseSet->Case[nCase].FirstSelection.nSelect - 1][b]
            == pCaseSet->Case[nCase].SecondSelection.nCardArray[pCaseSet->Case[nCase].SecondSelection.nSelect - 1][c])
        {
            nCnt++;
            nLastValue = pCaseSet->Case[nCase].SecondSelection.nCardArray[pCaseSet->Case[nCase].SecondSelection.nSelect - 1][c];
        }

        if (nCnt > 1)
        {
            printf("Case #%d: %s\n", nCase+1, "Bad magician!");
            continue;
        }

        if (nCnt == 1)
        {
            printf("Case #%d: %d\n", nCase + 1, nLastValue);
            continue;
        }

        printf("Case #%d: %s\n", nCase + 1, "Volunteer cheated!");
    }

    return;
}


int _tmain(int argc, _TCHAR* argv[])
{
    FILE        *hFile = NULL;
    PCASE_SET   pCaseSet = (PCASE_SET)malloc(sizeof(CASE_SET)* MAX_CASE);

    hFile = fopen("C:\\Users\\Lloyd\\Documents\\Visual Studio 2013\\Projects\\ProjectA\\Debug\\input.txt", "rt+");
    
    fscanf(hFile, "%d", &pCaseSet->nNumOfCases);

    for (int i = 0; i < pCaseSet->nNumOfCases; i++)
    {
        fscanf(hFile, "%d", &pCaseSet->Case[i].FirstSelection.nSelect);

        for (int b = 0; b < 4; b++)
        for (int c = 0; c < 4; c++)
            fscanf(hFile, "%d", &(pCaseSet->Case[i].FirstSelection.nCardArray[b][c]));

        fscanf(hFile, "%d", &pCaseSet->Case[i].SecondSelection.nSelect);

        for (int b = 0; b < 4; b++)
        for (int c = 0; c < 4; c++)
            fscanf(hFile, "%d", &(pCaseSet->Case[i].SecondSelection.nCardArray[b][c]));

    }

    fclose(hFile);

    MagicTrick(pCaseSet);

    free(pCaseSet);

	return 0;
}

