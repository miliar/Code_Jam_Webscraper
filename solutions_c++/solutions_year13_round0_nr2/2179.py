#include<iostream>
#include<cstring>

using namespace std;

#define MAXLENGTH 100

int main() {
  int T, N, M;
  float heights[MAXLENGTH][MAXLENGTH], rowmax[MAXLENGTH], columnmax[MAXLENGTH], curmax;
  bool impossible;
  
  cin >> T;
  cin.ignore(256, '\n');
  for (int trial = 1; trial <= T; ++trial) {
    impossible = false;
    cin >> N >> M;
    for (int row = 0; row < N; ++row) {
      for (int column = 0; column < M; ++column) {
        cin >> heights[row][column];
      }
      cin.ignore(256, '\n');
    }
    
    curmax = 0.0;
    for (int row = 0; row < N; ++row) {
      for (int column = 0; column < M; ++column) {
        if (heights[row][column] > curmax) curmax = heights[row][column];
      }
      rowmax[row] = curmax;
      curmax = 0.0;
    }
    
    curmax = 0.0;
    for (int column = 0; column < M; ++column) {
      for (int row = 0; row < N; ++row) {
        if (heights[row][column] > curmax) curmax = heights[row][column];
      }
      columnmax[column] = curmax;
      curmax = 0.0;
    }

    for (int row = 0; row < N; ++row) {
      for (int column = 0; column < M; ++column) {
        if (heights[row][column] < rowmax[row] && heights[row][column] < columnmax[column]) impossible = true;
      }
    }
    
    cout << "Case #" << trial << ": ";
    if (impossible) cout << "NO" << endl;
    else cout << "YES" << endl;
  }
}
