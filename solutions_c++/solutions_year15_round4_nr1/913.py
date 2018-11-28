#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <map>
#include <queue>
#include <ctime>
#include <cmath>

using namespace std;

#define forn(I,N) for (int I=0; I<N; I++)
#define fornd(I,N) for (int I=N-1; I>=0; I--)
#define forab(I,A,B) for (int I=A; I<=B; I++)
#define forabd(I,A,B) for (int I=B; I>=A; I--)
#define FOREACH(I,A) for (__typeof__(A)::iterator I=A.begin(); I<A.end(); I++)
#define pb push_back
#define mp make_pair

typedef long long int ll;

int checkSafe(int r, int c, char dir, vector<vector<char> > & grid, vector<vector<bool> > & safe, vector<vector<bool> > & visited) {
  int R = grid.size();
  int C = grid[0].size();

  //cout << r << " " << c << endl;
  if(r < 0 || c < 0 || r >= R || c >= C) {
    return -1;
  }

  if(visited[r][c] && grid[r][c] != '.') {
    safe[r][c] = true;
    return 0;
  }
  if(grid[r][c] != '.' && safe[r][c]) {
    return 0;
  }

  visited[r][c] = true;
  int isSafe;
  //cout << "dir" << dir << endl;
  if(grid[r][c] != '.') {
    dir = grid[r][c];
  }
  if(dir =='^') {
    isSafe = checkSafe(r - 1, c, dir, grid, safe, visited);
  }
  else if(dir == 'v') {
    isSafe = checkSafe(r + 1, c, dir, grid, safe, visited);
  }
  else if(dir == '>') {
    isSafe = checkSafe(r, c + 1, dir, grid, safe, visited);
  }
  else {
    isSafe = checkSafe(r, c - 1, dir, grid, safe, visited);
  }

  if(isSafe >= 0 || grid[r][c] == '.') {
    if(isSafe) {
      safe[r][c] = true;
    }
    //cout << dir << endl;
    //cout << r << " " << c << " " << grid[r][c] << endl;
    return isSafe;
  }

  grid[r][c] = '^';
  isSafe = checkSafe(r - 1, c, grid[r][c], grid, safe, visited);
  if(isSafe >= 0) {
    safe[r][c] = true;
  //cout << r << " " << c << grid[r][c] << endl;
    return isSafe + 1;
  }

  grid[r][c] = 'v';
  isSafe = checkSafe(r + 1, c, grid[r][c], grid, safe, visited);
  if(isSafe >= 0) {
    safe[r][c] = true;
  //cout << r << " " << c << grid[r][c] << endl;
    return isSafe + 1;
  }

  grid[r][c] = '>';
  isSafe = checkSafe(r, c + 1, grid[r][c], grid, safe, visited);
  if(isSafe >= 0) {
    safe[r][c] = true;
  //cout << r << " " << c << grid[r][c] << endl;
    return isSafe + 1;
  }

  grid[r][c] = '<';
  isSafe = checkSafe(r, c - 1, grid[r][c], grid, safe, visited);
  if( isSafe >= 0) {
    safe[r][c] = true;
  //cout << r << " " << c << grid[r][c] << endl;
    return isSafe + 1;
  }

  return -1;
}

int main() {
  int T;
  cin >> T;

  forn(i, T) {
    int R, C;
    cin >> R >> C;

    vector<vector<char> > grid(R, vector<char>(C));
    vector<vector<bool> > safe(R, vector<bool>(C));

    forn(j, R) {
      forn(k, C) {
        cin >> grid[j][k];
      }
    }

    bool possible = true;
    int counter = 0;
    forn(j, R) {
      forn(k, C) {
        if(!safe[j][k]) {
          if(grid[j][k] == '.') {
            safe[j][k] = true;
          }
          else {
            vector<vector<bool> > visited(R, vector<bool>(C));
            int temp = checkSafe(j, k, '.', grid, safe, visited);
            //cout << temp << endl;
            if(temp == -1) {
              possible = false;
              break;
            }
            else {
              counter += temp;
            }
          }
        }
      }
      if(!possible) {
        break;
      }
    }

    cout << "Case #" << i + 1 << ": ";
    if(possible) {
      cout << counter << endl;
    }
    else {
      cout << "IMPOSSIBLE" << endl;
    }
  }

  return 0;
}
