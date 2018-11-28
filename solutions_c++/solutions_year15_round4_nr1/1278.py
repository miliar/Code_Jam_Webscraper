#include<cstdio>
#include<algorithm>
#include<vector>
#include<map>
#include<iostream>
using namespace std;

#define For(Q,W) for(int Q=0; Q<W; Q++)

int dx[] = {0,0,-1,1};
int dy[] = {-1,1,0,0};

void solve(int T){
  printf("Case #%d: ",T+1);
  int r,c;
  scanf("%d %d ",&r,&c);
  char pole[r+2][c+2];
  For(i,r+2)For(j,c+2) pole[i][j]='#';
  For(i,r)
  For(j,c){
      char pom;
      scanf(" %c ",&pom);
      pole[i+1][j+1]=pom;
  }
  
  int ans = 0;
  bool imposible = false;
  For(i,r)
  For(j,c){
      if(pole[i+1][j+1]=='.') continue;
      int d;
      if(pole[i+1][j+1]=='^') d=0;
      if(pole[i+1][j+1]=='v') d=1;
      if(pole[i+1][j+1]=='<') d=2;
      if(pole[i+1][j+1]=='>') d=3;
      
      bool fine=false;
      int somx = j+1+dx[d], somy =i+1+dy[d];
      
      while(pole[somy][somx]!='#'){
        if(pole[somy][somx]!='.'){
            fine =true;
            break;
        }
        somx+=dx[d];
        somy+=dy[d];
      }
      
      if (fine) continue;
      ans+=1;
      bool can=false;
      
      For(dd,4){
          somx = j+1+dx[dd], somy =i+1+dy[dd];
      
          while(pole[somy][somx]!='#'){
            if(pole[somy][somx]!='.'){
                can =true;
                break;
            }
            somx+=dx[dd];
            somy+=dy[dd];
          }
      }
      if(!can) imposible=true;
      
  }
  
  if(imposible){
      printf("IMPOSSIBLE\n");
  }
  else{
      printf("%d\n",ans);
  }
}

int main(){
  int T;
  scanf("%d ",&T);
  For(i,T) solve(i);
  return 0;
}

