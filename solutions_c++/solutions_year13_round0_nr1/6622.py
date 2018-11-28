#include <iostream>
#include <fstream>
using namespace std;


char square[4][4];

char win;
int checker(char * line, int increment){
    bool allX = true; bool allO = true;
    int counter = 0;
    for (int f = 0; counter < 4; f += increment, counter ++) {
        if (line[f] != 'O' && line[f] != 'T') { allO = false;}
        if (line[f] != 'X' && line[f] != 'T') { allX = false;}
    }
    if (allX) { return -1;}
    if (allO) { return 1;}
    return 0;
}

int main()
{ ifstream fin("A-large.in");
ofstream fout("COMPLETEDLARGE.txt");
    int tc,t;
    fin >> tc;
    for (t=0;t<tc;t++)
    {bool winX = false; bool winO = false;
        for (int i=0;i<4;i++)
        {
            for (int j=0;j<4;j++)
            {
                fin>>square[i][j];
            }
        }
       cout<<endl;

        for (int l=0;l<4;l++){
            win = checker(square[l],1);

            if (win == 1){
                winO = true;
            } else if (win == -1){
                winX = true;
            }
        }


        for (int l=0;l<4;l++){
            win = checker(&square[0][l],4);

            if (win == 1){
                winO = true;
            } else if (win == -1){
                winX = true;
            }
        }


            win = checker(&square[0][0],5);

            if (win == 1){
                winO = true;
            } else if (win == -1){
                winX = true;
            }



            win = checker(&square[0][3],3);

            if (win == 1){
                winO = true;
            } else if (win == -1){
                winX = true;
            }




            bool incomplete = false;
            for (int x=0;x<4;x++){
                for(int y=0;y<4;y++){
                    if (square[x][y] == '.')
                    {
                        incomplete = true;
                    }
                }}

           if (winO){fout<<"Case #"<<t+1<<": O won"<<endl;}
           else if(winX){fout<<"Case #"<<t+1<<": X won"<<endl;}
         else if (incomplete){fout<<"Case #"<<t+1<<": Game has not completed"<<endl;}
          else{fout<<"Case #"<<t+1<<": Draw"<<endl;}
          }
          fin.close();

    return 0;
}
