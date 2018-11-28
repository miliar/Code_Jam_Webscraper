#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <utility>
#include <cctype>
#include <numeric>
using namespace std;

#define rep(i,n) for(int (i)=0; (i)<(int)(n); ++(i))
#define foreach(c,i) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)

vector<string> m;
const string blah[4] = { "X won", "O won", "Draw", "Game has not completed" };

int f() {
  const char tgt[2] = {'X', 'O'};
  rep(i,2) {
    // vertical
    rep(j,4) {
      bool ok = true;
      rep(k,4) {
        if (m[j][k] != tgt[i] && m[j][k] != 'T') {
          ok = false;  break;
        }
      }
      if (ok) return i;
    }
    // horizontal
    rep(j,4) {
      bool ok = true;
      rep(k,4) {
        if (m[k][j] != tgt[i] && m[k][j] != 'T') { ok = false; break; }
      }
      if (ok) return i;
    }
  }
  // diagonal
  for (int i = 0; i < 2; ++i) {
    // upper left
    bool ok = true;
    for (int j = 0; j < 4; ++j) {
      if (m[j][j] != tgt[i] && m[j][j] != 'T') { ok = false; break; }
    }
    if (ok) return i;
    // upper right
    ok = true;
    for (int j = 0, k = 3; j < 4; ++j,--k) {
      if (m[j][k] != tgt[i] && m[j][k] != 'T') { ok = false; break; }
    }
    if (ok) return i;
  }
  // map is full
  bool isFull = true;
  rep(i,4) {
    rep(j,4) {
      if (m[i][j] == '.') { isFull = false; break; }
    }
  }
  if (isFull) return 2;
  return 3;
}

int main() {
  // ios_base::sync_with_stdio(false);
  int T;
  cin >> T;
  for (int z = 1; z <= T; ++z) {
    m.clear();
    rep(i,4) {
      string s;
      cin >> s;
      m.push_back(s);
    }
    cout << "Case #" << z << ": " << blah[f()] << endl;
  }
  return 0;
}
