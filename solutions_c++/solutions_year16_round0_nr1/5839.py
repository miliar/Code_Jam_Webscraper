#include <iostream>
#include <set>
#include <string>

using namespace std;

void solve() {
  int n;
  cin >> n;
  if(n == 0){
    cout << "INSOMNIA" << endl;
    return;
  }
  string tmp = to_string(n);
  set < char > digits(tmp.begin(), tmp.end());
  int step = 1;
  while(digits.size() != 10){
    ++step;
    tmp = to_string(n * step);
    digits.insert(tmp.begin(), tmp.end());
  }
  cout << n * step << endl;
}

int main() {
  int n;
  cin >> n;
  for(int i = 1; i <= n; ++i){
    cout << "Case #" << i << ": ";
    solve();
  }
}
