#include<iostream>
#include<map>
#include<vector>
using namespace std;

typedef long long int ll;

class Solver{
public:
  ll getAns( ll N ){
    if( N==0 ) return -1;
    vector<bool> appeared( 10, false );
    int cnt = 0;
    ll i;
    for( i=1; cnt<10 ; ++i ){
      setNum( N*i, appeared, cnt );
    }
    return N*(i-1);
  }
private:
  void setNum( ll N, vector<bool>& appeared, int& cnt ){
    while( N>0 ){
      ll t = N%10;
      if( !appeared[t] ){
	appeared[t] = true;
	++cnt;
      }
      N /= 10;
    }
  }
};
int main(){
  int n; cin >> n;
  for( int i=0; i<n; ++i ){
    ll t; cin >> t;
    cout << "Case #" << i+1 << ": ";
    Solver s;
    t = s.getAns( t );
    if( t==-1 )
      cout << "INSOMNIA";
    else
      cout << t;
    cout << endl;
  }
  return 0;
}
