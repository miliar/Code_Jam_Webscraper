#include <iostream>
#include <vector>
#include <string>
using namespace std;


int main(int argc, char const *argv[]) {
  int t;
  cin >> t;
  for (size_t c = 1; c <= t; c++) {
    int n;
    cin >> n;
    vector<bool> seen(10, false);
    int tmp = n;
    while (tmp) {
      seen[tmp % 10] = true;
      tmp /= 10;
    }
    int mul = 2;
    while (n != 0) {
      int tmp = n * mul;
      while (tmp) {
        seen[tmp % 10] = true;
        tmp /= 10;
      }
      bool finished = true;
      for (int j = 0; j < 10; ++j) {
        finished &= seen[j];
      }
      if (finished) {
        break;
      }
      mul++;
    }
    cout << "Case #" << c << ": " << (n != 0 ? to_string(n * mul) : "INSOMNIA") << endl;
  }
  return 0;
}
