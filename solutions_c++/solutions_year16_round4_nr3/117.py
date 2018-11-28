#include <iostream>
#include <string>
#include <vector>

using namespace std;

namespace {

const string kImpossible = "IMPOSSIBLE";

class UnionFind {
 public:
  UnionFind(int n) : data_(n, -1) {}

  void unite(int a, int b) {
    a = find(a);
    b = find(b);
    if (a != b) {
      if (data_[a] > data_[b]) swap(a, b);
      data_[a] += data_[b];
      data_[b] = a;
    }
  }

  int find(int a) {
    if (data_[a] < 0) return a;
    return data_[a] = find(data_[a]);
  }

 private:
  vector<int> data_;
};

string Solve(int R, int C, vector<int> courtiers) {
  vector<int> indices(1);
  for (int i = 0; i < C; ++i) {
    indices.push_back(i);
  }
  for (int i = 0; i < R; ++i) {
    indices.push_back((R + 1) * C + C * R + i);
  }
  for (int i = 0; i < C; ++i) {
    indices.push_back((R + 1) * C - 1 - i);
  }
  for (int i = 0; i < R; ++i) {
    indices.push_back((R + 1) * C + R - 1 - i);
  }

  auto is_valid = [&](int hedges) {
    UnionFind uf((R + 1) * C + (C + 1) * R);
    for (int j = 0; j < R; ++j) {
      for (int k = 0; k < C; ++k) {
        int u = j * C + k;
        int d = u + C;
        int l = (R + 1) * C + k * R + j;
        int r = l + R;
        if ((hedges >> (j * C + k)) & 1) {
          uf.unite(u, r);
          uf.unite(d, l);
        } else {
          uf.unite(u, l);
          uf.unite(d, r);
        }
      }
    }
    for (int i = 0; i < R + C; ++i) {
      if (uf.find(indices[courtiers[i * 2]]) !=
          uf.find(indices[courtiers[i * 2 + 1]])) {
        return false;
      }
    }
    return true;
  };

  for (int i = 0; i < (1 << (R * C)); ++i) {
    if (!is_valid(i)) continue;
    string res;
    for (int j = 0; j < R; ++j) {
      for (int k = 0; k < C; ++k) {
        res += "/\\"[(i >> (j * C + k)) & 1];
      }
      if (j < R - 1) res += '\n';
    }
    return res;
  }
  return kImpossible;
}

}

int main(void) {
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    int R, C;
    cin >> R >> C;
    vector<int> courtiers(2 * (R + C));
    for (int j = 0; j < courtiers.size(); ++j) cin >> courtiers[j];
    cout << "Case #" << i << ":" << endl << Solve(R, C, courtiers) << endl;
  }

  return 0;
}
