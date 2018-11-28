#include <bits/stdc++.h>

using namespace std;

string s;

void read() {
  cin >> s;
}

char opp(char c) {
  if (c == '+')
    return '-';
  else
    return '+';
}

void kill() {
  int ans = 0;
  int i = s.length() - 1;

  char aim = '+';

  while (i >= 0) {
    if (s[i] != aim) {
      ++ans;
      aim = opp(aim);
    }
    --i;
  }

  cout << ans << endl;
}



int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cout << "Case #" << i << ": ";
    read();
    kill();
    cerr << "Case #" << i << " done.\n";
  }
  return 0;
}
