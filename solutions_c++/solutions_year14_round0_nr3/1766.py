#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <string>
#include <string.h>
#include <set>
#include <stdio.h>
#include <assert.h>
#include <sstream>
#include <stdlib.h>
using namespace std;

int grid[5][5], seen[5][5], rev[5][5], r, c;
int num[5][5];
void dfs(int i, int j) {
  seen[i][j] = 1;
  rev[i][j] = 1;
  if (num[i][j])
    return;
  for (int dx = -1; dx <= 1; ++dx)
    for (int dy = -1; dy <= 1; ++dy)
      if (!!dx || !!dy) {
	int nx = i+dx, ny = j+dy;
	if ((nx>=0) && (nx<r) && (ny>=0) && (ny<c) && !grid[nx][ny]) {
	  rev[nx][ny] = 1;
	  if (!num[nx][ny] && !seen[nx][ny])
	    dfs(nx, ny);
	}
      }
}
int main(int argc, char* argv[]) {
  int nocases;
  cin >> nocases;
  for (int rr = 1; rr <= nocases; ++rr) {
    int m;
    cin >> r >> c >> m;
    vector<int> v;
    for (int i = 0; i < r*c; ++i)
      if (i < m)
	v.push_back(1);
      else
	v.push_back(0);
    sort(v.begin(), v.end());
    bool found = false;
    printf("Case #%d:\n", rr);
    do {
      for (int i = 0; i < r; ++i)
	for (int j = 0; j < c; ++j)
	  grid[i][j] = v[i*c+j];
      memset(num, 0, sizeof(num));
      for (int i = 0; i < r; ++i)
	for (int j = 0; j < c; ++j)
	  for (int dx = -1; dx <= 1; ++dx)
	    for (int dy = -1; dy <= 1; ++dy) {
	      int nx = i+dx, ny = j+dy;
	      if (nx>=0 && nx<r && (ny>=0) && (ny<c))
		num[i][j] += grid[nx][ny];
	    }
      for (int x = 0; x < r; ++x)
	for (int y = 0; y < c; ++y)
	  if (!grid[x][y]) {
	    memset(seen, 0, sizeof(seen));
	    memset(rev, 0, sizeof(rev));
	    dfs(x, y);
	    bool good = true;
	    for (int i = 0; (i < r) && good; ++i)
	      for (int j = 0; (j < c) && good; ++j)
		if (!grid[i][j] && !rev[i][j])
		  good = false;
	    if (good) {
	      found = true;
	      for (int i = 0; i < r; ++i) {
		for (int j = 0; j < c; ++j)
		  if (i==x && j==y)
		    cout << "c";
		  else if (!grid[i][j])
		    cout << ".";
		  else
		    cout << "*";
		cout << endl;
	      }
	      goto done;
	    }
	  }
    } while(next_permutation(v.begin(), v.end()));
  done:
    if (!found)
      cout << "Impossible" << endl;
  }
  return 0;
}
