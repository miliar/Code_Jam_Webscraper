#include <stdio.h>
#include <stdlib.h>
int n,m;
char tab[100][100];
int tmp[100][100];
int pre_check[1000000];
int come[100];
int ch[100];
int ans = 100000;
int occ[100];
int always;
int choose(int k){
  if( k == n ) return 0;
  int chk = 0;
  for(int i = 0 ; i < n ; i++ ){
    if( tmp[come[k]][i] == 1 && occ[i] == 0 ){
      chk = 1;
      occ[i] = 1;
      choose(k+1);
      occ[i] = 0;
    }
  }
  if( ! chk ) always = 0;
}
int rec2(int k){
  if( k == n ){
    for(int i= 0 ; i< n ;i++ ) occ[i] = 0;
    choose(0);
    return 0;
  }
  for(int i = 0 ; i < n ; i++ ){
    if( ch[i] == 0 ){
      ch[i] = 1;
      come[k] = i;
      rec2(k+1);
      ch[i] = 0;
    }
  }
}
int check(){
  for(int i = 0 ; i < n ; i++ ) ch[i] = 0;
  always = 1;
  rec2(0);
  return always;
}
int encode(){
  int result =0;
  for(int i = 0 ; i < n ; i++ ){
    for(int j = 0 ;j <n ; j++ ){
      result *=2;
      result+=tmp[i][j];
    }
  }
  return result;
}
int gg = 0;
int rec(int x,int y,int pre){
  if( x == n && y == 0 ){
    int count = 0;
    if( ! pre ){
      for(int i = 0 ;i <n ; i++ ){
        for(int j = 0 ; j < m; j++ ){
          if( tab[i][j] == 1 && tmp[i][j] == 0 ) return 0;
          if( tab[i][j] == 0 && tmp[i][j] == 1 ) count++;
        }
      }
    }
    if( n < 4 ) if( check() && count < ans ) ans = count;
    if( n == 4 ){
      if( pre ){
        pre_check[encode()] = check();
        gg ++;
      }else{
        if( pre_check[encode()] && count < ans ) ans = count;
      }
    }

    return 0;
  }

  tmp[x][y] = 0;
  if( y == m-1 ){ rec(x+1,0,pre);}
  else rec(x,y+1,pre);
  tmp[x][y] = 1;
  if( y == m-1 ) rec(x+1,0,pre);
  else rec(x,y+1,pre);
}

int main(){
  int t;
  scanf("%d",&t);
  n = 4;
  m = 4;
  rec(0,0,1);
  for(int e = 0 ; e < t ; e++ ){
    scanf("%d",&n);
    m =n;
    ans = 1000000;
    for(int i = 0 ; i < n ; i++ ){
      scanf("%s",tab[i]);
      for(int j = 0 ; j < n ;j++ ) tab[i][j] -='0';
    }
    rec(0,0,0);
    printf("Case #%d: %d\n",e+1,ans);
  }
}

    

