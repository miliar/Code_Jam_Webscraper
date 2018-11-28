#include <iostream>
#include <string>
#include <cmath>
#include <vector>
using namespace std;
int main() {
  int tk, tk1 = 0;
  cin >> tk;
  while (tk--) {
    tk1++;
    long long k, c, s;
    cin >> k >> c >> s;
    cout << "Case #" << tk1 << ": ";
    for (long long i = 0; i < s; i++) {
      if (i) {
        cout << " ";
      }
      long long res = 1;
      for (int j = 0; j < c - 1; j++) {
        res *= k;
      }
      cout << i * res + 1;
    }
    cout << endl;
  }
  return 0;
}
