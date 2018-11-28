#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

void reverse(char* cPanString, int nCount, char cPrevChar)
{
    for(int nIndex=0;nIndex < nCount; ++nIndex)
    {
        cPanString[nIndex] = cPrevChar;
    }
}

void makePanHappy(char *cPanString, int &nPanShifts)
{
    int nPanLen = strlen(cPanString);
    bool bMinFound = false;
    char ch = '\0';
    for(int nIndex = 0; nIndex < nPanLen; ++nIndex)
    {
        ch = cPanString[nIndex];
        if(ch == '-')
        {
            bMinFound = true;
            cPanString[nIndex] = '+';
        }
    }
    if(bMinFound)
        nPanShifts++;
}

int calculatePanShifts(char* cPanString)
{
    char ch = '\0';
    char cPrevChar = '\0';
    int nCount = 0;
    int nPanShifts = 0;
    cPrevChar = cPanString[nCount];
    while((ch = cPanString[nCount++])!= '\0')
    {
         if(cPrevChar != ch)
         {
             reverse(cPanString, nCount, ch);
             nPanShifts++;
         }
         cPrevChar = ch;
    }
    makePanHappy(cPanString, nPanShifts);
    return nPanShifts;
}

int main()
{
    cout << "................PanCake................" << endl;


    FILE *fpIn = fopen("/home/naveen/cake/Input.txt","r");
    FILE *fpOut = fopen("/home/naveen/cake/Output.txt","w");
    int nTestCaseIndex = 0;
    int nTestCaseNo = 1;
    char cPanString[100] = {0};
    int nPanShifts = 0;
    fscanf(fpIn,"%d",&nTestCaseNo);
    while(!(nTestCaseIndex>=nTestCaseNo))
    {
        nPanShifts = 0;
        nTestCaseIndex++;
        fscanf(fpIn,"%s",cPanString);
        nPanShifts = calculatePanShifts(cPanString);
        fprintf(fpOut,"Case #%d: %d\n",nTestCaseIndex, nPanShifts);
    }
    fclose(fpIn);
    fclose(fpOut);

    return 0;
}

