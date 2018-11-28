#include <iostream>
#include <string>
#include <cstdio>
#include <cmath>
#include <set>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; ++t) {
    int A, B, K;
    cin >> A >> B >> K;
    int win = 0;
    for (int a = 0; a < A; ++a) {
      for (int b = 0; b < B; ++b) {
        int num = a & b;
        if (num < K) ++win;
      }
    }
    cout << "Case #" << (t+1) << ": " << win << endl;
  }
  return 1;
}
