#include <algorithm>
#include <iostream>
#include <stack>
#include <vector>

using namespace std;

void solve() {
  int n, x;
  cin >> n >> x;
  vector < int > s(n);
  for(int& v: s) cin >> v;
  sort(s.begin(), s.end());
  stack < int > down;
  int ans = 0;
  int l = 0, r = n - 1;
  for(; l < r; ){
    if(s[l] + s[r] <= x){
      ++l;
      --r;
    }else{
      --r;
    }
    ++ans;
  }
  if(l == r) ++ans;
  cout << ans;
}

int main() {
  ios_base::sync_with_stdio(false);
  int t;
  cin >> t;
  for(int test = 1; test <= t; ++test){
    cout << "Case #" << test << ": ";
    solve();
    cout << '\n';
  }
}