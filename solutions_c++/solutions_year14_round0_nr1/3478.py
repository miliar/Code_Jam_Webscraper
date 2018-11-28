#include <iostream>
#include <cstdio>
using namespace std;
int main() {
  ios::sync_with_stdio(0);
  freopen("inA.txt", "r", stdin);
  freopen("outA.txt", "w", stdout);
  int T;
  cin >> T;
  int row[2];
  int ans[17];
  int mat[17][17];
  for (int cases = 1; cases <= T; ++cases) {
    cin >> row[0];
    for (int i=0; i<17; ++i) ans[i]=0;
    for (int i=0; i<4; ++i)
    for (int j=0; j<4; ++j)
      cin >> mat[i][j];
    
    for (int i=0; i<4; ++i) {
      ans[mat[row[0]-1][i]]++;
    }
    cin >> row[1];
    
    for (int i=0; i<4; ++i)
    for (int j=0; j<4; ++j)
      cin >> mat[i][j];
        
    for (int i=0; i<4; ++i) {
      ans[mat[row[1]-1][i]]++;
    }
    cout << "Case #" << cases << ": ";
    int sol = -1;
    int res = 0;
    for (int i=1; i<=16; ++i) {
      if (ans[i]==2) {
        ++sol;
        res = i;
      }
    }
    if (sol == -1) {
      cout << "Volunteer cheated!\n";
    } else if (sol > 0) {
      cout << "Bad magician!\n";
    } else {
      cout << res << "\n";
    }
      
  }
  return 0;
}