#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <string.h>
#include <algorithm>
#include <set>
#include <cstdio>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;

int main() {
  int TC; cin >> TC;
  for (int t = 1; t <= TC; t++) {
    int N, M; cin >> N >> M;
    vvi grass(N, vi(M));
    for(int i = 0; i < N; ++i) {
      for(int j = 0; j < M; ++j) {
        cin >> grass[i][j];
      }
    }
    vi rows(N, -1);
    vi cols(M, -1);

    bool ok = true;

    for(int i = 0; i < N; ++i) {
      int l = 0;
      for(int j = 0; j < M; ++j) {
        l = max(l, grass[i][j]);
      }
      rows[i] = l;
      for(int j = 0; j < M; ++j) {
        if(grass[i][j] != l) {
          if(cols[j] != -1) {
            if(cols[j] != grass[i][j]) ok = false;
          } else {
            cols[j] = grass[i][j];
          }
        }
      }
    }
    for(int j = 0; j < M; ++j) {
      if(cols[j] == -1) continue;
      for(int i = 0; i < N; ++i) {
        if(grass[i][j] != cols[j]) ok =false;
      }
    }
    
    printf("Case #%d: %s\n", t, (ok ? "YES" : "NO"));
  }


  return 0;
}
