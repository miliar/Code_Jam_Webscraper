#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

int T;
bool used[11];
ll N;

void setn(ll k){
  if( k == 0 ) used[0] = true;
  while( k > 0 ){
    used[k%10] = true;
    k/=10;
  }
}

bool check(){
  for(int i=0;i<10;i++) if( !used[i] ) return true;
  return false;
}

int main(){
  cin >>T;
  for(int ttt=1;ttt<=T;ttt++){
    cin >> N;
    cout << "Case #" << ttt << ": ";
    if( N == 0 ) cout << "INSOMNIA" << endl;
    else {
      memset(used,0,sizeof(used));
      setn( N );
      ll i=2;
      while( check() ){
        ll p = N*(i++);
        setn( p );
      }
      cout << N*(i-1) << endl;
    }
  }
}
