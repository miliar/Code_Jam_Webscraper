#include <iostream>
#include <string>

using namespace std;

void solve() {
  string s;
  cin >> s;
  const int n = s.size();
  string res;
  int ans = 0;
  for(int i = 0; i < n; ++i){
    if(!res.empty() && res.back() == s[i]){
      ans += 10;
      res.pop_back();
    }else{
      res.push_back(s[i]);
    }
  }
  cout << ans + res.size() / 2 * 5 << endl;
}

int main() {
  int tests;
  cin >> tests;
  for(int test = 1; test <= tests; ++test){
    cout << "Case #" << test << ": ";
    solve();
  }
}
