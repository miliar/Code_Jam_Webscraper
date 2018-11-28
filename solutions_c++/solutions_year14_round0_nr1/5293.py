#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    ifstream input("A-small-attempt0.in");
    //ifstream input(".in");
    ofstream output("output.txt");
    int firstCardSet[16];
    int secondCardSet[16];
    int testCases;
    input>>testCases;
    for(int i=1;i<=testCases;i++)
    {
        int firstRow,secondRow;
        input>>firstRow;
        for(int j=0;j<16;j++)
            input>>firstCardSet[j];

        input>>secondRow;
        for(int j=0;j<16;j++)
            input>>secondCardSet[j];

        int firstChosenRow[4],secondChosenRow[4];
        for(int j=0;j<4;j++)
        {
            firstChosenRow[j]=firstCardSet[j+((firstRow-1)*4)];
            secondChosenRow[j]=secondCardSet[j+((secondRow-1)*4)];
        }

        int answer=-1;
        for(int j=0;j<4;j++)
        {
            if(firstChosenRow[0]==secondChosenRow[j])
            {
                if(answer==-1)
                    answer=firstChosenRow[0];
                else
                {
                    answer=-2;
                    break;
                }
            }
            if(firstChosenRow[1]==secondChosenRow[j])
            {
                if(answer==-1)
                    answer=firstChosenRow[1];
                else
                {
                    answer=-2;
                    break;
                }
            }
            if(firstChosenRow[2]==secondChosenRow[j])
            {
                if(answer==-1)
                    answer=firstChosenRow[2];
                else
                {
                    answer=-2;
                    break;
                }
            }
            if(firstChosenRow[3]==secondChosenRow[j])
            {
                if(answer==-1)
                    answer=firstChosenRow[3];
                else
                {
                    answer=-2;
                    break;
                }
            }
        }
        output<<"Case #"<<i<<": ";
        if(answer==-1)      output<<"Volunteer cheated!";
        else if(answer==-2) output<<"Bad magician!";
        else                output<<answer;
        output<<endl;
    }
    return 0;
}
