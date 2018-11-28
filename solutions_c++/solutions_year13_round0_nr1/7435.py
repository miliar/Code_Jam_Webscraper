#include <iostream>
#include <string>
using namespace std;

int main(int argc,char **argv){
  int test;
  cin >> test;
  for(int tt = 1; tt <= test; tt++){
    string board[4];
    int oro[4] = {0},xr[4] = {0},tr[4] = {0};
    int oc[4] = {0},xc[4] = {0},tc[4] = {0};
    int od = 0,xd = 0,td = 0;
    int ow = 0,xw = 0;
    int isnotfull = 0;
 
    for(int i = 0; i < 4; i++)
      cin >> board[i];
    
    for(int i = 0; i < 4; i++){
      for(int j = 0; j < 4; j++){
		if(board[i][j] == 'O')
		  oro[i]++;
		else if(board[i][j] == 'X')
		  xr[i]++;
		else if(board[i][j] == 'T')
		  tr[i]++;
	  }
	  if(oro[i]+tr[i] == 4)
		ow = 1;
      else if(xr[i] + tr[i] == 4)
		xw = 1;
	  else if(xr[i]+oro[i]+tr[i] != 4)
		isnotfull = 1;
    }
    
    for(int i = 0; i < 4; i++){
      for(int j = 0; j < 4; j++){
	if(board[j][i] == 'O')
	  oc[i]++;
	else if(board[j][i] == 'X')
	  xc[i]++;
	else if(board[j][i] == 'T')
	  tc[i]++;
      }
      if(oc[i]+tc[i] == 4)
	ow = 1;
      else if(xc[i] + tc[i] == 4)
	xw = 1;
      else if(xc[i]+oc[i]+tc[i] != 4)
	isnotfull = 1;
    }

    for(int i = 0;i < 4; i++){
      if(board[i][i] == 'O')
	od++;
      else if(board[i][i] == 'X')
	xd++;
      else if(board[i][i] == 'T')
	td++;
    }
    if(od + td == 4)
      ow = 1;
    else if(xd + td == 4)
      xw = 1;
    else if(xd + td + od != 4)
      isnotfull = 1;
    

	od = xd = td = 0;
    for(int i = 0;i < 4; i++){
      if(board[i][3-i] == 'O')
	od++;
      else if(board[i][3-i] == 'X')
	xd++;
      else if(board[i][3-i] == 'T')
	td++;
    }
    if(od + td == 4)
      ow = 1;
    else if(xd + td == 4)
      xw = 1;
    else if(xd + td + od != 4)
      isnotfull = 1;
    
	cout << "Case #" << tt << ": " ;
    if(ow && !xw)
		cout << "O won" << endl;
	else if(xw && !ow)
		cout << "X won" << endl;
	else if( isnotfull)
		cout << "Game has not completed" << endl;
	else
		cout << "Draw" << endl;
    
    //skip empty line
    //cin >> board[0];
  }
}
