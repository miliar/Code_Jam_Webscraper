#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

void solve() {
  string s;
  cin >> s;
  if(all_of(s.begin(), s.end(), [](char c){return c == '+';})){
    cout << 0 << endl;
    return;
  }
  while(s.back() == '+') s.pop_back();
  int ans = 1;
  for(size_t i = 0; i + 1 < s.size(); ++i)
    ans += s[i] != s[i + 1];
  cout << ans << endl;
}

int main() {
  int n;
  cin >> n;
  for(int i = 1; i <= n; ++i){
    cout << "Case #" << i << ": ";
    solve();
  }
}
