#include <iostream>
#include <string>

using namespace std;

string judgeWinner(char table[4][4]){
  string result;
  bool Xwon = false;
  bool Owon = false;
  bool complete = true;
  bool okay;

  for(int i=0;i<4;i++){
    for(int j=0;j<4;j++){
      if(table[i][j] == '.'){
	complete = false;
      }
    }
  }
  
  char symbol,fsymbol;

 
  //column check

  for(int i=0;i<4;i++){
    if(Xwon || Owon){
      continue;
    }
    okay = true;
    
    fsymbol = table[i][0];
    if(fsymbol == 'T'){
      fsymbol = table[i][1];
    }
    if(fsymbol == '.'){
      continue;
    }

    for(int k=1;k<4;k++){
      if(table[i][k] == 'T'){
	continue;
      }
      symbol = table[i][k];

      if(symbol != fsymbol){
	okay = false;
      }
    }

    if(okay){
      if(symbol == 'X'){
	Xwon = true;
      }
      else if(symbol == 'O'){
	Owon = true;
      }
    }
  }
  
  //row check
  for(int j=0;j<4;j++){
    if(Xwon || Owon){
      continue;
    }
    okay = true;
 
    fsymbol = table[0][j];
    if(fsymbol == 'T'){
      fsymbol = table[1][j];
    }
    if(fsymbol == '.'){
      continue;
    }

    for(int k=1;k<4;k++){
      if(table[k][j] == 'T'){
	continue;
      }
      symbol = table[k][j];
      
      if(symbol != fsymbol){
	okay = false;
      }
    }
    if(okay){
      
      if(symbol == 'X'){
	Xwon = true;
      }
      else if(symbol == 'O'){
	Owon = true;
      }
    }
  }

  //cross check
  if(!Xwon && !Owon){
    okay = true;
    fsymbol = table[0][0];
    if(fsymbol == 'T'){
      fsymbol = table[1][1];
    }
    for(int k=1;k<4;k++){
      if(table[k][k] == 'T'){
	continue;
      }
      symbol = table[k][k];
      if(symbol != fsymbol || symbol == '.'){
	okay = false;
      }
    }
    if(okay){
      if(symbol == 'X'){
	Xwon = true;
      }
      else if(symbol == 'O'){
	Owon = true;
      }
    }
  }


  //rev cross check
  if(!Xwon && !Owon){
    okay = true;
    fsymbol = table[0][3];
    if(fsymbol == 'T'){
      fsymbol = table[1][2];
    }
    for(int k=1;k<4;k++){
      if(table[k][3-k] == 'T'){
	continue;
      }
      symbol = table[k][3-k];
      if(symbol != fsymbol || symbol == '.'){
	okay = false;
      }
    }
    if(okay){
      if(symbol == 'X'){
	Xwon = true;
      }
      else if(symbol == 'O'){
	Owon = true;
      }
    }
  }
  
  //judge
  if(Xwon){
    result = "X won";
  }
  else if(Owon){
    result = "O won";
  }
  else if(complete){
    result = "Draw";
  }
  else{
    result = "Game has not completed";
  }
  
  return result;
}

void disptable(int size, char table[4][4]){
  for(int row=0;row<size;row++){
    for(int col=0;col<size;col++){
      cout << table[row][col];
    }
    cout << endl;
  } 
}

int main(){
  int repeat;
  const int tSize = 4;
  char table[tSize][tSize];

  cin >> repeat;
  for(int i=0;i<repeat;i++){
    for(int row=0; row < tSize;row++){
      for(int col=0; col < tSize;col++){
	cin >> table[row][col];
      }
    }

    /*   disptable(tSize,table);
     */

    cout << "Case #"<< i+1 << ": ";
    cout << judgeWinner(table) << endl;
    
  }  
}
