#include <cstdio>

char c[4][4];
int T;
int tx,ty;
bool draw;
bool won(char h){
  if(tx!=-1)c[ty][tx] = h;
  bool bol;
  // riadky
  for(int i=0; i<4; i++){
    bol = 1;
    for(int j=0; j<4; j++) if(c[i][j] != h) bol = 0;
    if (bol) return 1;
  }
  //stlpce
  for(int i=0; i<4; i++){
    bol = 1;
    for(int j=0; j<4; j++) if(c[j][i] != h) bol = 0;
    if (bol) return 1;
  }
  //diagonaly
  bol = 1;
  for(int i=0; i<4; i++) if(c[i][i] != h) bol = 0;
  if(bol) return 1;
  bol = 1;
  for(int i=0; i<4; i++) if(c[i][3-i] != h) bol = 0;
  if(bol) return 1;
  return 0;
}

int main(){
  scanf("%d",&T);
  for(int t=0; t<T; t++){
    tx=-1;
    draw = 1;
    for(int i=0; i<4; i++) for(int j=0; j<4; j++){
      scanf(" %c ", &c[i][j]);
      if(c[i][j] == 'T') {tx = j; ty = i;}
      if(c[i][j] == '.') draw=0;
    }
    bool X = won('X');
    bool O = won('O');
    printf("Case #%d: ",t+1);
    if(X) printf("X won\n");
    else if(O) printf("O won\n");
    else if(draw) printf("Draw\n");
    else printf("Game has not completed\n");
  }
  return 0;
}