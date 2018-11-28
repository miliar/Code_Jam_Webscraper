#include <cstdio>
#include <fstream>
#include <iostream>

using namespace std;

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  int T;
  cin >> T;

  for(int t = 1; t <= T; t++) {
    int r[2];
    int mat[4][4][2];
    for(int m = 0; m < 2; m++) {
      cin >> r[m];
      for(int i = 0; i < 4; i++)
        for(int j = 0; j < 4; j++) {
          cin >> mat[i][j][m];
        }
    }

    int cnt = 0, val = -1;
    for(int i = 0; i < 4; i++) {
      for(int j = 0; j < 4; j++) {
        if(mat[r[0]-1][i][0] == mat[r[1]-1][j][1]) {
          val = mat[r[0]-1][i][0];
          cnt++;
        }
      }
    }

    cout << "Case #" << t << ": ";
    if(cnt == 0)
      cout << "Volunteer cheated!" << endl;
    else if(cnt > 1)
      cout << "Bad magician!" << endl;
    else
      cout << val << endl;
  }

  return 0;
}
