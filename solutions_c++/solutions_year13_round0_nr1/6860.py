#include <iostream>
#include <algorithm>
using namespace std;

const int H = 4;
const int W = H;

char G[H][W];

inline bool isIn(int i, int j) {
  return 0 <= i && i < H && 0 <= j && j < W;
}

bool win(char player) {
  for(int i = 0; i < H; ++i) {
    for(int j = 0; j < W; ++j) {
      for(int di = -1; di <= 1; ++di) {
	for(int dj = -1; dj <= 1; ++dj) {
	  if(di == 0 && dj == 0) continue;
	  for(int k = 0; k < 4; ++k) {
	    int ni = i + di * k;
	    int nj = j + dj * k;
	    if(!isIn(ni, nj)) break;
	    if(G[ni][nj] == 'T' || G[ni][nj] == player);
	    else break;
	    if(k+1 == 4) return true;
	  }
	}
      }
    }
  }
  return false;
}

int main() {
  int T;
  cin >> T;
  for(int tc = 0; tc < T; ++tc) {
    bool existSpace = false;
    for(int i = 0; i < H; ++i) {
      for(int j = 0; j < W; ++j) {
	cin >> G[i][j];
	if(G[i][j] == '.') existSpace = true;
      }
    }
    int winner;
    if(win('X')) winner = 'X';
    else if(win('O')) winner = 'O';
    else if(existSpace) winner = -1;
    else winner = 0;

    cout << "Case #" << tc+1 << ": ";
    if(winner == -1) cout << "Game has not completed" << endl;
    else if(winner == 0) cout << "Draw" << endl;
    else cout << (char)winner << " won" << endl;
  }
  return 0;
}
