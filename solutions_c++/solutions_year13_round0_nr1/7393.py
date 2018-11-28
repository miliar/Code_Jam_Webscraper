#include <iostream>
#include <iomanip>
#include <string.h>
#include <cstdlib>
using namespace std;

char checkHorizontal(string board[4])
{
   for(int i = 0; i < 4; i++)
   {
      if (board[i] == "XXXX" || board[i] == "XXXT" || board[i] == "XXTX" || board[i] == "XTXX" || board[i] == "TXXX") return 'X';
      if (board[i] == "OOOO" || board[i] == "OOOT" || board[i] == "OOTO" || board[i] == "OTOO" || board[i] == "TOOO") return 'O';
   }
   return 'N';
}
char checkVertical(string board[4])
{
    for(int i = 0; i < 4; i++)
    {
       if((board[0][i] == 'X' || board[0][i] == 'T') && (board[1][i] == 'X' || board[1][i] == 'T') && (board[2][i] == 'X' || board[2][i] == 'T') && (board[3][i] == 'X' || board[3][i] == 'T')) return 'X';
       if((board[0][i] == 'O' || board[0][i] == 'T') && (board[1][i] == 'O' || board[1][i] == 'T') && (board[2][i] == 'O' || board[2][i] == 'T') && (board[3][i] == 'O' || board[3][i] == 'T')) return 'O';
    }
return 'N';
}
char checkDiaganol(string board[4])
{
   if((board[0][0] == 'X' || board[0][0] == 'T') && (board[1][1] == 'X' || board[1][1] == 'T') && (board[2][2] == 'X' || board[2][2] == 'T') && (board[3][3] == 'X' || board[3][3] == 'T')) return 'X';
   if((board[0][0] == 'O' || board[0][0] == 'T') && (board[1][1] == 'O' || board[1][1] == 'T') && (board[2][2] == 'O' || board[2][2] == 'T') && (board[3][3] == 'O' || board[3][3] == 'T')) return 'O';
   if((board[0][3] == 'X' || board[0][3] == 'T') && (board[1][2] == 'X' || board[1][2] == 'T') && (board[2][1] == 'X' || board[2][1] == 'T') && (board[3][0] == 'X' || board[3][0] == 'T')) return 'X';
   if((board[0][3] == 'O' || board[0][3] == 'T') && (board[1][2] == 'O' || board[1][2] == 'T') && (board[2][1] == 'O' || board[2][1] == 'T') && (board[3][0] == 'O' || board[3][0] == 'T')) return 'O';
   return 'N';
}

char checkComplete(string board[4])
{
   for(int i = 0; i < 4; i++)
   {
      if(board[i][0] == '.' || board[i][1] == '.' || board[i][2] == '.' || board[i][1] == '.') return 'N';
   }
return 'T';
}

int main()
{
   char check;
   int testCases = 0;
   string message;
   string board[4];
   char blank;

   cin >> testCases;
   cin.get(blank);
   for(int i = 0; i < testCases; i++)
   {
      for(int j = 0; j < 4; j++)
      {
         cin >> board[j];
      }
      check =  checkDiaganol(board);
      if (check == 'N')
      check = checkHorizontal(board);
      if (check == 'N')
      check = checkVertical(board);
      if (check == 'N')
      check = checkComplete(board);
      if (check == 'X') message = "X won";
      if (check == 'O') message = "O won";
      if (check == 'T') message = "Draw";
      if (check == 'N') message = "Game has not completed";
      cout << "Case #" << i+1 << ": " << message << endl;
   }

   return 0;
}
