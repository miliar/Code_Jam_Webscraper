#include <stdio.h>
#include <vector>
#include <string.h>
#include <iostream>

using namespace std;

string reduce(string s) {
  string o = "";
  int l = s.length();
  char last = s[0];
  o += last;
  for(int i = 1; i < l; i++) {
    if(s[i]!=last) {
      last = s[i];
      o += last;
    }
  }
  return o;
}

void solve() {
  string s;
  cin >> s;
  s = reduce(s);
  int l = s.length();
  if(s[l-1]=='-') printf("%d\n", l);
  else printf("%d\n", l-1);
}

int main() {
  int t;
  scanf("%d", &t);
  for(int i = 1; i <= t; i++) {
    printf("Case #%d: ", i);
    solve();
  }
  return 0;
}
