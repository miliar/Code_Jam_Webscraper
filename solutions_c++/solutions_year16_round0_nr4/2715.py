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
    int K, C, S;
    cin >> K >> C >> S;

    // Small
    cout << "Case #" << t + 1 << ":";

    for (int i = 0; i != K; ++i) {
      cout << " " << i + 1;
    }

    cout << endl;

    // Large
    /*int SS = ceil(K * 1.0 / C);

    if (S < SS) {
      cout << "Case #" << t + 1 << ": IMPOSSIBLE" << endl;
      continue;
    }

    int MAX_ID = C * SS;

    int p[200] = { 0, };
    for (int i = 0; i != K; p[i] = i++);

    int padding = MAX_ID - C;
    for (int i = K; i != MAX_ID; p[i++] = padding);

    unsigned long long A[200] = { 0, };
    for (int i = 0; i != SS; ++i) {
      A[i] = p[i * C];
    }

    for (int i = 1; i != C; ++i) {
      for (int j = 0; j != SS; ++j) {
        A[j] = A[j] * K + p[i + j * SS];
      }
    }

    cout << "Case #" << t + 1 << ":";

    for (int i = 0; i != SS; ++i) {
      cout << " " << A[i] + 1;
    }

    cout << endl;*/
  }

  return 0;
}