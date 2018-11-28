#include <iostream>
#include <fstream>

using namespace std;

int main()
{
   int T,X=1;

    ifstream fin("A-small-attempt0.in");
    ofstream fout("A-small-attempt0.out");

    fin >> T;

    while(T-->0)
    {
        int ans1,ans2,firstArrangement[4][4],secondArrangement[4][4] ;
        fin >> ans1;
        for(int i=0;i<4;i++)
            for(int ii=0;ii<4;ii++)
                fin >> firstArrangement[i][ii] ;
        fin >> ans2;
        for(int i=0;i<4;i++)
            for(int ii=0;ii<4;ii++)
                fin >> secondArrangement[i][ii] ;

        int cEqAns=0,y=0;
        for(int i=0;i<4;i++) {
            for(int ii=0;ii<4;ii++) {
                if (firstArrangement[ans1-1][i]==secondArrangement[ans2-1][ii]) {
                    cEqAns++;
                    y=firstArrangement[ans1-1][i];
                }
            }
        }

        fout << "Case #" << X++ << ": ";
        if (cEqAns==0)
            fout << "Volunteer cheated!";
        if (cEqAns==1)
            fout << y;
        if (cEqAns>1)
            fout << "Bad magician!";
        fout << "\n";
    }
    return 0;
}
