#include <iostream>
#include <set>
#include <vector>
#include <cmath>

using namespace std;

int main()
{
  int cases;
  cin >> cases;

  for (auto curCase = 1; curCase <= cases; curCase++) {

    int64_t K, C, S;
    cin >> K >> C >> S;

    cout << "Case #" << curCase << ":";
    if (K == 1) {
      cout << " " << 1;
    }
    else {
      if (C == 1) {
        if (K == S) {
          for (auto pos = 1; pos <= K; ++pos) {
            cout << " " << pos;
          }
        }
        else {
          cout << " IMPOSSIBLE";
        }
      }
      else {
        if (S >= K - 1) {
          for (auto pos = 2; pos <= K; ++pos) {
            cout << " " << pos;
          }
        }
        else if ((S == K - 2) && (K >= 4)) {
          for (auto pos = 2; pos < K - 1; ++pos) {
            cout << " " << pos;
          }

          int64_t KC = K;
          for (int64_t c = 2; c <= C; ++c) {
            KC = KC * KC;
          }
          cout << " " << (KC - 1);
        }
        else {
          cout << " IMPOSSIBLE";
        }
      }
    }
    cout << endl;
  }
}
