#include <cassert>
#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

class Solver {
 public:
  void Solve() {
    int begin = 0;
    for (int i = 0; i < N; ++i) {
      std::sort(soldiers.begin() + begin, soldiers.end(),
                [i](const vector<int>& a, const vector<int>& b) {
                  return a[i] < b[i];
                });
      while (begin < soldiers.size() - 1 &&
             soldiers[begin][i] == soldiers[begin + 1][i]) {
        begin++;
      }
      begin++;
    }

    int m = Missing();
    vector<int> ans;
    for (int i = 0; i < m; ++i) {
      ans.push_back(
          soldiers[2 * i][m] + soldiers[2 * i + 1][m] - soldiers[2 * m][i]);
    }
    ans.push_back(soldiers[2 * m][m]);
    for (int i = m + 1; i < N; ++i) {
      int idx = 2 * i - 1;
      ans.push_back(
          soldiers[idx][m] + soldiers[idx + 1][m] - soldiers[2 * m][i]);
    }
    for (int i = 0; i < N; ++i) {
      cout << " " << ans[i];
    }
    cout << endl;
  }

  int Missing() {
    for (int i = 0; i < N - 1; ++i) {
      if (soldiers[2 * i][i] != soldiers[2 * i + 1][i]) return i;
    }
    return N - 1;
  }

  int N;
  vector<vector<int>> soldiers;
};

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; ++t) {
    Solver solver;
    cout << "Case #" << t + 1 << ":";
    cin >> solver.N;
    int N = solver.N;
    solver.soldiers.resize(2 * N - 1);
    for (int i = 0; i < 2 * N - 1; ++i) {
      for (int j = 0; j < N; ++j) {
        int k;
        cin >> k;
        solver.soldiers[i].push_back(k);
      }
    }
    solver.Solve();
  }
}
