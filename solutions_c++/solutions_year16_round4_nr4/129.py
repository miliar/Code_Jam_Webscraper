#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

namespace {

int Solve(vector<string> workers) {
  const int N = workers.size();
  int w = 0;
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j) {
      w |= (workers[i][j] == '1') << (i * N + j);
    }
  }
  int res = N * N;
  for (int i = 0; i < (1 << (N * N)); ++i) {
    if (w & i) continue;
    int t = w | i;
    map<int, int> counts;
    for (int i = 0; i < N; ++i) {
      ++counts[(t >> (i * N)) & ((1 << N) - 1)];
    }
    int b = 0;
    for (const auto& p : counts) {
      if (b & p.first || p.second != __builtin_popcount(p.first)) {
        b = 0;
        break;
      }
      b |= p.first;
    }
    if (b == (1 << N) - 1) res = min(res, __builtin_popcount(i));
  }
  return res;
}

}

int main(void) {
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    int N;
    cin >> N;
    vector<string> workers(N);
    for (int j = 0; j < N; ++j) cin >> workers[j];
    cout << "Case #" << i << ": " << Solve(workers) << endl;
  }

  return 0;
}
