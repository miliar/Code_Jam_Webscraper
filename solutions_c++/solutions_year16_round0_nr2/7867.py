#include <iostream>
using namespace std;

int count(string& ps) {
  int out = 0;
  for(int i = 1; i < ps.size(); ++i) {
    out += (ps[i] != ps[i-1]);
  }
  return out;
}

int main() {
  int T, i;
  string ps;
  cin >> T;
  for(i = 1; i <= T; ++i) {
    cin >> ps;
    ps.push_back('+');
    cout << "Case #" << i << ": " << count(ps) << endl;
  }
  return 0;
}
