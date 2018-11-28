#include<iostream>

using namespace std;

char table[4][4];
bool comp;


bool init(){
  comp = true;
}

void input(){
  for(int i = 0; i < 4; i++)
    for(int j = 0; j < 4; j++){
      cin >> table[i][j];
      if(table[i][j] == '.') comp = false;
    }
}

bool get(char c){
  
  int Tnum,Cnum;

  for(int i = 0; i < 4; i++){
    Tnum = Cnum = 0;
    for(int j = 0; j < 4; j++){
      if(table[i][j] == c) Cnum++;
      if(table[i][j] == 'T') Tnum++;
    }
    if(Tnum==1&&Cnum==3||Cnum==4) return true;
  }

  for(int i = 0; i < 4; i++){
    Tnum = Cnum = 0;
    for(int j = 0; j < 4; j++){
      if(table[j][i] == c) Cnum++;
      if(table[j][i] == 'T') Tnum++;
    }
    if(Tnum==1&&Cnum==3||Cnum==4) return true;
  }

  Tnum = Cnum = 0;
  for(int i = 0; i < 4; i++){
    if(table[i][i] == c) Cnum++;
    if(table[i][i] == 'T') Tnum++;
  }
  if(Tnum==1&&Cnum==3||Cnum==4) return true;
  
  Tnum = Cnum = 0;
  for(int i = 0; i < 4; i++){
    if(table[i][3-i] == c) Cnum++;
    if(table[i][3-i] == 'T') Tnum++;
  }
  if(Tnum==1&&Cnum==3||Cnum==4) return true;
  return false;
}

void solve(int rev){
  bool A = get('X');
  bool B = get('O');

  cout << "Case #" << rev+1 << ": ";
  if(A) cout << "X won" << endl;
  else if(B) cout << "O won" << endl;
  else if(comp) cout << "Draw" << endl;
  else cout << "Game has not completed" << endl;

}

int main(){

  int T;
  cin >> T;

  for(int i = 0; i < T; i++){
    init();
    input();
    solve(i);
  }
  return 0;
}
