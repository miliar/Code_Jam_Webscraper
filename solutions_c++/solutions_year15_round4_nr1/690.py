#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;
#define DEBUG(x) cerr << '>' << #x << ':' << (x) << endl;
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define REP(i,a) for(int i=0; i<(a);++i)
inline bool EQ(double a, double b) {return fabs(a-b) < 1e-9;}

const int INF = 1<<29;
typedef long long ll;

int R, C;
char A[200][200];

const int UP = 0;
const int RIGHT = 1;
const int DOWN = 2;
const int LEFT = 3;

bool isSafe(int x, int y, int d) {
  if (d == UP) {
    --y;
    while (y >= 0 && A[y][x] == '.') --y;
    return y >= 0;
  }
  if (d == DOWN) {
    ++y;
    while (y < R && A[y][x] == '.') ++y;
    return y < R;
  }
  if (d == LEFT) {
    --x;
    while (x >= 0 && A[y][x] == '.') --x;
    return x >= 0;
  }
  if (d == RIGHT) {
    ++x;
    while (x < C && A[y][x] == '.') ++x;
    return x < C;
  }
  abort();
}

int solve() {
  scanf("%d%d ", &R, &C);
  char buf[200];
  REP(i,R) {
    gets(buf);
    REP(j,C) {
      A[i][j] = buf[j];
    }
  }
  vector<pair<int, int>> arrows;
  int total = 0;
  REP(y,R) REP(x,C) {
    if (A[y][x] == '.') continue;
    bool anySafe = false;
    bool defaultSafe = false;
    REP(i,4) {
      bool safe = isSafe(x, y, i);
      if (safe) anySafe = true;
      bool isDefault = false;
      isDefault |= (i == UP && A[y][x] == '^');
      isDefault |= (i == DOWN && A[y][x] == 'v');
      isDefault |= (i == LEFT && A[y][x] == '<');
      isDefault |= (i == RIGHT && A[y][x] == '>');
      if (isDefault) {
        defaultSafe = safe;
      }
    }
    if (!anySafe) {
      return -1;
    }
    total += !defaultSafe;
  }
  return total;
}

int main() {
  int T;
  scanf("%d", &T);
  REP(t,T) {
    int s = solve();
    if (s >= 0) {
      printf("Case #%d: %d\n", t+1, s);
    } else {
      printf("Case #%d: IMPOSSIBLE\n", t+1);
    }
  }
  return 0;
}
