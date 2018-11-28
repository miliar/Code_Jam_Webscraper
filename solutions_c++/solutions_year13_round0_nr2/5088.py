#include <iostream>
#include <string>

using namespace std;

int main() {
  int T, N, M;
  cin >> T;
  int max = 100;
  for(int t = 1; t <= T; t++) {
    cout << "Case #" << t << ": ";
    cin >> N >> M;
    int lawn[N][M];
    bool pos = true;
    int start[N][M];
    for(int n = 0; n < N; n++) {
      for(int m = 0; m < M; m++) {
        cin >> lawn[n][m];
        start[n][m] = max;
      }
    }
    if(N == 1 || M == 1) {
      pos = true;
    } else {
      for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
          if(pos && lawn[i][j] < start[i][j]) {
            int a = lawn[i][j];
            bool maybe = true;
            for(int n = 0; n< N; n++) {
              if(lawn[n][j] > a) {
                maybe = false; break;
              }
            }
            if(maybe) {
              for(int n = 0; n <N; n++) {
                start[n][j] = a;
              }
            } else {
              maybe = true;
              for(int m = 0; m < M; m++) {
                if(lawn[i][m] > a) {
                  maybe = false; break;
                }
              }
              if(maybe) {
                for(int m = 0; m <M; m++) {
                  start[i][m] = a;
                }
              } else {
                pos = false; break;
              }
            }
          }
        }
      }
    }
    if(pos) {
      cout << "YES" << endl;
    } else {
      cout << "NO" << endl;
    }
  }
}
