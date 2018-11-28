#include <iostream>
#include <cstdint>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <array>

using namespace std;

int main(int argc, char *argv[]) {
  ios_base::sync_with_stdio(false);
  unsigned long T;
  cin >> T;
  for (unsigned int i = 1; i <= T; ++i) {
    unsigned long S_max;
    cin >> S_max;
    string vec; cin >> vec;
    cout << "Case #" << i << ": ";
    unsigned long needed = 0;
    unsigned long have = 0;
    for (unsigned long x = 0; x < S_max + 1; ++x) {
      unsigned long S = vec[x] - '0';
      if (S == 0) continue;
      if (have < x) {
        needed += x - have;
        have += x-have;
      } 
      have += S;
    }
    cout << needed << '\n';
  }
}
