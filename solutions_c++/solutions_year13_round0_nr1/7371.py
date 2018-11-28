#include<cstdio>
#include<iostream>
using namespace std;

bool checkCol(char b[4][4], char c){
  
  for(int y=0;y<4;++y){
    int count=0;
    for(int x=0;x<4;++x)
      if(b[x][y]==c || b[x][y]=='T')
          count++;
    if(count==4)
      return true;
  }
  return false;
}

bool checkRow(char b[4][4], char c){
  for(int x=0;x<4;++x){
    int count=0;
    for(int y=0;y<4;++y)
      if(b[x][y]==c || b[x][y]=='T')
          count++;
    if(count==4)
      return true;
  }
  return false;
}

bool checkDiag(char b[4][4], char c){
  int count =0;
  bool r=true;
  for(int i=0;i<4;++i)
    if(b[i][i]!=c && b[i][i]!='T')
     r = false;
  if(r){
    return r;
  }
  for(int i=0;i<4;++i)
    if(b[i][3-i]!=c && b[i][3-i]!='T')
     return false;
  return true;
}

bool checkFinish(char b[4][4]){
  for(int x=0;x<4;++x)
    for(int y=0;y<4;++y)
      if(b[x][y]=='.')
        return false;
  return true;
}
int main(){
  int N;
  scanf("%d",&N);
  for(int T=1;T<=N;++T){
    char b[4][4];
    for(int i=0;i<4;++i){
      for(int j=0;j<4;++j){
        scanf("%c",&b[i][j]);
        if(b[i][j]=='\n')
          j--;
      }
    }

    if(checkCol(b,'O') || checkRow(b,'O') || checkDiag(b,'O')){
      printf("Case #%d: O won\n",T);
      continue;
    }

    if(checkCol(b,'X') || checkRow(b,'X') || checkDiag(b,'X')){
      printf("Case #%d: X won\n",T);
      continue;
    }

    if(checkFinish(b)){
      printf("Case #%d: Draw\n",T);
    }else{
      printf("Case #%d: Game has not completed\n",T);
    }
  }

  return 0;
} 
