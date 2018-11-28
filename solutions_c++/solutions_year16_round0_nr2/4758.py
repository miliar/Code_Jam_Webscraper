#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

void solve()
{
  string s;
  cin >> s;

  s.resize(unique(s.begin(), s.end()) - s.begin());

  int n = s.length();
  if (s[0] == '+') {
    cout << n - n%2 << endl;
  } else {
    cout << n - (n+1)%2 << endl;
  }
}

int main()
{
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    cout << "Case #" << i << ": ";
    solve();
  }
  return 0;
}
