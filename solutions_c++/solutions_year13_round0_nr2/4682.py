#include <vector>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <map>
#include <string>
using namespace std;

void output(int i, string a) {
  cout << "Case #" << (i+1) << ": " << a << endl;
}


int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    int matrix[100][100] = {};
    int maxrow[100] = {};
    int maxcol[100] = {};
    int N,M;
    cin >> N;
    cin >> M;
    for (int j = 0; j < N; j++) {
      for (int k = 0; k < M; k++)  {
        cin >> matrix[j][k];
        maxrow[j] = (matrix[j][k] > maxrow[j] ? matrix[j][k] : maxrow[j]);
        maxcol[k] = (matrix[j][k] > maxcol[k] ? matrix[j][k] : maxcol[k]);
        // cout << "matrix " << j << " " << k << " = " << matrix[j][k] << " maxrow " << maxrow[j] << " maxcol " << maxcol[k] << endl;
      }
      // cout << endl;
    }
    // cout << endl;
    
    bool isOk = true;
    for (int j = 0; j < N; j++) {
      for (int k = 0; k < M; k++) {
        if (matrix[j][k] < maxrow[j] && matrix[j][k] < maxcol[k]) {
          isOk = false;
          // cout << "matrix " << j << " " << k << " = " << matrix[j][k] << " maxrow " << maxrow[j] << " maxcol " << maxcol[k] << endl << endl;
        }
      }
    }
    
    if (isOk) {
      output(i, "YES");
    } else {
      output(i, "NO");
    }
  }
}