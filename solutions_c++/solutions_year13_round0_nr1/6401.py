#include <iostream>

using namespace std;

/*typedef enum tableState{
  Dot = 0,
  X = 1,
  O = 2,
  T = 3} state;*/

int c2s(char c){
  switch(c){
  case '.': return 0;
  case 'X': return 1;
  case 'O': return 2;
  case 'T': return 3;
  }
}

char s2c(int s){
  switch(s){
  case 0  : return '.';
  case 1  : return 'X';
  case 2  : return 'O';
  case 3  : return 'T';
  default : return '\0';
  }
}

int main(void){
  int n, n0;
  int table[4][4];
  char buf[5], c;

  cin >> n;
  n0 = n;
  while(n--){
    for(int i = 0; i < 4; ++i){
      cin >> buf;
      for(int j = 0; j < 4; ++j)
	table[i][j] = c2s(buf[j]);
    }
    int cur0,cur1;
    
    for(int i = 0; i < 4; ++i){
      cur0 = table[i][0], cur1 = table[0][i];
      for(int j = 0; j < 4; ++j){
	cur0 = cur0 & (int)table[i][j];
	cur1 &= table[j][i];
      }
      if(cur0 || cur1)
	break;
    }

    if(!cur0 && !cur1){
      //Diagonal
      cur0 = table[0][0];
      cur1 = table[0][3];
      for(int i = 0; i < 4; ++i){
	cur0 = cur0 & table[i][i];
	cur1 &= table[i][3 - i];
      }
    }
    c = 0;
    if(cur0 != 0)
      c = s2c(cur0);
    if(cur1 != 0)
      c = s2c(cur1);
    cout << "Case #" << n0 - n << ": ";
    if(c)
      cout << c << " won" << endl;
    else{
      for(int i = 0; i < 4; ++i){
	for(int j = 0; j < 4; ++j){
	  if(table[i][j] == 0){
	    cout << "Game has not completed" << endl;
	    c = '.';
	    break;
	  }
	}
	if(c) break;
      }
      if(!c) cout << "Draw" << endl;
    }
  }
}
