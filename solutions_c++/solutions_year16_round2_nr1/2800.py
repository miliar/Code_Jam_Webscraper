#include <iostream>
#include <string>
#include <algorithm>
#include <set>
#include <functional>
#include <map>

using namespace std;

string remove_digit(string digit, string line) {
  for (int i = 0; i < digit.length(); ++i) {
    for (int j = 0; j <= line.length(); ++j) {
      if (line[j] == digit[i]) {
        line.erase(j, 1);
        break;
      }
    }
  }
  return line;
}

int main()
{
  map<char, int> code;
  code['Z'] = 0;
  code['X'] = 6;
  code['W'] = 2;
  code['S'] = 7;
  code['V'] = 5;
  code['G'] = 8;
  code['F'] = 4;
  code['O'] = 1;
  code['T'] = 3;
  code['N'] = 9;
  string digits[] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
  char codes[] = { 'Z', 'X', 'W', 'S', 'V', 'G', 'F', 'O', 'T', 'N' };

  int T;
  std::cin >> T;

  for (int t = 0; t < T; ++t)
  {
    string line;
    std::cin >> line;
    int d[10] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
    
    for (int i = 0; i < 10; ++i) {
      while (line.find(codes[i]) != string::npos) {
        line = remove_digit(digits[code[codes[i]]], line);
        d[code[codes[i]]]++;
      }
    }
    string res = "";
    for (int i = 0; i < 10; ++i) {
      for (int j = 0; j < d[i]; ++j) {
        res += to_string(i);
      }
    }
    cout << "Case #" << t + 1 << ": " << res;
    cout << endl;
  }
  return 0;
}