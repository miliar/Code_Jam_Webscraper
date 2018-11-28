#include <stdio.h>
int n,m;
double p[1000];
int tmp[1000];
double ap[1000];
int an;
double dp[100][100];
double ans = 0;
double find(){
  for(int i = 0; i <= an ;i++ )
    for(int j = 0; j <= an ; j++ ) dp[i][j] = 0;

  dp[1][0] = (1-ap[0]);
  dp[1][1] = ap[0];

  for(int x = 2 ; x <= an ; x++ ){
    for(int y = 0 ; y <= x ; y++ ){
      dp[x][y] = dp[x-1][y] * (1-ap[x-1]);
      if( y > 0 ) dp[x][y] += dp[x-1][y-1] * ap[x-1];
    }
  }
  return dp[an][an/2];
}
  
int rec(int k){
  if( k == n ){
    int ct = 0;
    for(int i = 0 ; i < n ; i++ ){
      ct+=tmp[i];
    }
    if( ct !=m ) return 0;
    an = 0;
    for(int i = 0 ; i < n ; i++ ){
      if( tmp[i] == 1 ) ap[an++] = p[i];
    }
    double cur = find();
    if( cur > ans ) ans = cur;
    // if( ans == 1 ){
    //   for(int i = 0 ; i < n ; i++ ){ printf("%d ",tmp[i]); }
    //   printf("\n");
    // }
    return 0;
  }
  tmp[k] = 0;
  rec(k+1);
  tmp[k] = 1;
  rec(k+1);
}
int main(){
  int t;
  scanf("%d",&t);
  for(int e = 0 ; e < t ; e++ ){
    scanf("%d %d",&n,&m);
    ans = 0;
    for(int i = 0 ; i < n ;i++ ){
      scanf("%lf",&p[i]);
    }
    rec(0);
    printf("Case #%d: %lf\n",e+1,ans);
  }
}
    
    


