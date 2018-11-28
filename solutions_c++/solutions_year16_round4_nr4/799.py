#include <cstdio>
#include <cassert>
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
#define FOR(v, it) for (auto it = v.begin(); it != v.end(); ++it)

constexpr int N = 5;
bool taken[5];
int perm[5];
int n;
int mat2[N][N];
bool recurse(int idx) {
  if (idx == n) {
#ifdef DEBUG
    for (int i = 0; i < n; ++i) {
      assert(taken[i]);
    }
#endif
    
    return true;
  }
  bool gotten = false;
  for (int j = 0; j < n; ++j) {
    if (mat2[perm[idx]][j] && !taken[j]) {
      gotten = true;
      taken[j] = true;
      bool ans = recurse(idx+1);
      if (!ans) return false;
      taken[j] = false;
    }
  }
  return gotten;
}

int main() {
  int n_cases;
  scanf("%d", &n_cases);
  char str[N];
  int mat[N][N];
  for (int ctr = 0; ctr < n_cases; ++ctr) {
    memset(mat, 0, sizeof(mat));
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
      scanf("%s", str);
      for (int j = 0; j < n; ++j) {
        mat[i][j] = str[j] == '1';
      }
    }
    int best_cost = 1 << 30;

    for (int mask = 0; mask < (1 << (n*n)); ++mask) {
      memset(mat2, 0, sizeof(mat2));
      bool good = true;
      int cost = 0;
#ifdef DEBUG2
      puts("TRY");
#endif
      for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
          bool ok = (mask >> ((i*n) + j)) & 1;
          #ifdef DEBUG2
          printf("%d ", ok);
          #endif
          if (!ok && mat[i][j]) {
            good = false;
            break;
          }
          if (ok && !mat[i][j]) {
            ++cost;
          }
          mat2[i][j] = ok;
        }
        #ifdef DEBUG2
        puts("");
        #endif
        if (!good) break;
      }
      if (!good) continue;

      #ifdef DEBUG2
      printf("GOOD! %d\n", n);
      for (int i = 0; i < n; ++i ){
        for (int j = 0; j < n; ++j) {
          printf("%d ", mat2[i][j]);
        }
        puts("");
      }
      #endif

      bool perfect = true;
      for (int i = 0; i < n; ++i) {
        perm[i] = i;
      }
      do {
        memset(taken, 0, sizeof(taken));
        if (!recurse(0)) {
          perfect = false;
          break;
        }
      } while (next_permutation(perm, perm+n));

      if (perfect) {
        best_cost = min(cost, best_cost);
        continue;
      }
    }

    printf("Case #%d: %d\n", ctr+1, best_cost);
  }
  
  return 0;
}
