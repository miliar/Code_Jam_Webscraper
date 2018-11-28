#include <iostream>
#include <string>
using namespace std;

int main() {
  int t;
  cin >> t;
  string board[4];
  for (int ti = 0; ti < t; ti++) {
    for (int i = 0; i < 4; i++)
      cin >> board[i];
    bool oline = false, xline = false;
    bool completed = true;
    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++)
        if (board[i][j] == '.')
          completed = false;
      int ocount = 0, xcount = 0;
      for (int j = 0; j < 4; j++) {
        if (board[i][j] == 'O')
          ocount += 10;
        else if (board[i][j] == 'X')
          xcount += 10;
        else if (board[i][j] == 'T')
          ocount++, xcount++;
      }
      if (ocount >= 31)
        oline = true;
      if (xcount >= 31)
        xline = true;
      ocount = 0, xcount = 0;
      for (int j = 0; j < 4; j++) {
        if (board[j][i] == 'O')
          ocount += 10;
        else if (board[j][i] == 'X')
          xcount += 10;
        else if (board[j][i] == 'T')
          ocount++, xcount++;
      }
      if (ocount >= 31)
        oline = true;
      if (xcount >= 31)
        xline = true;
    }
    int ocount = 0, xcount = 0;
    for (int i = 0; i < 4; i++) {
      if (board[i][i] == 'O')
        ocount += 10;
      else if (board[i][i] == 'X')
        xcount += 10;
      else if (board[i][i] == 'T')
        ocount++, xcount++;
    }
    if (ocount >= 31)
      oline = true;
    if (xcount >= 31)
      xline = true;
    ocount = 0, xcount = 0;
    for (int i = 0; i < 4; i++) {
      if (board[i][3-i] == 'O')
        ocount += 10;
      else if (board[i][3-i] == 'X')
        xcount += 10;
      else if (board[i][3-i] == 'T')
        ocount++, xcount++;
    }
    if (ocount >= 31)
      oline = true;
    if (xcount >= 31)
      xline = true;
    if (oline)
      cout << "Case #"<<ti+1<<": O won"<<endl;
    else if (xline)
      cout << "Case #"<<ti+1<<": X won"<<endl;
    else if (completed)
      cout << "Case #"<<ti+1<<": Draw"<<endl;
    else
      cout << "Case #"<<ti+1<<": Game has not completed"<<endl;
  }
  return 0;
}
