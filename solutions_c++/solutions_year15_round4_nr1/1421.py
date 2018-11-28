#include <iostream>
#include <vector>
#include <string>

using namespace std;

int NOTHING = 0;
int UP = 1; int  DOWN = 2; int LEFT = 3; int RIGHT = 4;

int R,C;
vector<vector<int> > grid;


int readInput() {
  cin >> R >> C;
  grid.clear();
  grid.resize(R);
  for (int r = 0; r < R; ++r) {
    string temp;
    grid[r].resize(C);
    cin >> temp;
    for (int c = 0; c < C; ++c) {
      if (temp[c] == '.') {grid[r][c] = NOTHING;}
      if (temp[c] == '^') {grid[r][c] = UP;}
      if (temp[c] == '>') {grid[r][c] = RIGHT;}
      if (temp[c] == '<') {grid[r][c] = LEFT;}
    if (temp[c] == 'v') {grid[r][c] = DOWN;}
    }
  }
}

bool isAlone(int r,int c) {
  for (int x = 0; x < R; ++x) {
    if (x == r) continue;
    if (grid[x][c] != NOTHING) return false;
  }
  for (int y = 0; y < C; ++y) {
    if (y == c) continue;
    if (grid[r][y] != NOTHING) return false;
  }
  return true;
}

int solve() {
  int res = 0;
  for (int r = 0; r < R; ++r){
    for(int c = 0; c < C; ++c) {
      if (grid[r][c] == NOTHING) continue;
      if (isAlone(r,c)) return -1;
 
      if (grid[r][c] == UP) {
	if (r == 0) {
	  res ++;
	  continue;
	}
	int toAdd = 1;
	for (int x = r-1; x >= 0;  --x) {
	  if (grid[x][c] != NOTHING) {toAdd = 0; break;}
	}
	res = res+toAdd;
      }

      if (grid[r][c] == DOWN) {
	if (r == R-1) {
	  res ++;
	  continue;
	}
	int toAdd = 1;
	for (int x = r+1; x < R;  ++x) {
	  if (grid[x][c] != NOTHING) {toAdd = 0; break;}
	}
	res = res+toAdd;
      }
      if (grid[r][c] == RIGHT) {
	if (c == C-1) {
	  res ++;
	  continue;
	}
	int toAdd = 1;
	for (int y = c+1; y < C;  ++y) {
	  if (grid[r][y] != NOTHING) {toAdd = 0; break;}
	}
	res = res+toAdd;
      }
      if (grid[r][c] == LEFT) {
	if (c == 0) {
	  res ++;
	  continue;
	}
	int toAdd = 1;
	for (int y = c-1; y >= 0;  --y) {
	  if (grid[r][y] != NOTHING) {toAdd = 0; break;}
	}
	res = res+toAdd;
      }
    }
  }
  return res;
}


int main() {
int T;
cin >> T;
for (int cas = 0; cas < T; ++cas) {
  readInput();
  int res = solve();
  if (res == -1) {
    cout << "Case #" << cas +1 << ": IMPOSSIBLE" << endl;
  } else {
    cout << "Case #" << cas +1 << ": " << res << endl;
  }
}
}
