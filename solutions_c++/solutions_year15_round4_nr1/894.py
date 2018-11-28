#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

int t, R, C;
vector <string> grid;

string ch = "^v<>";

bool route(int i, int j, int k){
  if (k == 0) {
    for (int ii = 0; ii < i; ii++){
      if (grid[ii][j] != '.') return true;
    }
    return false;
  } 
  if (k == 1) {
    for (int ii = i + 1; ii < R; ii++){
      if (grid[ii][j] != '.') return true;
    }
    return false;    
  }
  if (k == 2) {
    for (int jj = 0; jj < j; jj++)
      if (grid[i][jj] != '.') return true;
    return false;
  }
  if (k == 3) {
    for (int jj = j + 1; jj < C; jj++)
      if (grid[i][jj] != '.') return true;
    return false;
  }
  return false;
}

int main(){
  cin >> t;
  for (int cs = 1; cs <= t; cs++){
    cout << "Case #" << cs << ": ";
    cin >> R >> C;
    grid.resize(R);
    for (int i = 0; i < R; i++) cin >> grid[i];

    bool valid = true;
    int change = 0;

    for (int i = 0; i < R; i++){
      for (int j = 0; j < C; j++){
	char c = grid[i][j];
	if (c == '.') continue;

	int r = find(ch.begin(), ch.end(), c) - ch.begin();
	if (route(i, j, r)) continue;

	bool found = false;
	for (int k = 0; k < 4; k++){
	  if (r == k) continue;
	  if (route(i, j, k)) {
	    change++;
	    found = true;
	    break;
	  }
	}
	if (!found) valid = false;
      }
    }
    if (valid) cout << change << endl;
    else cout << "IMPOSSIBLE" << endl;
  }
  return 0;
}
