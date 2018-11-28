#include<bits/stdc++.h>
using namespace std;

int N,K;
double P[222];


double check(int st){
  int num = __builtin_popcount( st );
  double res = 0.0;
  for(int i=0;i<(1<<num);i++){
    if( __builtin_popcount( i ) == num/2 ){
      double r = 1.0;
      for(int j=0,k=0;j<N;j++){
        if( st & (1<<j) ){
          if(i &(1<<k) ) r *= P[j];
          else r *= (1.0 - P[j]);
          k++;
        }
      }
      res += r;
    }
  }
  return res;
}

double solve(){
  if( K&1 ) return 0.0;
  double res = 0.0;
  for(int i=0;i<(1<<N);i++){
    if( __builtin_popcount( i ) == K ) {
      res = max( res, check( i ) );      
    }
  }
  return res;
}

int main(){
  int T;
  cin >> T;
  for(int ttt=1;ttt<=T;ttt++){   
    cout << "Case #"<< ttt << ": ";
    cin >> N >> K;
    for(int i=0;i<N;i++) {
      cin >> P[i];
    }
    //cout << solve(0) << endl;
    //cout << solve(1) << endl;
    double res = solve();
    printf("%.9lf\n",res );
    
  }
}

