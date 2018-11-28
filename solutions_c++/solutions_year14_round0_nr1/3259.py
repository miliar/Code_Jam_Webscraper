#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    int CaseNums,CaseNum=1, FirstRow, SecondRow, Arr1[4][4], Arr2[4][4],num;
    ifstream fin("A-small-attempt4.in");
	ofstream fout("namenum.out");
    fin>>CaseNums;
    while (CaseNum<=CaseNums){
        int casses=0;
        fin>>FirstRow;
        for(int i=0; i<4; i++)
            for(int j=0; j<4; j++)
                fin>>Arr1[i][j];
        fin>>SecondRow;
        for(int i=0; i<4; i++)
            for(int j=0; j<4; j++)
                fin>>Arr2[i][j];
        for (int i=FirstRow-1, j=0; j<4; j++){
            for (int k=SecondRow-1, l=0; l<4; l++){
                if(Arr1[i][j]==Arr2[k][l]){
                   num=Arr1[i][j];
                   casses++;
                }
            }
        }
        if(casses==1)
            fout<<"Case #"<<CaseNum<<": "<<num<<"\n";
        else if(casses>1)
            fout<<"Case #"<<CaseNum<<": Bad magician!\n";
        else
            fout<<"Case #"<<CaseNum<<": Volunteer cheated!\n";
        CaseNum++;
    }
    return 0;
}
