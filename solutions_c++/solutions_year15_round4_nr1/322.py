#include <bits/stdc++.h>
using namespace std;

const int MAXR = 101;
const int MAXC = 101;
const string D = ">v<^";
const int di[] = {0,1,0,-1};
const int dj[] = {1,0,-1,0};

int R, C;
char G[MAXR][MAXC];

int main() {
  int T; cin >> T;

  for(int tc = 1; tc <= T; ++tc) {
    cout << "Case #" << tc << ": ";
    cin >> R >> C;
    for(int i = 0; i < R; ++i) {
      for(int j = 0; j < C; ++j) {
        cin >> G[i][j];
      }
    }
    try {
      int res = 0;
      for(int i = 0; i < R; ++i) {
        for(int j = 0; j < C; ++j) {
          if(G[i][j] == '.') continue;
          int d = D.find(G[i][j]);
          set<int> ks;
          for(int k = 0; k < 4; ++k) {
            int pi = i;
            int pj = j;
            while(1) {
              pi += di[k];
              pj += dj[k];
              if(pi < 0 || pi >= R) break;
              if(pj < 0 || pj >= C) break;
              if(G[pi][pj] != '.') {
                ks.insert(k);
                break;
              }
            }
          }
          if(ks.count(d)) continue;
          if(ks.empty()) throw 0;
          ++res;
        }
      }
      cout << res << endl;
    } catch(...) {
      cout << "IMPOSSIBLE" << endl;
    }

  }
  return 0;
}
