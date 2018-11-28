#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
using namespace std;

int main(){
  ofstream Outfile;
  Outfile.open("Output.out");
  char board[4][4];
  int times;
  bool fin = false;
  char winner;
  bool unfin = false;
  string hold;
  cin >> times;
  for(int x = 1; x<=times; x++){
    for(int i = 0; i<4; i++){
        cin >> hold;
        for(int z=0; z<4; z++){
          board[i][z] = hold[z];
        }
    }
    fin = false;
    unfin = false;

    //Horizontal Checks
    char check;
    int count = 0;
    for(int i = 0; i < 4; i++){
      count = 0;
      check = board[i][0];
      for(int q = 1; q<4; q++){
        if(check == '.'){ 
          unfin = true;
          break;
        }
        if(check == 'T'){
          check = board[i][q];
        }
        if(board[i][q] == check || board[i][q] == 'T'){
          count++;
        }
        if(board[i][q] == '.'){
          unfin = true;
        }
      }
      if(count == 3){
        fin = true;
        winner = check;
        break;
      }
    }
    
    //Verticle Checks
    for(int i = 0; i < 4; i++){
      count = 0;
      check = board[0][i];
      for(int q = 1; q<4; q++){
        if(check == '.') break;
        if(check == 'T'){
          check = board[q][i];
        }
        if(board[q][i] == check || board[q][i] == 'T'){
          count++;
        }
      }
      if(count == 3){
        fin = true;
        winner = check;
      }
    }

    //Diagonals
    count = 0;
    check = board[0][0];
    for(int q = 1; q<4; q++){
      if(check == '.') break;
      if(check == 'T'){
        check = board[q][q];
      }
      if(board[q][q] == check || board[q][q] == 'T'){
        count++;
      }
    }
    if(count == 3){
      fin = true;
      winner = check;
    }
    
    count = 0;
    check = board[0][3];
    for(int q = 1; q<4; q++){
      if(check == '.') break;
      if(check == 'T'){
        check = board[q][3-q];
      }
      if(board[q][3-q] == check || board[q][3-q] == 'T'){
        count++;
      }
    }
    if(count == 3){
      fin = true;
      winner = check;
    }

    Outfile << "Case #" << x <<": ";
    if(fin){
      Outfile <<winner<<" won"<<endl;
    }else if(!fin && unfin){
      Outfile <<"Game has not completed"<<endl;
    }else{
      Outfile << "Draw"<<endl;
    }
  }
  Outfile.close();
}
