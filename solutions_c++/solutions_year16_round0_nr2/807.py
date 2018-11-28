#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string flip(string &s, int depth)
{
  string t = s;
  for (int i = 0; i < depth; ++i)
    t[i] = (s[depth - i - 1] == '+' ? '-' : '+');
  return t;
}

int main()
{
  int T;

  cin >> T;
  for (int i = 1; i <= T; ++i) {
    string s;
    cin >> s;

    int nflip = (int)(s[s.length() - 1] == '-');
    for (int j = 1; j < s.length(); ++j)
      if (s[j - 1] != s[j])
        ++nflip;

    cout << "Case #" << i << ": " << nflip << endl;
  }

  return 0;
}
