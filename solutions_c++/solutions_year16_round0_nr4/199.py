#include <iostream>
#include <vector>
using namespace std;

typedef long long ll;
#define all(c)  (c).begin(),(c).end()
#define rep(var,n)  for(int var=0;var<(n);var++)

vector<ll> solve_l(int k, int c) {
  vector<ll> ans;
  for (int i=0; i<k; i+=c) {
    ll x = 0;
    for (int j=0; j<c; ++j) {
      if (i+j >= k) break;
      x = x*k + (i+j);  // k^c <= 1e18 < 2e63
    }
    ans.push_back(1+x);
  }
  return ans;
}

int main(){
  int _T; cin>>_T; // 1-100
  rep(_t,_T){
    cout << "Case #" << (1+_t) << ":";

    int K, C, S; cin >> K >> C >> S;

    vector<ll> s = solve_l(K,C);
    if (s.size() <= S) {
      for (int i=0; i<s.size(); ++i) {
        cout << " " << s[i];
      }
    } else {
      cout << " IMPOSSIBLE";
    }
    cout << endl;
  }
}
