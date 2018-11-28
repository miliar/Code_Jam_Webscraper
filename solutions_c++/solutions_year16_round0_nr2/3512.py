#include <algorithm>
#include <array>
#include <iostream>
#include <ios>
#include <istream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {
  cout.precision(8); cout.setf(ios_base::showpoint);
  long t; cin >> t;
  cin.get();

  for (long i = 1; i <= t; ++i) {
    string s;
    cin >> s;

    int sol = 0;
    char bad_side = '-';
    for (auto it = s.rbegin(); it != s.rend(); ++it) {
      if (*it == bad_side) {
        ++sol;
        bad_side = bad_side == '-' ? '+' : '-';
      }
    }

    cout << "Case #" << i << ": " << sol << endl;
  }

  return 0;
}
