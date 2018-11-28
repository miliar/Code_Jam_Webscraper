#include <string>
#include <vector>
#include <cstring>
#include <cmath>
#include <utility>
#include <algorithm>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <list>
#include <iomanip>
#include <ctime>
#include <cassert>
#include <stack>
#include <unordered_map>
#include <unordered_set>

#define what_is(x) cout << #x << " is " << x << endl;

using namespace std;

typedef long long ll;

int dfs (pair<int,int> u, map< pair<int,int>, pair<int,int> >& G, vector<string>& grid, vector< vector<bool> >& visited) {
  if (visited[u.first][u.second]) {
    return 0;
  }
  visited[u.first][u.second] = true;
  if (G[u] == make_pair(-1, -1)) {
    return 1;
  }
  return dfs(G[u], G, grid, visited);
}

void make_graph(vector<string>& grid, map< pair<int,int>, pair<int,int> >& G) {
  int r = grid.size(), c = grid[0].size();
  for (int i = 0; i < r; i++) {
    for (int j = 0; j < c; j++) {
      if(grid[i][j] == '^') {
	bool found = false;
	for (int k = i - 1; k >= 0 && !found; k--) {
	  if (grid[k][j] != '.') {
	    G[make_pair(i,j)] = make_pair(k, j);
	    found = true;
	  }
	}
	if (!found) {
	  G[make_pair(i,j)] = make_pair(-1, -1);
	}
      }
      else if(grid[i][j] == 'v') {
	bool found = false;
	for (int k = i + 1; k < r && !found; k++) {
	  if (grid[k][j] != '.') {
	    G[make_pair(i,j)] = make_pair(k, j);
	    found = true;
	  }
	}
	if (!found) {
	  G[make_pair(i,j)] = make_pair(-1, -1);
	}
      }
      else if (grid[i][j] == '>') {
	bool found = false;
	for (int k = j + 1; k < c && !found; k++) {
	  if (grid[i][k] != '.') {
	    G[make_pair(i,j)] = make_pair(i, k);
	    found = true;
	  }
	}
	if (!found) {
	  G[make_pair(i,j)] = make_pair(-1, -1);
	}
      }
      else if (grid[i][j] == '<') {
	bool found = false;
	for (int k = j - 1; k >= 0 && !found; k--) {
	  if (grid[i][k] != '.') {
	    G[make_pair(i,j)] = make_pair(i, k);
	    found = true;
	  }
	}
	if (!found) {
	  G[make_pair(i,j)] = make_pair(-1, -1);
	}
      }
    }
  }
}

bool check_poss(vector<string>& grid) {
  int r = grid.size(), c = grid[0].size();
  for (int i = 0; i < r; i++) {
    for (int j = 0; j < c; j++) {
      if (grid[i][j] == '.') {
	continue;
      }
      bool found = false;
      for (int k = i - 1; k >= 0 && !found; k--) {
	if (grid[k][j] != '.') {
	  found = true;
	}
      }
      for (int k = i + 1; k < r && !found; k++) {
	if (grid[k][j] != '.') {
	  found = true;
	}
      }
      for (int k = j + 1; k < c && !found; k++) {
	if (grid[i][k] != '.') {
	  found = true;
	}
      }
      for (int k = j - 1; k >= 0 && !found; k--) {
	if (grid[i][k] != '.') {
	  found = true;
	}
      }
      if (!found) {
	return false;
      }
    }
  }
  return true;
}

int main () {
  std::ios::sync_with_stdio(false);
  int t;
  cin >> t;
  for (int i = 0; i < t; i++) {
    int r, c;
    cin >> r >> c;
    vector<string> grid(r);
    vector< vector<bool> > visited(r, vector<bool>(c, false));
    map< pair<int,int>, pair<int,int> > G;
    for (int i = 0; i < r; i++) {
      cin >> grid[i];
    }
    if (!check_poss(grid)) {
      cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
      continue;
    }
    make_graph(grid, G);
    int ans = 0;
    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
	if (grid[i][j] != '.') {
	  ans += dfs(make_pair(i, j), G, grid, visited);
	}
      }
    }
    cout << "Case #" << i + 1 << ": " << ans << endl;
  }
  return 0;
}

