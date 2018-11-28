#include <iostream>
using namespace std;

string fun(string &input) {
  int letter[26] = {0};
  for (int i = 0; i < input.length(); ++i) {
    letter[input[i] - 'A']++;
  }
  int output[10] = {0};
  while (letter['Z' - 'A'] > 0) {
    output[0]++;
    letter['Z' - 'A']--;
    letter['E' - 'A']--;
    letter['R' - 'A']--;
    letter['O' - 'A']--;
  }
  while (letter['W' - 'A'] > 0) {
    output[2]++;
    letter['T' - 'A']--;
    letter['W' - 'A']--;
    letter['O' - 'A']--;
  }
  while (letter['U' - 'A'] > 0) {
    output[4]++;
    letter['F' - 'A']--;
    letter['O' - 'A']--;
    letter['U' - 'A']--;
    letter['R' - 'A']--;
  }
  while (letter['G' - 'A'] > 0) {
    output[8]++;
    letter['E' - 'A']--;
    letter['I' - 'A']--;
    letter['G' - 'A']--;
    letter['H' - 'A']--;
    letter['T' - 'A']--;
  }
  while (letter['O' - 'A'] > 0) {
    output[1]++;
    letter['O' - 'A']--;
    letter['N' - 'A']--;
    letter['E' - 'A']--;
  }
  while (letter['X' - 'A'] > 0) {
    output[6]++;
    letter['S' - 'A']--;
    letter['I' - 'A']--;
    letter['X' - 'A']--;
  }
  while (letter['H' - 'A'] > 0) {
    output[3]++;
    letter['T' - 'A']--;
    letter['H' - 'A']--;
    letter['R' - 'A']--;
    letter['E' - 'A']--;
    letter['E' - 'A']--;
  }
  while (letter['S' - 'A'] > 0) {
    output[7]++;
    letter['S' - 'A']--;
    letter['E' - 'A']--;
    letter['V' - 'A']--;
    letter['E' - 'A']--;
    letter['N' - 'A']--;
  }
  while (letter['V' - 'A'] > 0) {
    output[5]++;
    letter['F' - 'A']--;
    letter['I' - 'A']--;
    letter['V' - 'A']--;
    letter['E' - 'A']--;
  }
  while (letter['N' - 'A'] > 0) {
    output[9]++;
    letter['N' - 'A']--;
    letter['I' - 'A']--;
    letter['N' - 'A']--;
    letter['E' - 'A']--;
  }
  string s;
  for (int i = 0; i < 10; ++i) {
    if (output[i] > 0) {
      s.append(output[i], '0' + i);
    }
  }
  return s;
}

int main() {
  int T = 0;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    string s;
    cin >> s;
    cout << "Case #" << i << ": " << fun(s) << endl;
  }
}
