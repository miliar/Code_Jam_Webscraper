#include <stdlib.h>
#include <iostream>

using namespace std;

int solve(string s)
{
  int ans = 0;
  for (int i = 1; i < s.size(); i++) {
    ans += (s[i] != s[i - 1]);
  }
  ans += (s[s.size() - 1] == '-');
  return ans;
}

int main()
{
  int T;
  cin >> T;

  for (int t = 1; t <= T; t++) {
    string s;
    cin >> s;
    //cout << s << "\n";
    cout << "Case #" << t << ": " << solve(s) << "\n";
  }
}

