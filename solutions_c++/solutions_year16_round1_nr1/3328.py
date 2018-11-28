#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

typedef long long LL;

int T;
string S;

int main()
{
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    cin >> S;
    cout << "Case #" << i << ": ";

    string s;
    for (int j = 0; j < S.length(); ++j) {
      char c = S[j];
      if (!s.length() || c >= s[0])
        s = c + s;
      else
        s = s + c;
    }

    cout << s << endl;
  }

  return 0;
}
