#include <bits/stdc++.h>

using namespace std;

int matrix[15][15], n;

bool invalid() {
  for (int i = 0; i < n; ++i) {
    for (int j = 1; j < n; ++j) {
      if (matrix[i][j] <= matrix[i][j - 1]) return true;
    }
  }
  for (int j = 0; j < n; ++j) {
    for (int i = 1; i < n; ++i) {
      if (matrix[i][j] <= matrix[i - 1][j]) return true;
    }
  }
  return false;
}

int main() {
  int nt; scanf("%d", &nt);
  for (int caso = 1; caso <= nt; ++caso) {
    scanf("%d", &n);
    vector< vector<int> > vec;
    
    for (int i = 0; i < 2 * n - 1; ++i) {
      vector<int> v;
      for (int j = 0; j < n; ++j) {
        int x; scanf("%d", &x);
        v.push_back(x);
      }
      vec.push_back(v);
    }

    sort(vec.begin(), vec.end());

    for (int mask = 0, fim = 1 << (n * 2 - 1); mask < fim; ++mask) {
      if (__builtin_popcount(mask) != n) continue;

      vector< vector<int> > rows, cols;

      for (int j = 0; j < 2 * n - 1; ++j) {
        if (mask & (1 << j)) {
          rows.push_back(vec[j]);
        } else {
          cols.push_back(vec[j]);
        }
      }

      for (int i = 0; i < rows.size(); ++i) {
        for (int j = 0; j < n; ++j) {
          matrix[i][j] = rows[i][j];
        }
      }

      if (invalid()) continue;

      vector<int> answer;
      int num_tries = 0;

      for (int j = 0; j < n; ++j) {
        bool yes = false;
        for (int idx = 0; idx < cols.size(); ++idx) {
          yes = true;
          for (int i = 0; i < n; ++i) {
            if (matrix[i][j] != cols[idx][i]) {
              yes = false; break;
            }
          }
          if (yes) break;
        }
        if (!yes) {
          ++num_tries;
          for (int i = 0; i < n; ++i) {
            answer.push_back(matrix[i][j]);
          }
        }
      }
    
      if (num_tries == 1) {
        printf("Case #%d:", caso);
        for (int i = 0; i < n; ++i) printf(" %d", answer[i]);
        puts("");
        break;
      }
    }

  }
  return 0;
}
