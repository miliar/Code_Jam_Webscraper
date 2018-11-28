#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <set>
using namespace std;
using ll = long long;

class range {private: struct I{int x;int operator*(){return x;}bool operator!=(I& lhs){return x<lhs.x;}void operator++(){++x;}};I i,n;
public:range(int n):i({0}),n({n}){}range(int i,int n):i({i}),n({n}){}I& begin(){return i;}I& end(){return n;}};

void solve();

int main() {
  int T; cin >> T;
  for (int test : range(1, T+1)) {
    cout << "Case #" << test << ": ";
    solve();
  }
}

////////////////////////////////////////////////////////////////////////////////

void solve() {
  int H, W;
  cin >> H >> W;
  string f[H];
  for (int i : range(H)) cin >> f[i];

  const int di[4] = {-1, 0, 1, 0};
  const int dj[4] = {0, -1, 0, 1};

  int enc[256];
  enc['^'] = 0;
  enc['<'] = 1;
  enc['v'] = 2;
  enc['>'] = 3;

  int ret = 0;
  for (int i : range(H))
  for (int j : range(W)) {
    if (f[i][j] != '.') {
      vector<int> ex(4, 0);
      for (int r : range(4)) {
        int ai = i + di[r], aj = j + dj[r];

        for (;;) {
          if (ai < 0 || ai >= H || aj < 0 || aj >= W) break;
          if (f[ai][aj] != '.') ex[r] = 1;

          ai += di[r];
          aj += dj[r];
        }
      }
      int arrow = enc[(int)f[i][j]];
      if (ex[arrow]) {
        ;
      } else {
        if (accumulate(ex.begin(), ex.end(), 0) == 0) ret += 90000;
        else ret++;
      }
    }
  }

  if (ret >= 90000) cout << "IMPOSSIBLE" << endl;
  else cout << ret << endl;
}

