#include <algorithm>
#include <bitset>
#include <cassert>
#include <cinttypes>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <functional>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

const int kInf = numeric_limits<int>::max() / 32;

using Table = vector<vector<char>>;

class Kuhn {
 public:
  Kuhn(const vector<vector<int>>& g, int K) : g(g), K(K) { N = g.size(); }

  bool CheIsFull() {
    mt.assign(K, -1);
    for (int v = 0; v < N; ++v) {
      used.assign(N, false);
      Try(v);
    }

    int cnt = 0;
    for (int i = 0; i < K; ++i) {
      if (mt[i] != -1) {
        ++cnt;
      }
    }

    return cnt == N;
  }

 private:
  bool Try(int v) {
    if (used[v]) {
      return false;
    }

    used[v] = true;
    for (size_t i = 0; i < g[v].size(); ++i) {
      int to = g[v][i];
      if (mt[to] == -1 || Try(mt[to])) {
        mt[to] = v;
        return true;
      }
    }
    return false;
  }

  vector<vector<int>> g;
  int N, K;
  vector<int> mt;
  vector<char> used;
};

bool IsGood(const Table& gr) {
  int N = gr.size();

  for (int i = 0; i < N; ++i) {
    int cnt_machine = count(gr[i].begin(), gr[i].end(), true);
    if (cnt_machine == N) {
      continue;
    }

    vector<vector<int>> g;
    for (int j = 0; j < N; ++j) {
      if (!gr[i][j]) {
        continue;
      }

      g.resize(g.size() + 1);

      for (int k = 0; k < N; ++k) {
        if (i == k) {
          continue;
        }

        if (gr[k][j]) {
          g.back().push_back(k);
        }
      }
    }

    Kuhn kuhn(g, N);
    if (kuhn.CheIsFull()) {
      return false;
    }
  }

  return true;
}

int Go(Table& gr, map<Table, int>& memo) {
  auto it = memo.find(gr);
  if (it != memo.end()) {
    return it->second;
  }

  int N = gr.size();

  if (IsGood(gr)) {
    memo[gr] = 0;
    return 0;
  }

  int result = kInf;
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j) {
      if (gr[i][j]) {
        continue;
      }

      gr[i][j] = true;
      result = min(result, 1 + Go(gr, memo));
      gr[i][j] = false;
    }
  }

  assert(result != kInf);
  memo[gr] = result;
  return result;
}

void Solve() {
  int N;
  cin >> N;

  Table gr(N, vector<char>(N, false));
  for (int i = 0; i < N; ++i) {
    string S;
    cin >> S;
    for (int j = 0; j < N; ++j) {
      gr[i][j] = (S[j] == '1');
    }
  }

  map<Table, int> memo;
  cout << Go(gr, memo) << endl;
}

int main() {
//  freopen("../Console/1.txt", "rb", stdin);
  freopen("../Console/D-small-attempt0.in", "rb", stdin);
  freopen("../Console/D-small-attempt0.out", "wb", stdout);
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int T;
  cin >> T;
  for (int tc = 0; tc < T; ++tc) {
    cout << "Case #" << tc + 1 << ": ";
    Solve();
  }

  return 0;
}
