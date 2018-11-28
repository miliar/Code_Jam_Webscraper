#include <iostream>
#include <stdio.h>

using namespace std;

bool checkCountCompleted(int* nFlagIndex)
{
    bool retVal = true;
    for(int nIndex=0; nIndex < 10; ++nIndex)
    {
        if(nFlagIndex[nIndex] != 1)
            retVal = false;
    }
    return retVal;
}
void parseNoFillArray(int nFinalSleepNo, int* nFlagIndex)
{
    int nDigit = 0;

    while(nFinalSleepNo)
    {
        nDigit = nFinalSleepNo % 10;
        nFlagIndex[nDigit] = 1;
        nFinalSleepNo = nFinalSleepNo / 10;
    }
}

int calculateSleepNo(int nSleepNo)
{
    int nFinalSleepNo = 0;
    int nMultipleNo = 1;
    int nFlagIndex[10] = {0};
    bool nEndSearch = true;
    while(nEndSearch)
    {
        nFinalSleepNo = nMultipleNo * nSleepNo;
        if(nFinalSleepNo == 0)
        {
            nFinalSleepNo = -1;
            break;
        }
        parseNoFillArray(nFinalSleepNo, nFlagIndex);
        nEndSearch = !checkCountCompleted(nFlagIndex);
        nMultipleNo++;
    }
    return nFinalSleepNo;
}

int main()
{
    cout << "..........Sleep............" << endl;
    FILE *fpIn = fopen("/home/naveen/Jam/Input.txt","r");
    FILE *fpOut = fopen("/home/naveen/Jam/Output.txt","w");
    int nTestCaseIndex = 0;
    int nTestCaseNo = 1;
    int nSleepNo = 0;
    fscanf(fpIn,"%d",&nTestCaseNo);
    while(!(nTestCaseIndex>=nTestCaseNo))
    {
        nTestCaseIndex++;
        fscanf(fpIn,"%d",&nSleepNo);
        int nFinalSleepIndex = calculateSleepNo(nSleepNo);
        if(nFinalSleepIndex == -1)
        {
            fprintf(fpOut,"Case #%d: INSOMNIA\n",nTestCaseIndex);
        }
        else
        {
            fprintf(fpOut,"Case #%d: %d\n",nTestCaseIndex, nFinalSleepIndex);
        }
    }
    fclose(fpIn);
    fclose(fpOut);
    return 0;
}

