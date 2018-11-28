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

char cmap[] = {'P', 'R', 'S'};
int vmap[] = {1, 0, 2};

int main() {
  int n_cases;
  scanf("%d", &n_cases);
  for (int ctr = 0; ctr < n_cases; ++ctr) {
    llong n;
    llong r, p ,s;
    scanf("%lld %lld %lld %lld", &n, &r, &p, &s);

    int arr[24];
    for (int i = 0; i < p; ++i) {
      arr[i] = 0;
    }
    for (int i = 0; i < r; ++i) {
      arr[i+p] = 1;
    }
    for (int i = 0; i < s; ++i) {
      arr[i+p+r] = 2;
    }
    n = (1 << n);
    bool ok = false;
    do {
      int tmp[24];
      copy(arr, arr+n, tmp);
      bool tie = false;
      for (int delta = 1; delta < n; delta *= 2) {
        for (int i = 0; i < n; i += 2*delta) {
#ifdef DEBUG
          printf("%d (%d) vs %d (%d): ", tmp[i], i, tmp[i+delta], i + delta);
#endif
          if (tmp[i] == tmp[i + delta]) {
            #ifdef DEBUG
            puts("TIE");
            #endif
            tie = true;
            break;
          } else {
            if ((vmap[tmp[i]] + 1) % 3 == vmap[tmp[i + delta]]) {
#ifdef DEBUG
              printf("w1\n");
#endif
              tmp[i] = tmp[i + delta];
            } else {
              // win first
#ifdef DEBUG
              printf("w0\n");
#endif
            }
          }
        }
        if (tie) break;
      }
      if (!tie) {
        ok = true;
        break;
      }
    } while (next_permutation(arr, arr+n));

    if (ok) {
      printf("Case #%d: ", ctr+1);
      for (int i = 0; i < n; ++i) {
        printf("%c", cmap[arr[i]]);
      }
      puts("");
    } else {
      printf("Case #%d: IMPOSSIBLE\n", ctr+1);
    }
  }
  return 0;
}
