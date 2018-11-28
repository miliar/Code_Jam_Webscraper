#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <utility>

using namespace std;

int main(int argc, char *argv[]) {
  int n;
  int N, M;
  int *lawn;

  if (argc != 2) return -1;
  freopen(argv[1], "r", stdin);

  cin >> n;

  for (int c = 1; c <= n; ++c) {
    bool possible = true;
    vector<pair<int, int> > cell_to_check;

    cout << "Case #" << c << ": ";

    cin >> N;
    cin >> M;

    lawn = (int *)malloc(N * M * sizeof(int));

    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < M; ++j) {
        cin >> lawn[i*M + j];
      }
    }

    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < M; ++j) {
        // Check row
        for (int k = 0; k < M; ++k) {
          if (lawn[i*M + k] > lawn[i*M + j]) {
            pair<int, int> p(i, j);
            cell_to_check.push_back(p);
          }
        }
        // Check column
        for (auto cell = cell_to_check.begin(); cell != cell_to_check.end(); ++cell) {
          auto ce = *cell;
          for (int i = 0; i < N; ++i) {
            if (lawn[i * M + ce.second] > lawn[ce.first * M + ce.second])
              possible = false;
          }
        }
      }
    }

    if (possible)
      cout << "YES";
    else
      cout << "NO";
    cout << endl;
  }

  return 0;
}
