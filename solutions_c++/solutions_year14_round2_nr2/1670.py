#include<bits/stdc++.h>

#define REP(i,s,n) for(int i=s;i<n;i++)
#define rep(i,n) REP(i,0,n)

using namespace std;

typedef long long ll;
const int IINF = INT_MAX;
const ll LLINF = LLONG_MAX;

int main(){
  /*
  int cnt= 0;
  rep(i,7){
    rep(j,8){
      if( ( i & j ) < 5 )cnt++;
    }
  }
  cout << cnt << endl;
  */

  int T,CNT = 1;
  cin >> T;
  while( T-- ){
    int A,B,K;
    cin >> A >> B >> K;
    int cnt= 0;
    rep(i,A)rep(j,B)if((i&j)<K)cnt++;
    cout << "Case #" << CNT++ << ": " << cnt<<endl;
  }

  return 0;
}
