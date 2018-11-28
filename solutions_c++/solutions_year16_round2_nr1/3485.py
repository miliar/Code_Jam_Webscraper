#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <unordered_map>
#include <queue>

#define max(a, b) ((a) > (b) ? (a) : (b))
#define min(a, b) ((a) < (b) ? (a) : (b))
#define MAX_N 401

using namespace std;

int chs[26];

int res[10];

int main() {
  int T;
  cin >> T;
  for (int cnt = 1; cnt <= T; ++cnt) {
    string s;
    cin >> s;
    for (int i = 0; i < 26; ++i) {
      chs[i] = 0;
    }
    int len = s.length();
    for (int i = 0; i < len; ++i) {
      chs[s[i] - 'A']++;
    }

    res[0] = chs['Z' - 'A'];
    chs['E' - 'A'] -= res[0];
    chs['R' - 'A'] -= res[0];
    chs['O' - 'A'] -= res[0];

    res[2] = chs['W' - 'A'];
    chs['T' - 'A'] -= res[2];
    chs['O' - 'A'] -= res[2];

    res[4] = chs['U' - 'A'];
    chs['F' - 'A'] -= res[4];
    chs['O' - 'A'] -= res[4];
    chs['R' - 'A'] -= res[4];

    res[5] = chs['F' - 'A'];
    chs['I' - 'A'] -= res[5];
    chs['V' - 'A'] -= res[5];
    chs['E' - 'A'] -= res[5];

    res[6] = chs['X' - 'A'];
    chs['S' - 'A'] -= res[6];
    chs['I' - 'A'] -= res[6];

    res[7] = chs['V' - 'A'];
    chs['S' - 'A'] -= res[7];
    chs['E' - 'A'] -= 2 * res[7];
    chs['N' - 'A'] -= res[7];

    res[8] = chs['G' - 'A'];
    chs['E' - 'A'] -= res[8];
    chs['I' - 'A'] -= res[8];
    chs['H' - 'A'] -= res[8];
    chs['T' - 'A'] -= res[8];

    res[9] = chs['I' - 'A'];
    chs['N' - 'A'] -= 2 * res[9];
    chs['E' - 'A'] -= res[9];

    res[3] = chs['R' - 'A'];
    chs['T' - 'A'] -= res[3];
    chs['H' - 'A'] -= res[3];
    chs['E' - 'A'] -= 2 * res[3];

    res[1] = chs['N' - 'A'];

    printf("Case #%d: ", cnt);
    for (int i = 0; i < 10; ++i) {
      for (int j = 0; j < res[i]; ++j) {
        cout << i;
      }
    }
    cout << endl;
  }
  return 0;
}
