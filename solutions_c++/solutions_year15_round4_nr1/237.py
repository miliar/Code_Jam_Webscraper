#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <vector>
using namespace std;

#define REP2(i, m, n) for(int i = (int)(m); i < (int)(n); i++)
#define REP(i, n) REP2(i, 0, n)
#define ALL(c) (c).begin(), (c).end()
#define FOREACH(i, c) for(auto i = (c).begin(); i != (c).end(); ++i)
#define BIT(n, m) (((n) >> (m)) & 1)

typedef long long ll;

const ll inf = 1e15;
const ll mod = 1000 * 1000 * 1000 + 7;
const double eps = 1e-9;

void solve(){
  int R, C;
  cin >> R >> C;
  vector<string> board(R);
  REP(i, R) cin >> board[i];

  int sum = 0;
  REP(r, R) REP(c, C) if (board[r][c] != '.'){
    int dr[] = {0, 1, -1, 0};
    int dc[] = {1, 0, 0, -1};
    int count[4] = {0, 0, 0, 0};
    REP(i, 4){
      int nr = r + dr[i];
      int nc = c + dc[i];
      while (0 <= nr && nr < R && 0 <= nc && nc < C){
        count[i] += board[nr][nc] != '.';
        nr += dr[i];
        nc += dc[i];
      }
    }

    if (accumulate(count, count + 4, 0) == 0) {
      cout << "IMPOSSIBLE" << endl;
      return;
    } else {
      int idx = 0;
      if (board[r][c] == '>') idx = 0;
      if (board[r][c] == '<') idx = 3;
      if (board[r][c] == '^') idx = 2;
      if (board[r][c] == 'v') idx = 1;
      if (count[idx] == 0) sum++;
    }
  }
  cout << sum << endl;
}
 
int main(){
  int T;
  cin >> T;
  REP(t, T){
    printf("Case #%d: ", t + 1);
    solve();
  }
  return 0;
}
