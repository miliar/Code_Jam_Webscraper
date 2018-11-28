#include<iostream>
#include<assert.h>
using namespace std;
int R,C;
char g[101][101];
int movex[4] = {0,0,-1,1};
int movey[4] = {-1,1,0,0};
bool check1( int y, int x ){
  for( int i = 0; i < R ;i++){
    if( i == y )continue;
    if( g[i][x] != '.' )return 0;
  }
  for( int i = 0; i < C ; i++){
    if( i == x )continue;
    if( g[y][i] != '.' )return 0;
  }
  return 1;
}
int check2( int y, int x , char c){
  int i = -1;
  if(c == '^' )i=0;
  if(c == 'v' )i=1;
  if(c == '<' )i=2;
  if(c == '>' )i=3;
  assert( i != -1 );
  y+=movey[i];
  x+=movex[i];
  //  cout<<"("<<x<<","<<y<<")"<<endl;
  while(y>-1&&x>-1&& y < R && x < C ){
    if(g[y][x] !='.' ){
      //      cout<<"y="<<y<<endl;
      //      cout<<"x="<<x<<endl;
      return 0;
    }
    y+=movey[i];
    x+=movex[i];
  }
  return 1;
}

int solv(){
  int res =0;
  for( int i = 0; i < R;i++){
    for(int j=0;j<C;j++){
      if(g[i][j]=='.')continue;
      if(check1(i,j))return -1;
      res += check2(i,j,g[i][j]);
      //      cout<<"check2("<<i<<","<<j<<","<<g[i][j]<<") = "<<check2(i,j,g[i][j])<<endl;
    }
  }
  return res;
}



int main(void){
  int T;
  cin>>T;
  for( int testcase = 1; testcase <= T; testcase++){
    cin>>R>>C;
    for(int i=0;i<R;i++){
      for(int j=0;j<C;j++){
        cin>>g[i][j];
      }
    }
    int ans = solv();
    if(ans == -1){
      cout<<"Case #"<<testcase<<": IMPOSSIBLE"<<endl;
    }else{
      cout<<"Case #"<<testcase<<": "<<ans<<endl;
    }
  }
  return 0;
}
