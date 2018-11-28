#include <iostream>

using namespace std;

int main(int argc, char** argv) {

  int T  = 0;
  cin >> T;
    for (int t = 0; t < T; t++) {
 
    int N = 0;
    cin >> N;    
    int M = 0;
    cin >> M;
    bool yes = true;

    int lawn[N * M];// = new lawn[N*M];

    int max_n[N];
    int max_m[M];

    for (int n = 0; n < N; n++) {
      max_n[n] = 0;
    }
    for (int m = 0; m < M; m++) {
      max_m[m] = 0;
    }

    for (int n = 0; n < N; n++) {
      for (int m = 0; m < M; m++) {
        int h = 0;
        cin >> h;
        if (h > max_n[n]) {
          max_n[n] = h;
        }
        if (h > max_m[m]) {
          max_m[m] = h;
        }
        lawn[n*M + m] = h;
      }
    }
/*    for (int n = 0; n < N; n++) {
      cout << "Max in horizontal line: " << max_n[n] << endl;
    }
    for (int m = 0; m < M; m++) {
      cout << "Max in vertical line: " << max_m[m] << endl;
    }
*/
    for (int n = 0; n < N; n++) {
      for (int m = 0; m < M; m++) {
        if (lawn[n*M + m] < max_n[n] && lawn[n*M + m] < max_m[m]) {
          yes = false;
          break;
        }
      }
    }

    cout << "Case #" << (t+1) << ": ";
    if (yes) {
      cout << "YES" << endl;
    } else {
      cout << "NO" << endl;
    }
  }
}
