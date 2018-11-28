#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

// Every entry must be larger than all its row or col

void solve(int t) {
  int N, M;
  vector<vector<int> > lawn;
  cin >> N >> M;
  lawn.resize(N);
  for (int n = 0; n < N; ++n) {
    for (int m = 0; m < M; ++m) {
      int h;
      cin >> h;
      lawn[n].push_back(h);
    }
  }

  vector<int> mr(N);
  for (int n = 0; n < N; ++n) {
    mr[n] = *max_element(lawn[n].begin(), lawn[n].end());
  }

  vector<int> mc(M, -1);
  for (int m = 0; m < M; ++m) {
    for (int n = 0; n < N; ++n) {
      mc[m] = mc[m] < lawn[n][m] ? lawn[n][m] : mc[m];
    }
  }

  for (int m = 0; m < M; ++m) {
    for (int n = 0; n < N; ++n) {
      if (lawn[n][m] < mr[n] && lawn[n][m] < mc[m]) {
        cout << "Case #" << t << ": NO\n";
        return;
      }
    }
  }

  cout << "Case #" << t << ": YES\n";



}

int main(int argc, const char *argv[]) {
  int T;
  cin >> T;
  for (int t = 0; t < T; t++) {
    solve(t + 1);
  }
  return 0;
}
