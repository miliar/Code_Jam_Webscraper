#include <iostream>
#define N 4
#define NOCARD -1
#define MORETHANONE -2
using namespace std;

int main() {
  int nTestCases;
  cin >> nTestCases;
  for (int c = 1; c <= nTestCases; ++c) {
    int row1,row2, dist1[N+1][N+1], dist2[N+1][N+1];
    bool candidate[N*N+1];
    int selectedCard = NOCARD;
    for (int i = 1; i <= N*N; ++i) candidate[i] = false;
    cin >> row1;
    for (int i = 1; i <= N; ++i)
      for (int j = 1; j <= N; ++j)
        cin >> dist1[i][j];
    cin >> row2;
    for (int i = 1; i <= N; ++i)
      for (int j = 1; j <= N; ++j)
        cin >> dist2[i][j];
    for (int j = 1; j <= N; ++j)
      candidate[dist1[row1][j]] = true;
    for (int j = 1; j <= N; ++j) {
      if (candidate[dist2[row2][j]]) {
        if (selectedCard == NOCARD) selectedCard = dist2[row2][j];
        else {
          selectedCard = MORETHANONE;
          break;
        }
      }
    }
    cout << "Case #" << c << ": ";
    if (selectedCard == NOCARD) cout << "Volunteer cheated!" << endl;
    else if (selectedCard == MORETHANONE) cout << "Bad magician!" << endl;
    else cout << selectedCard << endl;
  }
}
