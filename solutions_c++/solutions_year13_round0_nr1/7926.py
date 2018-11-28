#include <vector>
#include <iostream>

using namespace std;

int main(int argc, const char *argv[])
{
  int numBoards;
  cin >> numBoards;
  cin >> ws;
  for(int i=0; i<numBoards; i++) {
    string row1, row2, row3, row4, extra;
    getline(cin, row1, '\n');
    getline(cin, row2, '\n');
    getline(cin, row3, '\n');
    getline(cin, row4, '\n');
    vector<string> board;
    board.push_back(row1);
    board.push_back(row2);
    board.push_back(row3);
    board.push_back(row4);
    bool fullBoard = true, xWin = false, oWin = false;
    for(int j=0; j<4; j++) {
      if((board[0][j] == 'X' || board[0][j] == 'T') && 
          (board[1][j] == 'X' || board[1][j] == 'T') &&
          (board[2][j] == 'X' || board[2][j] == 'T') &&
          (board[3][j] == 'X' || board[3][j] == 'T') 
         ) xWin = true;
      if((board[0][j] == 'O' || board[0][j] == 'T') && 
          (board[1][j] == 'O' || board[1][j] == 'T') &&
          (board[2][j] == 'O' || board[2][j] == 'T') &&
          (board[3][j] == 'O' || board[3][j] == 'T') 
         ) oWin = true;
      if((board[j][0] == 'X' || board[j][0] == 'T') &&
         (board[j][1] == 'X' || board[j][1] == 'T') &&
         (board[j][2] == 'X' || board[j][2] == 'T') &&
         (board[j][3] == 'X' || board[j][3] == 'T')) xWin = true;
      if((board[j][0] == 'O' || board[j][0] == 'T') &&
         (board[j][1] == 'O' || board[j][1] == 'T') &&
         (board[j][2] == 'O' || board[j][2] == 'T') &&
         (board[j][3] == 'O' || board[j][3] == 'T')) oWin = true;
    }
    if(((board[0][0] == 'X' || board[0][0] == 'T') &&
        (board[1][1] == 'X' || board[1][1] == 'T') &&
        (board[2][2] == 'X' || board[2][2] == 'T') &&
        (board[3][3] == 'X' || board[3][3] == 'T')) ||
       ((board[0][3] == 'X' || board[0][3] == 'T') &&
        (board[1][2] == 'X' || board[1][1] == 'T') &&
        (board[2][1] == 'X' || board[2][2] == 'T') &&
        (board[3][0] == 'X' || board[3][0] == 'T')
       )) xWin = true;
    if(((board[0][0] == 'O' || board[0][0] == 'T') &&
        (board[1][1] == 'O' || board[1][1] == 'T') &&
        (board[2][2] == 'O' || board[2][2] == 'T') &&
        (board[3][3] == 'O' || board[3][3] == 'T')) ||
       ((board[0][3] == 'O' || board[0][3] == 'T') &&
        (board[1][2] == 'O' || board[1][1] == 'T') &&
        (board[2][1] == 'O' || board[2][2] == 'T') &&
        (board[3][0] == 'O' || board[3][0] == 'T')
       )) oWin = true;

    if(xWin) cout << "Case #" << (i+1) << ": X won" << endl;
    else if(oWin) cout << "Case #" << (i+1) << ": O won" << endl;
    else {
      for(int j=0; j<4; j++) for(int k=0; k<4; k++) if(board[j][k] == '.') fullBoard = false;
      cout << "Case #" << (i+1) << (fullBoard?": Draw":": Game has not completed") << endl;  
    }
    cin >> ws;
  } 
  return 0;
}
