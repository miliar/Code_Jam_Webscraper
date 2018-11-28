// Google Code Jam
// Qualification Round 2013
//
// Problem B. Lawnmower
//
// Compiled with C++11 and clang++
// clang++ -std=c++11 -stdlib=libc++ -Wall

#include <algorithm>
#include <cstring>
#include <iostream>

using std::cin;
using std::cout;
using std::endl;
using std::max;

int main(int argc, char* argv[]) {
  int t;
  cin >> t;
  for (auto testCase = 1; testCase <= t; ++testCase) {
    int n, m;
    cin >> n >> m;

    int lawn[n][m];
    for (auto i = 0; i < n; ++i) {
      for (auto j = 0; j < m; ++j) {
        cin >> lawn[i][j];
      }
    }

    cout << "Case #" << testCase << ": ";
    if (n == 1 || m == 1) {
      cout << "YES" << endl;
      continue;
    }

    int rows[n];
    int columns[m];
    memset(rows, 0, sizeof(rows));
    memset(columns, 0, sizeof(columns));

    bool possible = true;
    int grass;
    for (auto i = 0; possible && i < n; ++i) {
      for (auto j = 0; possible && j < m; ++j) {
        grass = lawn[i][j];
        rows[i] = max(rows[i], grass);
        columns[j] = max(columns[j], grass);

        bool horizontalOk = rows[i] <= grass;
        for (auto k = j + 1; horizontalOk && k < m; ++k) {
          horizontalOk = lawn[i][k] <= grass;
        }

        bool verticalOk = !horizontalOk && columns[j] <= grass;
        for (auto k = i + 1; verticalOk && k < n; ++k) {
          verticalOk = lawn[k][j] <= grass;
        }

        possible = horizontalOk || verticalOk;
      }
    }

    if (possible) {
      cout << "YES";
    } else {
      cout << "NO";
    }
    cout << endl;
  }
  return 0;
}
