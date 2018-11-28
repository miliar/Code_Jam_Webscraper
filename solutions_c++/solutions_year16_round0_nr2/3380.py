#include <string>
#include <fstream>
#include <iostream>
#include <istream>
#include <sstream>
#include <functional>
#include <numeric>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

int main() {
  int T;
  cin >> T;

  string ss;
  getline(cin, ss);

  for (int t = 0; t != T; ++t) {
    char s[102] = { 0, };
    cin >> s;

    int len = strlen(s);

    int count = 0;

    char lastC = s[0] == '+' ? '-' : '+';

    int idx = 1;
    while (idx != len) {
      if (lastC == s[idx]) {
        ++count;
        lastC = lastC == '+' ? '-' : '+';
      }
      ++idx;
    }

    if (s[len - 1] == '-') ++count;

    std::cout << "Case #" << t + 1 << ": " << count << endl;
  }

  return 0;
}