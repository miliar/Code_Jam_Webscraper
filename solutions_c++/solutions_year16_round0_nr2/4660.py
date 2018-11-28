#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
using namespace std;

void flip(string& str, int pos) {
  char tmp;
  for (int i = 0; i <= pos/2; ++i) {
    tmp = str[i];
    str[i] = (str[pos - i] == '+' ? '-' : '+');
    str[pos - i] = (tmp == '+' ? '-' : '+');
  }
}

int solve(string& str) {
  int count = 0;
  for(int i = 0; i < str.size() - 1; ++i) {
    if(str[i]==str[i+1]) continue;

    flip(str, i);
    ++count;
  }
  if(str.back() == '-')
    ++count;
  return count;
}

int main() {
  freopen("B-large.in", "r", stdin);
  freopen("file.out", "w", stdout);
  int T;
  string s;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";
    cin >> s;
    cout << solve(s) << endl;
  }
  return 0;
}
