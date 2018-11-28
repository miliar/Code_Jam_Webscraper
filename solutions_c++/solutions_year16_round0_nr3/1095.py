#include <stdio.h>
#include <vector>
#include <string.h>
#include <iostream>

using namespace std;

void jamCoin(string s) {
  cout << s;
  for(int i = 3; i < 12; i++) {
    cout << " " << i;
  }
  cout << endl;
}

string toBinary(int n) {
  string s = "";
  if (n/2 != 0) s += toBinary(n/2);
  s += ((n%2)+'0');
  return s;
}

string expand(string s, int n) {
  while(s.length() < n) s = '0' + s;
  return s;
}

void solve() {
  int n; int m;
  cin >> n >> m;
  string s = "";
  for(int i = 0; i < n; i++) s += '0';
  s[0] = '1'; s[1] = '1';
  s[n-1] = '1'; s[n-2] = '1';
  for(int i = 0; i < m; i++) {
    string p = expand(toBinary(i), n/2-2);
    for(int j = 2; j < (n-2); j++) {
      s[j] = p[j/2-1];
    }
    jamCoin(s);
  }
}

int main() {
  int t;
  cin >> t;
  for(int i = 1; i <= t; i++) {
    cout << "Case #" << i << ":\n";
    solve();
  }
  return 0;
}
