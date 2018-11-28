#include <iostream>
#include <string>
#include <algorithm>
#include <map>

using namespace std;

void process_case() {
  string s;
  cin >> s;

  map<char, long> chars;
  for (int i = 'A'; i <= 'Z'; ++i) {
    char c = (char)i;
    chars[c] = count(s.begin(), s.end(), c);
  }

  map<int, long> digits;
  digits[8] = chars['G'];
  digits[6] = chars['X'];
  digits[7] = chars['S'] - digits[6];
  digits[5] = chars['V'] - digits[7];
  digits[4] = chars['U'];
  digits[3] = chars['H'] - digits[8];
  digits[2] = chars['W'];
  digits[0] = chars['Z'];
  digits[1] = chars['O'] - digits[0] - digits[2] - digits[4];
  digits[9] = chars['I'] - digits[8] - digits[6] - digits[5];

  for (int i = 0; i < 10; ++i) {
    long count = digits[i];
    for (int n = 0; n < count; ++n) {
      cout << i;
    }
  }
}

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    cout << "Case #" << (i + 1) << ": ";
    process_case();
    cout << endl;
  }
  return 0;
}