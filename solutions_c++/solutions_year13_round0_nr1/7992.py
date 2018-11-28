#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{

    ofstream fout ("A.out");
    ifstream fin ("A-small-attempt0.in");

    int number;

    fin >> number;

    char tic[4][4];
    string wonalpha;
    int won=0;
    bool winning=true;
    bool dot=false;
    bool ending = false;

    for(int i=1;i<=number;i++)
    {
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                fin >> tic[j][k];
                if(tic[j][k]=='.')
                    dot = true;

                if(k>0 && tic[j][k]!='.' && (tic[j][k]==tic[j][k-1]||tic[j][k]=='T') && winning && !ending)
                {
                    won+=1;
                    if(tic[j][k]!='T')
                        wonalpha=tic[j][k];
                }

                else if(k>0)
                {
                    winning = false;
                    won = 0;
                }
            }
            if(won==3)
                ending=true;

            won = 0;
            winning = true;
        }

        if(ending)
            fout << "Case #" << i << ": " << wonalpha << " won" << endl;

        else
        {
            for(int k=0;k<4;k++)
            {
                for(int j=0;j<4;j++)
                {
                    if(j>0 && tic[j][k]!='.' && (tic[j][k]==tic[j-1][k] || tic[j][k]=='T') && winning && !ending)
                    {
                        won+=1;
                        if(tic[j][k]!='T')
                            wonalpha=tic[j][k];
                    }
                    else if(j>0)
                    {
                        winning = false;
                        won = 0;
                    }
                }
                if(won==3)
                    ending=true;

                won = 0;
                winning = true;
            }
            if(ending)
                fout << "Case #" << i << ": " << wonalpha << " won" << endl;
            else
            {
                if((tic[0][0]=='O'||tic[0][0]=='T') && (tic[1][1]=='O'||tic[1][1]=='T') && (tic[2][2]=='O'||tic[2][2]=='T') && (tic[3][3]=='O'||tic[3][3]=='T'))
                    fout << "Case #" << i << ": " << "O" << " won" << endl;
                else if((tic[0][0]=='W'||tic[0][0]=='T') && (tic[1][1]=='W'||tic[1][1]=='T') && (tic[2][2]=='W'||tic[2][2]=='T') && (tic[3][3]=='W'||tic[3][3]=='T'))
                    fout << "Case #" << i << ": " << "W" << " won" << endl;
                else if((tic[0][3]=='O'||tic[0][3]=='T') && (tic[1][2]=='O'||tic[1][2]=='T') && (tic[2][1]=='O'||tic[2][1]=='T') && (tic[3][0]=='O'||tic[3][0]=='T'))
                    fout << "Case #" << i << ": " << "O" << " won" << endl;
                else if((tic[0][3]=='W'||tic[0][3]=='T') && (tic[1][2]=='W'||tic[1][2]=='T') && (tic[2][1]=='W'||tic[2][1]=='T') && (tic[3][0]=='W'||tic[3][0]=='T'))
                    fout << "Case #" << i << ": " << "W" << " won" << endl;
                else if(!dot)
                    fout << "Case #" << i << ": " << "Draw" << endl;
                else
                    fout << "Case #" << i << ": " << "Game has not completed" << endl;
            }
        }
        dot = false;
        won = 0;
        winning = true;
        ending = false;
    }


    return 0;

}
