#include <bits/stdc++.h>

using namespace std;

int resolve (char *s) {
  int i, sum = 0;
  if (s[0] == '-')
    sum = 1;
  for (i = 0; s[i] && s[i] == '-'; i++);
  while (s[i]) {
    if (s[i] == '-') {
      sum += 2;
      while (s[i] && s[i] == '-')
        i++;
    }
    else
      i++;
  }
  return sum;
}

int main () {
  ios_base::sync_with_stdio(false);
  int t, i, n, caso;
  char s[101];
  
  cin >> t;
  
  for (caso = 1; caso <= t; caso++) {
    cin >> s;
    cout << "Case #" << caso << ": " << resolve (s) << endl;
  }
  
  return 0;
}










