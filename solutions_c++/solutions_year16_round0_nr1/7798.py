#include <iostream>

using namespace std;

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  
  long n;
  cin >> n;
  for (long i = 0; i < n; ++i) {
    long in;
    cin >> in;
    if (in == 0) // I figured the insomnia would only happen when starting with 0...
      cout << "Case #" << i+1 << ": INSOMNIA\n";
    else {
      bool seen[10] = {false};
      long v = 0;
      for (;;) {
        v += in;
        long d = v;
        for (; d >= 10; d /= 10) {
          seen[d%10] = true;
        }
        seen[d%10] = true; // Add the remaining digit (for breaks before the last one)
        bool all = true;
        for (int i = 0; i < 10; ++i) {
          if (!seen[i]) all = false;
        }
        if (all) {
          cout << "Case #" << i+1 << ": " << v << "\n";
          break;
        }
      }
    }
  }
  
}
