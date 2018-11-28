#include<iostream>
#include<string>
#include<vector>
#include <climits>

using namespace std;

int main() {
  vector<string> board;
  int tc=0;
  int tcn=1;
  int i;
  cin >> tc;
  cin.ignore(INT_MAX, '\n'); 
  for(;tc>0;tc--,tcn++) {
    string tmp;
    char who_won='U';
    int tmp1;    
    board.clear();
    for(tmp1=0;tmp1<4;tmp1++) {      
      getline(cin,tmp);
      board.push_back(tmp);
    }
    getline(cin,tmp);
    //row
    for(i=0;i<4;i++) {
      int rcountx=0,rcounto=0,j;
      for(j=0;j<4;j++) {
	if(board[i][j] == 'X' || board[i][j] == 'T') {
	  rcountx++;
	}
	if(board[i][j] == 'O' || board[i][j] == 'T') {
	  rcounto++;
	}

      }
      if(rcountx==4) {
	who_won='X';
	break;
      }
      else if(rcounto == 4) {
	who_won='O';
	break;
      }
    }
    if(who_won != 'U') {
      cout << "Case #" <<tcn<<": "<<who_won<<" won"<<endl;
      continue;
    }
    //column
    for(i=0;i<4;i++) {
      int ccountx=0, ccounto=0,j;
      for(j=0;j<4;j++) {
	if(board[j][i] == 'X' || board[j][i] == 'T') {
	  ccountx++;
	}
	if(board[j][i] == 'O' || board[j][i] == 'T') {
	  ccounto++;
	}

      }
      if(ccountx==4) {
	who_won='X';
	break;
      }
      else if(ccounto==4) {
	who_won='O';
	break;
      }
    }
    if(who_won != 'U') {
      cout << "Case #" <<tcn<<": "<<who_won<<" won"<<endl;
      continue;
    }
    int d1countx=0,d2countx=0;
    int d1counto=0,d2counto=0;
    for(i=0;i<4;i++) {
      if(board[i][i] == 'X' || board[i][i] == 'T') {
	d1countx++;
      }
      if(board[i][i] == 'O' || board[i][i] == 'T') {
	d1counto++;
      }
      if(board[i][3-i] == 'X' || board[i][3-i] == 'T') {
	d2countx++;
      }
      if(board[i][3-i] == 'O' || board[i][3-i] == 'T') {
	d2counto++;
      }
    }
    if(d1countx == 4 || d2countx == 4) {
      who_won='X';
    }
    else if(d1counto == 4 || d2counto == 4) {
      who_won='O';
    }
    if(who_won != 'U') {
      cout << "Case #" <<tcn<<": "<<who_won<<" won"<<endl;
      continue;
    }
    int found_dot=0;
    for(i=0;i<4;i++) {
      int j;
      for(j=0;j<4;j++) {
	if(board[i][j]=='.') {
	  found_dot=1;
	  break;
	}
      }
      if(found_dot)
	break;
    }
    if(found_dot) {
      cout << "Case #" <<tcn<<": Game has not completed"<<endl;
      continue;
    }
    else {
       cout << "Case #" <<tcn<<": Draw"<<endl;
    }
  }
  return 0;
}


      

  