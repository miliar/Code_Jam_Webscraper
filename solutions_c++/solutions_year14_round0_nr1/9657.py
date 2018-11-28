#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int i,j,k,test_cases,ans,ans1,ans2,grid1[4][4],grid2[4][4],counter;
    fstream textfile;
    fstream outfile;
    textfile.open("A-small-attempt5.in");
    outfile.open("outputfile.txt");
    textfile >> test_cases;
    for(i=1 ; i<=test_cases ; i++)
    {
        textfile >> ans1;
        for(j=0;j<4;j++)
        {
            for(k=0;k<4;k++)
                textfile >> grid1[j][k];
        }
        textfile >> ans2;
        for(j=0;j<4;j++)
        {
            for(k=0;k<4;k++)
                textfile >> grid2[j][k];
        }
        counter = 0;
        for(j=0;j<4;j++)
        {
            for(k=0;k<4;k++)
            {
                if(grid1[ans1-1][j] == grid2[ans2-1][k])
                {
                    ans = grid1[ans1-1][j];
                    counter++;
                }
            }
        }
        if(counter == 1)
            outfile <<"Case #"<< i <<": "<< ans <<endl;
        else if(counter > 1)
            outfile <<"Case #"<< i <<": Bad magician!"<<endl;
        else
            outfile <<"Case #"<< i <<": Volunteer cheated!"<<endl;
    }
    return 0;
}
