#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <map>
#include <set>
#include <sstream>
#include <queue>
#include <algorithm>
#include <utility>
#include <numeric>
#include <functional>
#include <cstddef>
#include <cstdlib>

using namespace std;

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  
  const int DR[] = {1,0,-1,0};
  const int DC[] = {0,1,0,-1};
  const string DIRS = "v>^<";

  int T;
  cin >> T;
  for(int test=1;test<=T;test++) {
    int R, C;
    cin >> R >> C;
    vector<string> grid(R);
    for(int r = 0; r < R; r++)
      cin >> grid[r];
    int result = 0;
    bool ok = true;
    for (int r = 0; r < R; r++) {
      for (int c = 0; c < C; c++) {
        if (grid[r][c] == '.') 
          continue;
        const int dir = DIRS.find(grid[r][c]); 
        int rr = r, cc = c;
        bool good = false;
        while (true) {
          rr += DR[dir];
          cc += DC[dir];
          if (rr < 0 || rr >= R || cc < 0 || cc >= C)
            break;
          if (grid[rr][cc] != '.') {
            good = true;
            break;
          }
        }
        if (!good) {
          bool empty = true;
          for(int d = 0; d < 4; d++) {
            rr = r;
            cc = c;
            while (true) {
              rr += DR[d];
              cc += DC[d];
              if (rr < 0 || rr >= R || cc < 0 || cc >= C)
                break;
              if (grid[rr][cc] != '.') {
                empty = false;
                break;  
              }                
            }
          }
          if (empty) 
            ok = false;
          result++;
        }
      }
    }
    cout << "Case #" << test << ": ";
    if (!ok) 
      cout << "IMPOSSIBLE\n";
    else 
      cout << result << endl;
  }

  return 0;
}
