#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <numeric>
#include <cstdlib>
#include <utility>

using namespace std;

int A[110][110];

bool R[110];
bool C[110];

int main() {
  int T; cin >> T;
  for(int t = 1; t <= T; t++) {
    int N, M; cin >> N >> M;
    for(int i = 0; i < N; i++) {
      for(int j = 0; j < M; j++) {
        cin >> A[i][j];
      }
    }

    bool res = true;
    for(int h = 1; res && h <= 100; h++) {
      for(int i = 0; i < N; i++) {
        R[i] = true;
        for(int j = 0; j < M && R[i]; j++) {
          R[i] = A[i][j] <= h;
        }
      }
      for(int j = 0; j < M; j++) {
        C[j] = true;
        for(int i = 0; i < N && C[j]; i++) {
          C[j] = A[i][j] <= h;
        }
      }
      for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
          res &= A[i][j] != h || R[i] || C[j];
        }
      }
    }
    cout << "Case #" << t << ": " << (res ? "YES" : "NO") << endl;
  }
  return 0;
}
