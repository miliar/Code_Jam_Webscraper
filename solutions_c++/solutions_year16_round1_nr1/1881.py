#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string.h>
#include <iostream>

using namespace std;

void solve() {
  string s;
  cin >> s;
  int l = s.length();
  string o = "";
  o += s[0];
  for(int i = 1; i < l; i++) {
    if(s[i]>=o[0]) o = s[i] + o;
    else o = o + s[i];
  }
  cout << o << endl;
}

int main() {
  int t;
  cin >> t;
  for(int i = 1; i <= t; i++) {
      cout << "Case #" << i << ": ";
      solve();
  }
  return 0;
}
