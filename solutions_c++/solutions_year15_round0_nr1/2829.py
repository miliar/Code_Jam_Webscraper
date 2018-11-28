#include <iostream>
#include <string>
using namespace std;

int caseMain() {
  int smax;
  string digits;
  cin >> smax >> digits; 

  int prev = 0;
  int res = 0;
  for (int i = 0; i <= smax; ++i) {
    if (prev < i) {
      int need = i - prev;
      res += need;
      prev += need;
    }
    prev += digits[i] - '0';
  }
  return res;
}

int main(int argc, const char* argv[]) {
  int T;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    cout << "Case #" << i + 1 << ": ";
    cout << caseMain() << endl;
  }
  return 0;
}
