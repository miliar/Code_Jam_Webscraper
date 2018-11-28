#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int check(int x, int p) {
  int 
}

string bin(int x) {
  string s;
  for (; x > 0; x >>= 1) {
    s += '0' + (x & 1);
  }
  reverse(s.begin(), s.end());
  return s;
}

vector<int> a;
bool solve(int x) {
  a.clear();
  for (int p = 2; p <= 10; ++p) {
    int d = check(i, p);
    if (d == -1) return false;
    a.push_back(d);
  }
  cout << "1" << bin(x) << "1";
  for (int i : a) {
    cout << " " << i;
  }
  cout << endl;
  return true;
}

int main() {
  int T; cin >> T;
  for (int tt = 1; tt <= T; ++t) {
    int N, J; cin >> N >> J;
    cout << "Case #" << tt << ":\n";
    for (int i = 0; i < (1<<(N-2)); ++i) {
      bool res = solve(i);
      if (res) --J;
      if (J == 0) break;
    }
  }
  return 0;
}
