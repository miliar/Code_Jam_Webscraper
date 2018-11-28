#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <string>
using namespace std;

int T;
string s[4];
int board[4][4];

void debug()
{
  for(int i=0;i<4;i++,cout << endl)
    for(int j=0;j<4;cout<< board[i][j] << " ",j++);
}

int solve()
{
  int i,j,row,column,diag,tot=1,res;

  //  debug();

  for(i=0;i<4;i++)
    {
      row = board[i][0]*board[i][1]*board[i][2]*board[i][3];
      column = board[0][i]*board[1][i]*board[2][i]*board[3][i];
      tot *= row;

      if(row >0 || column>0)
	{
	  if(row == 16 || row == 8 || column == 16 || column == 8)
	    return 1;
	  else if(row == 27 || row == 81 || column == 27 || column == 81)
	    return 2;
	}
    }
  diag = board[0][0]*board[1][1]*board[2][2]*board[3][3];
  if(diag >0)
    {
      if(diag == 16 || diag == 8)
	return 1;
      else if(diag == 27 || diag == 81)
	return 2;
    }
   diag = board[0][3]*board[1][2]*board[2][1]*board[3][0];
   if(diag >0)
    {
      if(diag == 16 || diag == 8)
	return 1;
      else if(diag == 27 || diag == 81)
	return 2;
    }
   if(tot > 0)
     return 3;
   return 4;
}

int main()
{
  int i,j,k,res;
  string tmp;
  cin >> T;

  map < int , string>RES;
  RES[1] = "O won";
  RES[2] = "X won";
  RES[3] = "Draw";
  RES[4] = "Game has not completed";

  for(i=1;i<=T;i++)
    {
      for(j=0;j<4;j++)
	{
	  cin >> s[j];
          for(k=0;k<4;k++){
	    if(s[j][k] == 'T')
	      board[j][k] = 1;
	    else if(s[j][k] == 'X')
	      board[j][k] = 3;
	    else if(s[j][k] == 'O')
	      board[j][k] = 2;
	    else
	      board[j][k] = 0;
	  }
	}
      res = solve();
      //      cin >> tmp;
      //      cin >> tmp;
      cout << "Case #" << i << ": " << RES[res] << endl;
    }
}
