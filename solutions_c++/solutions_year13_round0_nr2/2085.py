#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>

#define DEBUG 0

using namespace std;

bool checkColumn(vector< vector<int> >&desiredGrid, int y, int num, int N, int M) {
  for (int x = 0; x < N; x++) {
    if (num < desiredGrid[x][y])
      return false;
  }
  return true;
}

bool checkRow(vector< vector<int> >&desiredGrid, int x, int num, int N, int M) {
  for (int y = 0; y < M; y++) {
    if (num < desiredGrid[x][y])
      return false;
  }
  return true;
}


void fill_it_cols(vector< vector<int> >&grid, int y, int num, vector< vector<int> > &desiredGrid, vector< vector<bool> >&done, int N, int M) {
  for (int x = 0; x < N; x++) {
    grid[x][y] = num;
    if (desiredGrid[x][y] == grid[x][y])
      done[x][y] = true;
  }
}

void fill_it_rows(vector< vector<int> >&grid, int x, int num, vector< vector<int> > &desiredGrid, vector< vector<bool> >&done, int N, int M) {
  for (int y = 0; y < M; y++) {
    grid[x][y] = num;
    if (desiredGrid[x][y] == grid[x][y])
      done[x][y] = true;
  }
}


int main ()
{
  int T;
  cin >> T;
  for (int t = 0; t < T; t++) {
    cout << "Case #" << t+1 << ": ";
    int N, M;
    cin >> N >> M;
    vector< vector<int> > desiredGrid(N, vector<int>(M, 100));
    set<int, greater<int> > nums;
    map<int, vector< pair<int,int> > > mp;
#if DEBUG
    cout << endl;
#endif
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < M; j++) {
        cin >> desiredGrid[i][j];
        mp[desiredGrid[i][j]].push_back(make_pair(i,j));
        nums.insert(desiredGrid[i][j]);
#if DEBUG
        cout << desiredGrid[i][j];
#endif
      }
#if DEBUG
      cout << endl;
#endif
    }
#if DEBUG
    cout << endl;
#endif
    vector< vector<int> > grid(N, vector<int>(M, *nums.begin()));
    vector< vector<bool> > done(N, vector<bool>(M, false));
    bool contradiction = false;
    for (set<int>::iterator it = nums.begin();
        it != nums.end();
        it++) {
#if DEBUG
      cout << "nums: " << *it << endl;
#endif
      for (vector<pair<int,int> >::iterator it2 = mp[*it].begin();
          it2 != mp[*it].end();
          it2++) {
        int x = it2->first;
        int y = it2->second;
#if DEBUG
        cout << "x: " << x << ". y: " << y << endl;
#endif
        if (*it == grid[x][y]) {
          done[x][y] = true;
        }
        else {
          // check column
          bool col = checkColumn(desiredGrid, y, *it, N, M);
          if (col) {
            // fill it
            fill_it_cols(grid, y, *it, desiredGrid, done, N, M);
          }
          // check row
          bool row = checkRow(desiredGrid, x, *it, N, M);
          if (row) {
            fill_it_rows(grid, x, *it, desiredGrid, done, N, M);
          }
#if DEBUG
          cout << "col: " << col << ". row: " << row << endl;
#endif
          if (!col && !row) {
            contradiction = true;
            break;
          }
        }
      }
      if (contradiction) {
        break;
      }
    }
    cout << ((contradiction) ? "NO" : "YES") << endl;
  }
}
