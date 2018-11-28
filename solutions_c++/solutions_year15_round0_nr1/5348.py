#include <iostream>

using namespace std;

int main() {
  int t;
  cin >> t;
  for (int j = 1; j <= t; ++j) {
    int n;
    cin >> n;
    int s = 0, r = 0;
    for (int i = 0; i <= n; ++i) {
      char c;
      cin >> c;
      int x = c - '0';
      if (x > 0) {
        if (i > s) {
          r += i - s;
          s = i;
        }
        s += x;
      }
    }
    cout << "Case #" << j << ": " << r << endl;
  }
}