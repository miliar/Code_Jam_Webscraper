//
#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <stack>
#include <fstream>
#include <sstream>

using namespace std;

int main() {
  vector < vector < pair < int, int > > > G;
  int T[105][105], maxR[105], maxC[105];
  int nT, iT = 1, n, m;
  scanf("%d", &nT);
  while (nT--) {
    scanf("%d%d", &n, &m);
    memset(maxR, 0, sizeof maxR);
    memset(maxC, 0, sizeof maxC);
    G.assign(101, vector < pair < int, int > > ());
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        scanf("%d", &T[i][j]);
        maxR[i] = max(maxR[i], T[i][j]);
        maxC[j] = max(maxC[j], T[i][j]);
        G[T[i][j]].push_back(make_pair(i, j));
      }
    }
          
    bool can = false;
    for (int h = 1, r, c; h <= 100; h++) {
      for (int i = 0; i < G[h].size(); i++) {
        r = G[h][i].first;
        c = G[h][i].second;
        if (maxR[r] > h && maxC[c] > h) goto ans;
      }
    }
    can = true;
ans:
    printf("Case #%d: ", iT++);
    if (can) printf("YES\n");
    else printf("NO\n");
  }
  return 0;
}
