#include <iostream>

using namespace std;

int main(int argc, char** argv) {
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    int N;
    cin >> N;
    int M;
    cin >> M;
    int a[N][M];
    for (int j = 0; j < N; ++j) {
      for (int k = 0; k < M; ++k) {
        cin >> a[j][k];
      }
    }
    bool not_possible = false;
    for (int j = 0; j < N; ++j) {
      for (int k = 0; k < M; ++k) {
        int h = a[j][k];
        bool is_high = false;
        bool is_high2 = false;
        // row
        for (int l = 0; l < M; ++l) {
          if (a[j][l] > h) {
            is_high = true;
            break;
          }
        }
        // column
        for (int l = 0; l < N; ++l) {
          if (a[l][k] > h) {
            is_high2 = true;
            break;
          }
        }
        if (is_high && is_high2) {
          not_possible = true;
        }
      }
    }
    if (not_possible) {
      cout << "Case #" << i << ": NO" << endl;
    } else {
      cout << "Case #" << i << ": YES" << endl;
    }
  }
  return 0;
}

