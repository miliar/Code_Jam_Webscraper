#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";
    long long N;
    cin >> N;
    if (N == 0) {
      cout << "INSOMNIA" << endl;
    } else {
      vector<bool> d(10, false);
      long long x = 0;
      while (count(d.begin(), d.end(), false) > 0) {
        x += N;
        long long C = x;
        while (C > 0) {
          d[C % 10] = true;
          C = C / 10;
        }
      }
      cout << x << endl;
    }
  }
}
