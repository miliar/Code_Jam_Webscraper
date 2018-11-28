#include <string>
#include <fstream>
#include <iostream>
#include <istream>
#include <sstream>
#include <functional>
#include <numeric>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

int main() {
  int T;
  cin >> T;

  for (int t = 0; t != T; ++t) {
    int K;
    char S[2000] = {};
    cin >> S >> K;

    int p = 0;
    int c = 0;
    int l = strlen(S);

    while (p <= l - K)
    {
      if (S[p] != '+') {
        for (int i = p; i < p + K; ++i) {
          if (S[i] == '+')
            S[i] = '-';
          else
            S[i] = '+';
        }
        ++c;
      }
      ++p;
    }
    bool nana = false;
    for (int i = l - 1; i >= l - K; --i) {
      if (S[i] == '-') {
        nana = true;
        break;
      }
    }


    cout << "Case #" << t + 1 << ": ";

    // Result
    if (nana) {
      cout << "IMPOSSIBLE";
    }
    else {
      cout << c;
    }

    cout << endl;
  }

  return 0;
}