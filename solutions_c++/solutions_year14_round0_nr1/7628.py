#include <iostream>
#include <fstream>
#include <string>
#include <sys/stat.h>
#include <ios>
#include <string.h>
#include <time.h>

using namespace std;

int main()
{
    cout << "-----------------GCJ-----------------" << endl;

    const char* strInputFile = "./A-small-attempt1.in";
    const char* strOutputFile = "./A-small-attempt1.out";

    FILE* fpIn = fopen(strInputFile, "r");
    FILE* fpOut = fopen(strOutputFile, "w");

    int nTestCases = 0;
    fscanf(fpIn,"%d",&nTestCases);
    cout << "Test cases : " <<nTestCases << endl;


    for(int nTestCaseNo = 1; nTestCaseNo <= nTestCases; ++nTestCaseNo)
    {
        ////////////////////////////////////////////////////////
        int nFirstCardRow = -1;

        fscanf(fpIn,"%d",&nFirstCardRow);

        int pCardsFirst[4][4];

        for(int i=0;i<4;++i)
        {
            for(int j=0;j<4;++j)
            {
                fscanf(fpIn,"%d",&pCardsFirst[i][j]);
            }
        }

        int nSecondCardRow = -1;

        fscanf(fpIn,"%d",&nSecondCardRow);


        int pCardsSecond[4][4];

        for(int i=0;i<4;++i)
        {
            for(int j=0;j<4;++j)
            {
                fscanf(fpIn,"%d",&pCardsSecond[i][j]);
            }
        }
        //////////////////////////////////////////////

        int nIntersection = 0;
        int nSelectedCardNo = -1;
        for(int i=0;i<4;++i)
        {
            for(int j=0;j<4;++j)
            {
                int val1 = pCardsFirst[nFirstCardRow-1][i];
                int val2 = pCardsSecond[nSecondCardRow-1][j];
                if(val1 == val2)
                {
                    ++nIntersection;
                    nSelectedCardNo = val1;
                }
            }
        }

        if(nIntersection == 1)
        {
            fprintf(fpOut,"Case #%d: %d\n",nTestCaseNo,nSelectedCardNo);
        }
        else if(nIntersection > 1)
        {
            fprintf(fpOut,"Case #%d: Bad magician!\n",nTestCaseNo);
        }
        else if(nIntersection == 0)
        {
            fprintf(fpOut,"Case #%d: Volunteer cheated!\n",nTestCaseNo);
        }

    }
    fclose(fpIn);
    fclose(fpOut);
    cout << "-----------------GCJ-----------------" << endl;
    return 0;
}

