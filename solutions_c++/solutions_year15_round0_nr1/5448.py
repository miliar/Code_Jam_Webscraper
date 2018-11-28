#include <iostream>
#include <vector>
#include <string>

using namespace std;

int Smax;

string S;

void solve() {
  int res = 0;
  int nbUp = 0;
  for (int s = 0; s <= S.length(); ++s) {
    if (s > nbUp) res += s - nbUp, nbUp += s - nbUp;

    nbUp += (S[s] - '0');
  }

  cout << res << endl;
}

int main() {
  int T;

  cin >> T;

  for (int t = 0; t < T; ++t) {
    cin >> Smax;

    cin >> S;

    cout << "Case #" << (t+1) << ": ";

    solve();
  }

  return 0;
}
