#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 0x3f3f3f3f;

inline int getBit(const int mask, const int bit) {
  return (mask >> bit) & 1;
}

bool back(const vector<int> &G, vector<bool> &arrived, vector<bool> &used) {
  const int n = int(G.size());
  for (int i = 0; i < n; ++i) {
    if (!arrived[i]) {
      bool found = false;
      arrived[i] = true;
      for (int j = 0; j < n; ++j) {
        if (getBit(G[i], j) == 1 && !used[j]) {
          found = true;
          used[j] = true;
          if (!back(G, arrived, used))
            return false;
          used[j] = false;
        }
      }
      if (!found)
        return false;
      arrived[i] = false;
    }
  }
  return true;
}

int main() {
  ifstream in("input.txt");
  ofstream out("output.txt");
  int testCount;
  in >> testCount;
  for (int test = 1; test <= testCount; ++test) {
    int N;
    in >> N;
    vector<int> G = vector<int>(N, 0);
    for (int i = 0; i < N; ++i) {
      string row;
      in >> row;
      for (int j = 0; j < N; ++j)
        if (row[j] == '1')
          G[i] |= (1 << j);
    }
    int minCost = INF;
    for (int mask = 0; mask < (1 << (N * N)); ++mask) {
      vector<int> newG = vector<int>(N, 0);
      for (int i = 0; i < N; ++i)
        newG[i] = (mask >> (N * i)) & ((1 << N) - 1);
      int cost = 0;
      bool valid = true;
      for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
          if (getBit(newG[i], j) < getBit(G[i], j))
            valid = false;
          else if (getBit(newG[i], j) > getBit(G[i], j))
            ++cost;
        }
      }
      vector<bool> arrived = vector<bool>(N, false);
      vector<bool> used = vector<bool>(N, false);
      if (valid && back(newG, arrived, used))
        minCost = min(minCost, cost);
    }
    out << "Case #" << test << ": " << minCost << "\n";
  }
  in.close();
  out.close();
  return 0;
}
