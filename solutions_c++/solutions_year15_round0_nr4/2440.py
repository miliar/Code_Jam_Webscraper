#include <iostream>

using namespace std;

char x3[4][4] = {
  {'R', 'R', 'R', 'R'},
  {'R', 'R', 'G', 'R'},
  {'R', 'G', 'G', 'G'},
  {'R', 'R', 'G', 'R'}
};

char x4[4][4] = {
  {'R', 'R', 'R', 'R'},
  {'R', 'R', 'R', 'R'},
  {'R', 'R', 'R', 'G'},
  {'R', 'R', 'G', 'G'}
};
  

int main(){
  int cn, ci;
  int x, r, c;
  char win;
  
  cin >> cn;

  for(ci=1; ci<=cn; ++ci){
    cin >> x >> r >> c;

    if(x==1){
      win = 'G';
    }
    else if(x==2){
      if((r*c)%2){
	win = 'R';
      }
      else{
	win = 'G';
      }
    }
    else if(x==3){
      win = x3[r-1][c-1];
    }
    else if(x==4){
      win = x4[r-1][c-1];
    }

    cout << "Case #" << ci << ": ";

    cout << ((win == 'R')?"RICHARD":"GABRIEL");

    cout << "\n";
  }

  return 0;
}
