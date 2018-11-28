#include <bits/stdc++.h>

#define REP(i,n) for(int i=0;i<(int)(n);i++)
#define ALL(x) (x).begin(),(x).end()

using namespace std;

string str[128];
int num1[128], num2[128];

void solve(int cas) {
  int R, C; cin >> R >> C;
  REP(i,R) cin >> str[i];
  REP(i,R) REP(j,C) {
    if (str[i][j] != '.') { num1[i]++; num2[j]++; }
  }
  REP(i,R) REP(j,C) {
    if (str[i][j] != '.' && num1[i] == 1 && num2[j] == 1) {
      cout << "Case #" << cas << ": IMPOSSIBLE" << endl;
      return;
    }
  }

  int res = 0;
  REP(i,R) {
    REP(j,C) {
      if (str[i][j] != '.') {
        if (str[i][j] == '<') ++res;
        break;
      }
    }
  }
  REP(i,R) {
    for (int j = C-1; j >= 0; --j) {
      if (str[i][j] != '.') {
        if (str[i][j] == '>') ++res;
        break;
      }
    }
  }
  REP(j,C) {
    REP(i,R) {
      if (str[i][j] != '.') {
        if (str[i][j] == '^') ++res;
        break;
      }
    }
  }
  REP(j,C) {
    for (int i = R-1; i >= 0; --i) {
      if (str[i][j] != '.') {
        if (str[i][j] == 'v') ++res;
        break;
      }
    }
  }
  cout << "Case #" << cas << ": " << res << endl;
}

int main() {
  int T; cin >> T;
  REP(cas,T) {
    memset(num1, 0, sizeof(num1));
    memset(num2, 0, sizeof(num2));
    solve(cas + 1);
  }
  return 0;
}
