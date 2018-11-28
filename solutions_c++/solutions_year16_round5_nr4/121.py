#include <iostream>
#include <set>
#include <string>

using namespace std;

void solve() {
  int n, l;
  cin >> n >> l;
  set < string > good;
  for(int i = 0; i < n; ++i){
    string s;
    cin >> s;
    good.insert(s);
  }
  string bad;
  cin >> bad;
  if(good.find(bad) != good.end()){
    cout << "IMPOSSIBLE\n";
    return;
  }
  cout << "10?";
  for(int i = 0; i < 50; ++i)
    cout << "10";
  cout << ' ';
  if(l > 1)
    cout << string(l - 1, '?');
  else
    cout << 0;
  cout << endl;
}

int main() {
  int tests;
  cin >> tests;
  for(int test = 1; test <= tests; ++test){
    cout << "Case #" << test << ": ";
    solve();
  }
}
