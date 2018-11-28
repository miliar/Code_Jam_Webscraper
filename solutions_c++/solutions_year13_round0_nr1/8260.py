#include <iostream>
#include <string>
using namespace std;

int main() {
  int t;
  cin >> t;
  string output[t];
  char board[4][4];
  for(int i=0;i<t;i++) {
    for(int j=0;j<4;j++)
      for(int k=0;k<4;k++)
	cin >> board[j][k];
    bool found = false, dotFound = false;
    for(int j=0;j<4;j++) {
      char ch;
      if(board[j][0] == 'X' || (board[j][0] == 'T' && board[j][1] == 'X'))
	ch = 'X';
      else if(board[j][0] == 'O' || (board[j][0] == 'T' && board[j][1] == 'O'))
	ch = 'O';
      if(board[j][0] != '.') {
	for(int k=1;k<4;k++) {
	  if(board[j][k] == '.') {
	    dotFound = true;
	    break;
	  }
	  if(board[j][k] != ch && board[j][k] != 'T')
	    break;
	  if(k==3) {
	    if(ch == 'X')
	      output[i] = "X won";
	    else
	      output[i] = "O won";
	    found = true;
	  }
	}
      } else 
	dotFound = true;
      if(found == true)
	break;
    }
    if(found == false) {
      for(int j=0;j<4;j++) {
	char ch;
	if(board[0][j] == 'X' || (board[0][j] == 'T' && board[1][j] == 'X'))
	  ch = 'X';
	else if(board[0][j] == 'O' || (board[0][j] == 'T' && board[1][j] == 'O'))
	  ch = 'O';
	if(board[0][j] != '.') {
	  for(int k=1;k<4;k++) {
	    if(board[k][j] == '.') {
	      dotFound = true;
	      break;
	    }
	    if(board[k][j] != ch && board[k][j] != 'T')
	      break;
	    if(k==3) {
	      if(ch == 'X')
		output[i] = "X won";
	      else
		output[i] = "O won";
	      found = true;
	    }
	  }
	} else 
	  dotFound = true;
	if(found == true)
	  break;
      }
    }
    if(found == false) {
      char ch;
      if(board[0][0] == 'X' || (board[0][0] == 'T' && board[1][1] == 'X'))
	  ch = 'X';
	else if(board[0][0] == 'O' || (board[0][0] == 'T' && board[1][1] == 'O'))
	  ch = 'O';
      if(board[0][0] != '.') {
	for(int j=1;j<4;j++) {
	  if(board[j][j] == '.') {
	    dotFound = true;
	    break;
	  }
	  if(board[j][j] != ch && board[j][j] != 'T')
	    break;
	  if(j==3) {
	    if(ch == 'X')
	      output[i] = "X won";
	    else
	      output[i] = "O won";
	    found = true;
	  }
	}
      } else 
	dotFound = true;
    }
    if(found == false) {
      char ch;
      if(board[3][0] == 'X' || (board[3][0] == 'T' && board[2][1] == 'X'))
	  ch = 'X';
	else if(board[3][0] == 'O' || (board[3][0] == 'T' && board[2][1] == 'O'))
	  ch = 'O';
      if(board[3][0] != '.') {
	for(int j=1,k=2;j<4;j++,k--) {
	  if(board[j][k] == '.') {
	    dotFound = true;
	    break;
	  }
	  if(board[j][k] != ch && board[j][k] != 'T')
	    break;
	  if(j==3 && k==0) {
	    if(ch == 'X')
	      output[i] = "X won";
	    else
	      output[i] = "O won";
	    found = true;
	  }
	}
      } else 
	dotFound = true;
    }
    if(found == false) {
      if(dotFound == true)
	output[i] = "Game has not completed";
      else
	output[i] = "Draw";
    }
    //cout << endl;
  }
  for(int i=0;i<t;i++)
    cout << "Case #" << i+1 << ": " << output[i] << endl;
  return 0;
}
