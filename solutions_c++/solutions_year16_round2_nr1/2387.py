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

void main() {
  int T;
  cin >> T;

  for (int t = 0; t != T; ++t) {
    string str;
    cin >> str;

    int len = str.length();

    int count[26] = { 0, };

    for (int i = 0; i != len; ++i) {
      ++count[str[i] - 'A'];
    }

    int retCount[10] = { 0, };

    // 0
    int num0 = count['Z' - 'A'];
    retCount[0] = num0;
    count['Z' - 'A'] -= num0;
    count['E' - 'A'] -= num0;
    count['R' - 'A'] -= num0;
    count['O' - 'A'] -= num0;

    // 2
    int num2 = count['W' - 'A'];
    retCount[2] = num2;
    count['T' - 'A'] -= num2;
    count['W' - 'A'] -= num2;
    count['O' - 'A'] -= num2;

    // 4
    int num4 = count['U' - 'A'];
    retCount[4] = num4;
    count['F' - 'A'] -= num4;
    count['O' - 'A'] -= num4;
    count['U' - 'A'] -= num4;
    count['R' - 'A'] -= num4;

    // 6
    int num6 = count['X' - 'A'];
    retCount[6] = num6;
    count['S' - 'A'] -= num6;
    count['I' - 'A'] -= num6;
    count['X' - 'A'] -= num6;

    // 8
    int num8 = count['G' - 'A'];
    retCount[8] = num8;
    count['E' - 'A'] -= num8;
    count['I' - 'A'] -= num8;
    count['G' - 'A'] -= num8;
    count['H' - 'A'] -= num8;
    count['T' - 'A'] -= num8;

    // 7
    int num7 = count['S' - 'A'];
    retCount[7] = num7;
    count['S' - 'A'] -= num7;
    count['E' - 'A'] -= num7;
    count['V' - 'A'] -= num7;
    count['E' - 'A'] -= num7;
    count['N' - 'A'] -= num7;

    // 5
    int num5 = count['F' - 'A'];
    retCount[5] = num5;
    count['F' - 'A'] -= num5;
    count['I' - 'A'] -= num5;
    count['V' - 'A'] -= num5;
    count['E' - 'A'] -= num5;

    // 1
    int num1 = count['O' - 'A'];
    retCount[1] = num1;
    count['O' - 'A'] -= num1;
    count['N' - 'A'] -= num1;
    count['E' - 'A'] -= num1;

    // 3
    int num3 = count['T' - 'A'];
    retCount[3] = num3;
    count['T' - 'A'] -= num3;
    count['H' - 'A'] -= num3;
    count['R' - 'A'] -= num3;
    count['E' - 'A'] -= num3 * 2;

    // 9
    retCount[9] = count['I' - 'A'];

    string ret = "";
    for (char i = 0; i != 10; ++i) {
      int cc = retCount[i];
      if (cc == 0) continue;
      for (int j = 0; j != cc; ++j) {
        ret.push_back(i + '0');
      }
    }
    
    cout << "Case #" << t + 1 << ": " << ret << endl;
  }
}