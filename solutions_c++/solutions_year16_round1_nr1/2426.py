#include <iostream>
#include <string>

using namespace std;

string smart(int i, const string& s, const string& acc) {
  if(i == s.size()) return acc;
  if(i == 0) return smart(i + 1, s, string() + s[0]);
  if(s[i] >= acc[0]) return smart(i + 1, s, s[i] + acc);
  return smart(i + 1, s, acc + s[i]);
}

void solve() {
  string s;
  cin >> s;
  cout << smart(0, s, "") << endl;
}

int main() {
  int n;
  cin >> n;
  for(int i = 1; i <= n; ++i){
    cout << "Case #" << i << ": ";
    solve();
  }
}
