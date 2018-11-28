#include <bits/stdc++.h>
using namespace std;

const int R = 4;
int row[2];
int G[2][R][R];

int main() {
  int Tc;
  cin >> Tc;
  for(int tc = 0; tc < Tc; ++tc) {
    for(int k = 0; k < 2; ++k) {
      cin >> row[k];
      --row[k];
      for(int i = 0; i < R; ++i) {
	for(int j = 0; j < R; ++j) {
	  cin >> G[k][i][j];
	}
      }
    }
    int ans = -1;
    for(int i = 0; i < R; ++i) {
      for(int j = 0; j < R; ++j) {
	if(G[0][row[0]][i] == G[1][row[1]][j]) {
	  if(ans != -1) {
	    ans = -2;
	  } else {
	    ans = G[0][row[0]][i];
	  }
	}
      }
    }
    cout << "Case #" << tc+1 << ": ";
    if(ans == -1)
      cout << "Volunteer cheated!" << endl;
    else if(ans == -2)
      cout << "Bad magician!" << endl;
    else
      cout << ans << endl;
  }
  return 0;
}
