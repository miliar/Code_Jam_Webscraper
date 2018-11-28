#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; t++) {
    int N, M;
    cin >> N >> M;
    vector<int> grid(N * M);
    for (int n = 0; n < N; n++) {
      for (int m = 0; m < M; m++) {
        int value;
        cin >> value;
        grid[n * M + m] = value;
      }
    }
    bool cutable = true;
    // check if each value is cutable
    // (i.e. max of its row OR col)
    for (int n = 0; n < N; n++) {
      for (int m = 0; m < M; m++) {
        int cur = grid[n * M + m];
        bool maxcol = true;
        bool maxrow = true;
        for (int n0 = 0; n0 < N; n0++) {
          if (cur < grid[n0 * M + m])
            maxcol = false;
        }
        for (int m0 = 0; m0 < M; m0++) {
          if (cur < grid[n * M + m0])
            maxrow = false;
        }
        if (maxcol == false && maxrow == false)
          cutable = false;
      }
    }
    cout << "Case #" << t + 1 << ": ";
    if (cutable)
      cout << "YES";
    else
      cout << "NO";
    cout << endl;
  }
  return 0;
}
