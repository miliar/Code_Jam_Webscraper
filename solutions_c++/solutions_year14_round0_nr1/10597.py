#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

int main()
{
    int cases;
    char input[5];
    int grid1[4][4], grid2[4][4];
    ifstream fin("A-small-attempt0.in");
    ofstream fout("output.txt");
    fin>>input;
    cases=atoi(input);
    int store[4];

    for(int i=0; i < cases; i++)
    {
        int row1,row2;
        fin>>input;
        row1=atoi(input);
        row1--;
        for(int j=0; j<4; j++)
        {
            for(int k=0; k<4; k++)
            {
                fin>>input;
                grid1[j][k]=atoi(input);
            }
        }

        fin>>input;
        row2=atoi(input);
        row2--;

        for(int j=0; j<4; j++)
        {
            for(int k=0; k<4; k++)
            {
                fin>>input;
                grid2[j][k]=atoi(input);
            }
        }

        int matches=0;
        int match;
        for(int j=0; j<4; j++)
        {
            for(int k=0; k<4; k++)
            {
                if(grid1[row1][j]==grid2[row2][k])
                {
                    match=grid1[row1][j];
                    matches++;
                }
            }
        }
        if(matches>1)
        {
            fout<<"Case #"<<i+1<<": "<<"Bad magician!\n";
        }
        else if(matches==0)
        {
            fout<<"Case #"<<i+1<<": "<<"Volunteer cheated!\n";
        }
        else
        {
            fout<<"Case #"<<i+1<<": "<<match<<endl;
        }


    }

}
