#include <cstdlib>
#include <string>
#include <iostream>
#include <set>

using namespace std;

int main() {
  // Number of cases.
  unsigned long N, K, C, S, T, I;

  cin >> N;

  // For each test case.
  for (int i=1; i<=N; i++)
  {
    cin >> K >> C >> S;

    T = (K + C - 1) / C;

    if (S < T) {
        cout << "Case #" << i << ": IMPOSSIBLE" << endl;
        continue;
    }

    cout << "Case #" << i << ":";

    // Generate test indexes
    if (C == 1) {
      for (int j=0; j<K; j++)
        cout << " " << j+1;
    } else {
      int j;
      for (j=1, I=0; j<K; j++) {

        if (j % C == 0) {
          cout << " " << I+1;
          I = 0;
        }

        I = (I * K) + j;
      }
      cout << " " << I+1;
    }

    cout << endl;
  }

  return 0;
}
