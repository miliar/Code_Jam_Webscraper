#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll C, D, V;

vector<ll> DENOM;
vector<bool> can;

void dump()
{
  for(size_t i = 0; i < can.size(); ++i){
    cout << i << ":" << boolalpha << can[i] << " ";
  }
  cout << "\n";
}

void enable(ll d)
{
  for(ll i = V+1; i; ){
    --i;
    for(ll t = 0; t < C; ++t){
      ll diff = d * (t + 1);
      if(can[i] && i + diff <= V){
        can[i + diff] = true;
      }
    }
  }
}

ll solve()
{
  can = vector<bool>(V+1);
  can[0] = true;
  for(auto d : DENOM){
    enable(d);
    //dump();
  }
  ll ans = 0;
  for(auto it = find(can.begin(), can.end(), false), last = can.end();
      it != last; it = find(can.begin(), can.end(), false)){
    ++ans;
    ll d = it - can.begin();
    enable(d);
  }
  return ans;
}

int main(){
  size_t T;
  std::cin >> T;
  for(size_t i = 1; i <= T; ++i){
    std::cin >> C >> D >> V;
    DENOM.clear();
    for(ll j = 0; j < D; ++j){
      ll d;
      cin >> d;
      DENOM.push_back(d);
    }
    std::cout << "Case #" << i << ": " << solve() << "\n";
  }
}
