#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <queue>
#include <set>
#include <sstream>
#include <cmath>

#define REP(i, N) for (int i = 0; i < (int)N; i++)
#define MP(a, b) make_pair(a, b)
using namespace std;
typedef long long LL;
typedef pair<int, int> PII;
int nextInt() {
  char c;
  int res = 0;
  while (!isdigit(c = getchar())){};
  do {
    res = res * 10 + c - '0';
  } while (isdigit(c = getchar()));
  return res;
}

int R, C;
int table[111][111];
string solve() {
  int rmax[111], cmax[111];
  REP(i, 111) rmax[i] = cmax[i] = 0;
  REP(i, R) {
    REP(j, C) {
      rmax[i] = max(table[i][j], rmax[i]);
      cmax[j] = max(table[i][j], cmax[j]);
    }
  }
  int cnt = 0;
  REP(i, R) {
    REP(j, C) {
      if (table[i][j] >= rmax[i] || table[i][j] >= cmax[j]) cnt++;
    }
  }
  return cnt == R*C ? "YES" : "NO";
}

int main() {
  int T;
  cin >> T;
  REP(tt, T) {
    cin >> R >> C;
    REP(i, R) REP(j, C) {
      cin >> table[i][j];
    }
    printf("Case #%d: ", tt + 1);
    cout << solve() << endl;
  }
}
