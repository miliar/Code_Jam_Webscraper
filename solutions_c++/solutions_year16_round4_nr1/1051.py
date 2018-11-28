#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int T, N, R, P, S;

bool ans(const string &s)
{
  return count(s.begin(), s.end(), 'R') == R
    && count(s.begin(), s.end(), 'P') == P
    && count(s.begin(), s.end(), 'S') == S;
}

void each_case()
{
  string a, b, c;
  a = "P"; b = "R"; c = "S";
  for (int i = 0; i < N; ++i) {
    string aa, bb, cc;
    aa = a + b; bb = a + c; cc = b + c;
    a = aa; b = bb; c = cc;
  }

  if (ans(a)) cout << " " << a;
  else if (ans(b)) cout << " " << b;
  else if (ans(c)) cout << " " << c;
  else cout << " IMPOSSIBLE";
}

int main()
{
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    cout << "Case #" << i << ":";

    cin >> N >> R >> P >> S;
    each_case();

    cout << endl;
  }

  return 0;
}
