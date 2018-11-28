#include <iostream>
#include <math.h>
#include <climits>

using namespace std;

int main(int argc, char** argv) {
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    long long r;
    cin >> r;
    long long t;
    cin >> t;
    long long p = 1;
    for (; p <= 1000000000; ++p) {
      if ((2 * p * p + (2 * r - 1) * p) > t) {
        break;
      }
    }
    cout << "Case #" << i << ": " << (p - 1) << endl;
  }
}
