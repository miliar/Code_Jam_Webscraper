#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main ()
{
  int T;
  cin >> T;
  for(int t = 0; t < T; t++) {
    int row1, row2;
    vector<vector<int>> G1(4, vector<int>(4, 0));
    vector<vector<int>> G2(4, vector<int>(4, 0));
    cin >> row1;
    for(int i = 0; i < 4; i++)
      for(int j = 0; j < 4; j++)
        cin >> G1[i][j];
    cin >> row2;
    for(int i = 0; i < 4; i++)
      for(int j = 0; j < 4; j++)
        cin >> G2[i][j];
    int ans = -1;
    int numAns = 0;
    for(int i = 0; i < 4; i++) {
      for(int j = 0; j < 4; j++) {
        if (G1[row1-1][i] == G2[row2-1][j]) {
          ans = G1[row1-1][i];
          numAns++;
        }
      }
    }
    cout << "Case #" << t+1 << ": ";
    if (numAns == 0)
      cout << "Volunteer cheated!" << endl;
    else if (numAns == 1)
      cout << ans << endl;
    else
      cout << "Bad magician!" << endl;
  }
}
