#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool possible(int x, const vector<int>& S) {
  int Smax = S.size() - 1;
  int standing = x + S[0];

  for (int i = 1; i <= Smax; i++) {
    if (!S[i])
      continue;

    if (standing >= i)
      standing += S[i];
    else
      return false;
  }

  return true;
}

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int T;
  cin >> T;

  for (int kase = 1; kase <= T; kase++) {
    int Smax;
    cin >> Smax;
    cin.ignore(1);

    vector<int> S(Smax + 1);
    for (int i = 0; i <= Smax; i++) {
      char ch;
      cin >> ch;

      S[i] = ch - '0';
    }

    for (int i = 0; i <= Smax+1; i++) {
      if (possible(i, S)) {
        cout << "Case #" << kase << ": " << i << "\n";
        break;
      }
    }
  }

  return 0;
}
