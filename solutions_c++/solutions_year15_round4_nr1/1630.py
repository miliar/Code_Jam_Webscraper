#include<bits/stdtr1c++.h>
using namespace std;

int T, N, M, R;
string P[105];
bool B[105][105][4], possible;

int main () {
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    memset(B, false, sizeof B);
    R = 0; possible = true;
    cin >> N >> M;
    for (int i = 0; i < N; ++i) cin >> P[i];
    for (int i = 0; i < N; ++i)
      for (int j = 1; j < M; ++j)
        B[i][j][0] = B[i][j - 1][0] || (P[i][j - 1] != '.');
    for (int i = N - 2; i >= 0; --i)
      for (int j = 0; j < M; ++j)
        B[i][j][1] = B[i + 1][j][1] || (P[i + 1][j] != '.');
    for (int i = 0; i < N; ++i)
      for (int j = M - 2; j >= 0; --j)
        B[i][j][2] = B[i][j + 1][2] || (P[i][j + 1] != '.');
    for (int i = 1; i < N; ++i)
      for (int j = 0; j < M; ++j)
        B[i][j][3] = B[i - 1][j][3] || (P[i - 1][j] != '.');
    for (int i = 0; i < N; ++i)
      for (int j = 0; j < M; ++j)
        if (P[i][j] != '.') {
          switch (P[i][j]) {
          case '<': R += !B[i][j][0]; break;
          case 'v': R += !B[i][j][1]; break;
          case '>': R += !B[i][j][2]; break;
          case '^': R += !B[i][j][3]; break;
          }
          possible = possible && (B[i][j][0] || B[i][j][1] || B[i][j][2] || B[i][j][3]);
        }
    cout << "Case #" << t << ": " << ((possible)? to_string(R) : "IMPOSSIBLE") << endl;
  }
  return 0;
}
