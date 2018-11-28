// ProjectB.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#define _CRT_SECURE_NO_WARNINGS
#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <Windows.h>


#define MAX_CASE    1000

typedef struct _tagCaseSet
{
    int     nNumOfCases;

    struct
    {
        double   C;
        double   F;
        double   X;

    }Case[10];

}CASE_SET, *PCASE_SET;

bool isGoodForBuyNewFarm(double nTotCookie, double nTarget, int nNumOfFarm, double nFarmPrice, double nGatherPerFarm)
{
    double timea = 0;
    double timeb = 0;

    if (nTotCookie >= nTarget)
        return false;

    timea = (nTarget - nTotCookie) / (2 + (nNumOfFarm*nGatherPerFarm));
    timeb = (nTarget - (nTotCookie - nFarmPrice)) / (2 + ((nNumOfFarm + 1)*nGatherPerFarm));

    if (timea > timeb)
        return true;

    return false;
}

void CookieClickerAlpha(PCASE_SET pCaseSet)
{
    int     nNumOfFarm      = 0;
    double  nRemainCookie   = 0;
    double  nTotCookie      = 0;
    double  nTotTime        = 0;
    double  nloopTime       = 0;
    double  nGetPerSec      = 0;
    
    for (int nCase = 0; nCase < pCaseSet->nNumOfCases; nCase++)
    {
        nNumOfFarm  = 0;
        nTotCookie  = 0;
        nTotTime    = 0;
        nGetPerSec  = 0;
                
        for (int nloop = 0; nTotCookie < pCaseSet->Case[nCase].X; nloop++)
        {
            nGetPerSec  = 2 + (nNumOfFarm*pCaseSet->Case[nCase].F);
            nloopTime   = pCaseSet->Case[nCase].C / nGetPerSec;

            nTotCookie  += nGetPerSec*nloopTime;
            nTotTime    += nloopTime;
            
            if (isGoodForBuyNewFarm(nTotCookie, pCaseSet->Case[nCase].X, nNumOfFarm, pCaseSet->Case[nCase].C, pCaseSet->Case[nCase].F))
            {
                nTotCookie  -= pCaseSet->Case[nCase].C;
                nNumOfFarm  += 1;
            }
        }

        nTotCookie  -= nGetPerSec*nloopTime;
        nTotTime    -= nloopTime;
        
        nRemainCookie   = pCaseSet->Case[nCase].X - nTotCookie;
        nTotTime        = nTotTime + (nRemainCookie / (2 + (nNumOfFarm*pCaseSet->Case[nCase].F)));

        printf("Case #%d: %.7f\n", nCase + 1, nTotTime);

    }

    return;
}


void CookieClickerAlphaFile(PCASE_SET pCaseSet)
{
    int     nNumOfFarm      = 0;
    double  nRemainCookie   = 0;
    double  nTotCookie      = 0;
    double  nTotTime        = 0;
    double  nloopTime       = 0;
    double  nGetPerSec      = 0;
    
    FILE        *hFile = NULL;
    hFile = fopen("C:\\Users\\Lloyd\\Documents\\Visual Studio 2013\\Projects\\ProjectB\\Debug\\result.txt", "wt+");

    for (int nCase = 0; nCase < pCaseSet->nNumOfCases; nCase++)
    {
        nNumOfFarm  = 0;
        nTotCookie  = 0;
        nTotTime    = 0;
        nGetPerSec  = 0;
                
        for (int nloop = 0; nTotCookie < pCaseSet->Case[nCase].X; nloop++)
        {
            nGetPerSec  = 2 + (nNumOfFarm*pCaseSet->Case[nCase].F);
            nloopTime   = pCaseSet->Case[nCase].C / nGetPerSec;

            nTotCookie  += nGetPerSec*nloopTime;
            nTotTime    += nloopTime;
            
            if (isGoodForBuyNewFarm(nTotCookie, pCaseSet->Case[nCase].X, nNumOfFarm, pCaseSet->Case[nCase].C, pCaseSet->Case[nCase].F))
            {
                nTotCookie  -= pCaseSet->Case[nCase].C;
                nNumOfFarm  += 1;
            }
        }

        nTotCookie  -= nGetPerSec*nloopTime;
        nTotTime    -= nloopTime;
        
        nRemainCookie   = pCaseSet->Case[nCase].X - nTotCookie;
        nTotTime        = nTotTime + (nRemainCookie / (2 + (nNumOfFarm*pCaseSet->Case[nCase].F)));

        fprintf(hFile, "Case #%d: %.7f\n", nCase + 1, nTotTime);

    }

    fclose(hFile);

    return;
}


int _tmain(int argc, _TCHAR* argv[])
{
    FILE        *hFile = NULL;
    PCASE_SET   pCaseSet = (PCASE_SET)malloc(sizeof(CASE_SET)* MAX_CASE);
    ZeroMemory(pCaseSet, sizeof(CASE_SET)* MAX_CASE);

    hFile = fopen("C:\\Users\\Lloyd\\Documents\\Visual Studio 2013\\Projects\\ProjectB\\Debug\\input.txt", "rt+");

    fscanf(hFile, "%d", &pCaseSet->nNumOfCases);

    for (int i = 0; i < pCaseSet->nNumOfCases; i++)
    {
        fscanf(hFile, "%lf", &pCaseSet->Case[i].C);
        fscanf(hFile, "%lf", &pCaseSet->Case[i].F);
        fscanf(hFile, "%lf", &pCaseSet->Case[i].X);
    }

    fclose(hFile);

    CookieClickerAlphaFile(pCaseSet);

    free(pCaseSet);
    
    return 0;
}

