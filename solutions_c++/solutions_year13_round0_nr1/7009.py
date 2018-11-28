#include <iostream>

using namespace std;

int main() {
  int cases;
  cin >> cases;
  for(int c = 1; c <= cases; c++){
    string line[4];
    bool emptySpaces = false;
    bool somebodyWon = false;
    for(int i = 0; i < 4; i++)
      cin >> line[i];

    cout << "Case #"<< c <<": ";

    //horizontal
    for(int i =0; i < 4; i++){
      int xcount = 0, ocount = 0;
      for(int j = 0; j < 4; j++){
        emptySpaces = emptySpaces || line[i][j] == '.';
        switch(line[i][j]) {
          case 'X': xcount++;
                    ocount = 0;
          break;
          case 'O': ocount++;
                    xcount = 0;
          break;
          case 'T': xcount++;
                    ocount++;
        }
      }
      if(xcount == 4){
        cout << "X won" << endl;
        somebodyWon = true;
        break;
      } else if(ocount == 4){
        cout << "O won" << endl;
        somebodyWon = true;
        break;
      }
    }
    
    if(somebodyWon)
      continue;
    
    //vertical
    for(int j =0; j < 4; j++){
      int xcount = 0, ocount = 0;
      for(int i = 0; i < 4; i++){
        switch(line[i][j]) {
          case 'X': xcount++;
                    ocount = 0;
          break;
          case 'O': ocount++;
                    xcount = 0;
          break;
          case 'T': xcount++;
                    ocount++;
        }
      }
      if(xcount == 4){
        cout << "X won" << endl;
        somebodyWon = true;
        break;
      } else if(ocount == 4){
        cout << "O won" << endl;
        somebodyWon = true;
        break;
      }
    }
    
    if(somebodyWon)
      continue;
  
    // diagonal
    int dir[] = {0,3};
    for(int d = 0; d < 2; d++) {
      int xcount = 0, ocount = 0;
      for(int i = 0; i < 4; i++)
        switch(line[i][abs(dir[d] -i)]) {
          case 'X': xcount++;
                    ocount = 0;
          break;
          case 'O': ocount++;
                    xcount = 0;
          break;
          case 'T': xcount++;
                    ocount++;
        }
      if(xcount == 4){
        cout << "X won" << endl;
        somebodyWon = true;
        break;
      } else if(ocount == 4){
        cout << "O won" << endl;
        somebodyWon = true;
        break;
      } 
    }

    if(somebodyWon)
      continue;
  
    if(emptySpaces)
      cout << "Game has not completed" << endl;
    else
      cout << "Draw" << endl;
  }
  return 0;
}
