#include <iostream>
using namespace std;

typedef long long ll;

bool f(ll x,ll n,ll p){
  ll k = x; // People above me...
  ll bM = 0;
  for(int i=n-1;i>=0 && k > 0;i--){
    k = (k-1)/2;
    bM ^= (1ll << i);
  }

  return bM < p;
}

bool g(ll x,ll n,ll p){
  ll k = (1ll << n) - x - 1; // People below me...
  ll bM = (1ll << n) - 1;
  for(int i=n-1;i>=0 && k > 0;i--){
    k = (k-1)/2;
    bM ^= (1ll << i);
  }
  
  return bM < p;
}

void do_case(){
  ll n,p;
  cin >> n >> p;

  // always lose
  ll lo = 0, hi = (1ll << n)-1;
  while(hi - lo > 1){
    ll mid = (lo+hi)/2;
    if(f(mid,n,p)) lo = mid;
    else hi = mid;
  }
  ll ans1 = (f(hi,n,p) ? hi : lo);

  lo = 0, hi = (1ll << n)-1;
  while(hi - lo > 1){
    ll mid = (lo+hi)/2;
    if(g(mid,n,p)) lo = mid;
    else hi = mid;
  }
  
  ll ans2 = (g(hi,n,p) ? hi : lo);
  cout << ans1 << " " << ans2;
}

int main(){
  int T,C=1;
  cin >> T;
  while(T--){
    cout << "Case #" << C++ << ": "; do_case(); cout << endl;
  }
  return 0;
}
