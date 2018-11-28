#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <complex>
#include <numeric>
#include <ext/numeric>
#include <iostream>
#include <algorithm>
#include <set>
#include <string>
#include <map>
#include <functional>
#include <utility>
#include <vector>
#include <list>
#include <queue>
#include <bitset>

using namespace std;
using namespace __gnu_cxx;

typedef unsigned long long ullong;
typedef long long llong;
typedef list<int> EdgeList;
typedef vector<EdgeList> AdjList;
typedef pair<int, int> ii;
typedef vector<ii> vii;

#define FOR_EDGE(adj,v,it) for (EdgeList::iterator it = adj[v].begin(); \
    it != adj[v].end(); ++it)

int grid[128][128];
bool reachable[128][128];

int main() {
  int n_cases;
  scanf("%d", &n_cases);

  for (int ctr = 0; ctr < n_cases; ++ctr) {
    memset(grid, 0, sizeof(grid));
    memset(reachable, 0, sizeof(reachable));

    int n, m;
    scanf("%d %d", &n, &m);
    for (int i = 1; i <= n; ++i) {
      for (int j = 1; j <= m; ++j) {
        scanf("%d", &grid[i][j]);
      }
    }
 
    // rows
    for (int i = 1; i <= n; ++i) {
      int highest = 1;
      for (int j = 1; j <= m; ++j) {
        highest = max(highest, grid[i][j]);
      }
      for (int j = 1; j <= m; ++j) {
        if (grid[i][j] == highest) reachable[i][j] = true;
      }
    }

    // cols
    for (int i = 1; i <= m; ++i) {
      int highest = 1;
      for (int j = 1; j <= n; ++j) {
        highest = max(highest, grid[j][i]);
      }
      for (int j = 1; j <= n; ++j) {
        if (grid[j][i] == highest) reachable[j][i] = true;
      }
    }

    bool good = true;
    for (int i = 1; good && i <= n; ++i) {
      for (int j = 1; j <= m; ++j) {
        if (!reachable[i][j]) {
          good = false;
          break;
        }
      }
    }
    
    printf("Case #%d: ", ctr+1);
    if (good) puts("YES");
    else puts("NO");
  }

  return 0;
}
