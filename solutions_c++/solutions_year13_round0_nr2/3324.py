#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>
#include<limits>
#include<map>
#include<string>

using namespace std;

int main() {
  int T;
  cin >> T;
  
  for (int i = 0; i < T; i++) {
    int N, M;
    cin >> N >> M;
    int l[N][M];
    for (int j = 0; j < N; j++) {
      for (int k = 0; k < M; k++) {
        cin >> l[j][k];
      }
    }
    bool e, x, ex = true;
    for (int j = 0; j < N; j++) {
      for (int k = 0; k < M; k++) {
        e = false; 
        x = true;
        for (int a = 0; a < M; a++) {
          if (l[j][k] < l[j][a])
            x = false;
        }
        if (x) e = true;
        
        if (!e) {
          x = true;
          for (int a = 0; a < N; a++) {
            if (l[j][k] < l[a][k])
              x = false;
          }
          if (x) e = true;
        }
        
        if (!e) {
          ex = false;
          break;
        }
      }
      if (!ex) break;
    }
    if (ex)
      cout << "Case #" << i + 1 << ": YES" << endl;
    else
      cout << "Case #" << i + 1 << ": NO" << endl;
  }
  return 0;
}

