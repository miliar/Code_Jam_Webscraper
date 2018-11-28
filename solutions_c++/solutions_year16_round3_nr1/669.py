#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
using namespace std;

int T, N;

int main()
{
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    cout << "Case #" << i << ":";

    cin >> N;

    vector<int> P;
    int fst, snd, fsti, sndi;
    fst = snd = -1;
    fsti = sndi = -1;
    for (int j = 0; j < N; ++j) {
      int p; cin >> p;
      P.push_back(p);
      if (p > fst) {
        snd = fst; sndi = fsti;
        fst = p; fsti = j;
      } else if (p > snd) {
        snd = p; sndi = j;
      }
    }

    if (snd == -1) {
      while (P[fsti]) {
        int p = P[fsti];
        char c = (char)('A' + fsti);
        if (p == 1) {
          cout << " " << c;
          P[fsti] = P[fsti] - 1;
        } else {
          cout << " " << c << c;
          P[fsti] = P[fsti] - 2;
        }
      };
    } else {
      for (;;) {
        int sm = accumulate(P.begin(), P.end(), 0);
        if (!sm) break;

        int p = P[fsti], q = P[sndi];
        char pc = (char)('A' + fsti), qc = (char)('A' + sndi);
        if (p > q) {
          if (p - q == 1) {
            cout << " " << pc;
            P[fsti] = P[fsti] - 1;
          } else {
            cout << " " << pc << pc;
            P[fsti] = P[fsti] - 2;
          }
        } else if (sm > p + q) {
          cout << " ";
          int out = 0;
          for (int j = 0; j < N; ++j) {
            if (j == fsti || j == sndi) continue;
            int m = P[j];
            if (m > (2 - out)) m = 2 - out;
            for (int k = 0; k < m; ++k) {
              cout << (char)('A' + j);
              P[j] = P[j] - 1;
            }
            out += m;
            if (out == 2) break;
          }
        } else {
          cout << " " << pc << qc;
          P[fsti] = p - 1;
          P[sndi] = q - 1;
        }
      };
    }

    cout << endl;
  }

  return 0;
}
