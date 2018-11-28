#include <iostream>
#include <algorithm>

using namespace std;

typedef unsigned long long ll;

void solve()
{
  ll K, C, S;

  cin >> K >> C >> S;

  ll inc = 1;        // inc = K^(C-1)
  for (int i = 0; i < C-1; i++) {
    inc *= K;
  }

  ll pos = 1;
  for (int i = 0; i < S; i++) {
    cout << ' ' << pos;
    pos += inc;
  }
  cout << endl;
}

int main()
{
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    cout << "Case #" << i << ":";
    solve();
  }

  return 0;
}
