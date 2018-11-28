#include <iostream>
#include <cstdlib>
using namespace std;
int CheckBoard(char [4][4],int);

int main()
{
    int i,j;
    int CurrentCase;
    char Board[4][4];

    int NumberOfCases;
    cout << "Paste input please :\n";
    cin>>NumberOfCases;
    for (CurrentCase=1;CurrentCase<=NumberOfCases;CurrentCase++)
    {
       for(i =0;i<4;i++)
        {
         cin >> Board[i][0];
         cin >> Board[i][1];
         cin >> Board[i][2];
         cin >> Board[i][3];
        }
        CheckBoard(Board,CurrentCase);
    }
system("Pause");
}
int CheckBoard(char Board[4][4],int CurrentCase)
{
 int i,j;
bool T=0;
int Xcounter=0;
int Ocounter=0;

    //check row
       for(i =0;i<4;i++)
       {
         for (j =0;j<4;j++)
          {
             if (Board[i][j]=='X')Xcounter++;
            else if (Board[i][j]=='O')Ocounter++;
            else if (Board[i][j]=='T')T=1;
             if ((Xcounter==4) ||(Xcounter==3 &&T)) {cout << "Case #"  <<CurrentCase<< ": X won\n"; return 0;}
             else if ((Ocounter==4) ||(Ocounter==3 &&T)) {cout << "Case #" <<CurrentCase<< ": O won\n"; return 0;}
       }
        Xcounter=0;
        Ocounter=0;
        T=0;
       }
    //check column
        for(i =0;i<4;i++)
       {
         for (j =0;j<4;j++)
          {
             if (Board[j][i]=='X')Xcounter++;
            else if (Board[j][i]=='O')Ocounter++;
            else if (Board[j][i]=='T')T=1;
             if ((Xcounter==4) ||(Xcounter==3 &&T)) {cout << "Case #" <<CurrentCase << ": X won\n";return 0;}
             else if ((Ocounter==4) ||(Ocounter==3 &&T)) {cout << "Case #"<<CurrentCase << ": O won\n";return 0;}
       }
        Xcounter=0;
        Ocounter=0;
        T=0;
       }
    //check diagonal
       for(i =0;i<4;i++) //[0][0],[1][1],[2][2],[3][3]
       {

             if (Board[i][i]=='X')Xcounter++;
            if (Board[i][i]=='O')Ocounter++;
           if (Board[i][i]=='T')T=1;

             if ((Xcounter==4) ||(Xcounter==3 &&T)) {cout << "Case #" <<CurrentCase << ": X won\n";return 0;}
             else if ((Ocounter==4) ||(Ocounter==3 &&T)) {cout << "Case #"<<CurrentCase << ": O won\n";return 0;}

       }
         Xcounter=0;
        Ocounter=0;
        T=0;
      for(i =3;i>=0;i--) //[3][0],[2][1],[1][2],[0][3]
       {
            //cout <<Board[i][3-i];
             if (Board[i][3-i]=='X')Xcounter++;
            else if (Board[i][3-i]=='O')Ocounter++;
            else if (Board[i][3-i]=='T')T=1;
             if ((Xcounter==4) ||(Xcounter==3 &&T)) {cout << "Case #" <<CurrentCase << ": X won\n";return 0;}
             else if ((Ocounter==4) ||(Ocounter==3 &&T)) {cout << "Case #"<<CurrentCase << ": O won\n";return 0;}

       }
    //check if game is completerd
for (int i=0; i<4; i++)
	for (int j=0; j<4; j++)
		if (Board[i][j] == '.') {cout << "Case #" << CurrentCase << ": Game has not completed\n";return 0;}

cout << "Case #" << CurrentCase << ": Draw\n";return 0;;
}
