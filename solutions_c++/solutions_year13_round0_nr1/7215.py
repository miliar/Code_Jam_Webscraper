#include <iostream>

using namespace std;

int main( int argc, const char* argv[] ){
  string board[4];
  int count;
  cin >> count;

  for(int a = 0; a < count; ++a){
    getline(cin, board[0]);
    for(int i = 0; i < 4; i++)
      getline(cin, board[i]);


    bool diagR = false, diagL, fin = false, empty = false;

    int XDiagL = 0, XDiagR = 0, ODiagL = 0, ODiagR = 0;
    for(int i = 0; i < 4; ++i){
      int XVert = 0, XHorz = 0, OVert = 0, OHorz = 0;
      for(int x = 0; x < 4; ++x){
        diagR = i == x ? true : false;
        diagL = ((x == 3 && i == 0) || ( i == 3 && x ==  0) ||
          (x == 1 && i ==  2) || (i == 1 && x == 2) ? true : false);
        if(board[i][x] == 'X' || board[i][x] == 'T'){
          ++XVert;
          XDiagL += diagL ? 1 : 0;
        }
        if(board[i][x] == 'O' || board[i][x] == 'T'){
          ++OVert;
          ODiagL += diagL ? 1 : 0;
        }
        if(board[x][i] == 'X' || board[x][i] == 'T'){
          ++XHorz;
          XDiagR += diagR ? 1 : 0;
        }
        if(board[x][i] == 'O' || board[x][i] == 'T'){
          ++OHorz;
          ODiagR += diagR ? 1 : 0;          
        }
        if(board[x][i] == '.' || board[i][x] == '.')
          empty = true;
      }
      if(OVert == 4 || OHorz == 4 || ODiagL == 4 || ODiagR == 4 || XVert == 4 || XHorz == 4 || XDiagL == 4 || XDiagR == 4)
        cout << "Case #" << a + 1 << ": ";
      if(XVert == 4 || XHorz == 4 || XDiagL == 4 || XDiagR == 4){
        cout << "X won\n";
        fin = true;
        break;
      }

      if(OVert == 4 || OHorz == 4 || ODiagL == 4 || ODiagR == 4){
        cout << "O won\n";
        fin = true;
        break;
      }
    }
    if(fin == false){
      cout << "Case #" << a + 1<< ": ";
      if(empty == true)
        cout << "Game has not completed\n";
      else
        cout << "Draw\n";
      }
  }
  return 0;
}