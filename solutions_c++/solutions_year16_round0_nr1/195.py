#include <iostream>
#include <vector>
using namespace std;
typedef long long ll;
#define rep(var,n)  for(int var=0;var<(n);var++)

ll solve(int N) {
  int f = 0;
  ll iN=0, i=0;
  for (i=1,iN=N; i<1e9; ++i,iN+=N) {
    for (ll x=iN; x>0; x/=10) {
      f |= (1 << (x%10));
      if (f == 0x3ff) return iN;
    }
  }
  return -1;
}

int main(){
  int _T; cin>>_T; // 1-100
  rep(_t,_T){
    cout << "Case #" << (1+_t) << ": ";
    int N; cin >>N; // 0-1e6
    ll ans = solve(N);
    if (ans >= 0) {
      cout << ans << endl;
    } else {
      cout << "INSOMNIA" << endl;
    }
  }
  return 0;
}
