#include <iostream>
#include <fstream>
#define long int
using namespace std;

int main()
{
    ifstream in;
    in.open("D-small-attempt0.in");
    ofstream out;
    out.open("D-small-attempt0.out");
    unsigned short tests, currentTest=0;
    in>>tests;
    while(currentTest++<tests)
    {
        unsigned int generatorTilesNo, complexity, studentsNo;
        in>>generatorTilesNo>>complexity>>studentsNo;
        out<<"Case #"<<currentTest<<":";
        if(complexity==1)
        {
            if(studentsNo<generatorTilesNo) out<<" IMPOSSIBLE";
            else for(int i=1; i<=studentsNo; i++) out<<" "<<i;
        }
        else
        {
            if(studentsNo>=generatorTilesNo) // we get the exact pattern
                for(int i=1;i<=studentsNo;i++)
                    out<<" "<<(complexity-1)*generatorTilesNo*(i-1)+i;
            else
            if(studentsNo==generatorTilesNo-1)
                for(int i=1;i<=studentsNo;i++)
                    out<<" "<<(complexity-1)*generatorTilesNo*(i-1)+i+1;
            else out<<" IMPOSSIBLE";
        }
        out<<endl;
    }

    in.close();
    out.close();
}
