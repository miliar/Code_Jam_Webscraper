#include <iostream>
#include <cmath>
using namespace std;

bool fair(const string &s) {
  for (int i = 0; i < s.size()/2; i++)
    if (s[i] != s[s.size()-1-i])
      return false;
  return true;
}

bool fair(int x) {
  string s = "";
  while (x) {
    s += char('0' + x%10);
    x /= 10;
  }
  return fair(s);
}

bool fair_and_square(int x) {
  int rt = sqrt(x);
  if (rt * rt != x) return false;
  return fair(rt) && fair(x);
}

int main() {
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    int A, B; cin >> A >> B;
    int c = 0;
    for (int x = A; x <= B; x++)
      if (fair_and_square(x)) {
        c++;
      }
    cout << "Case #" << t << ": " << c << endl;
  }
  return 0;
}

