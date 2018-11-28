#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <complex>
#include <numeric>
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

typedef unsigned long long ullong;
typedef long long llong;
typedef list<int> EdgeList;
typedef vector<EdgeList> AdjList;
typedef pair<int, int> ii;
typedef vector<ii> vii;

#define FOR_EDGE(adj,v,it) for (EdgeList::iterator it = adj[v].begin(); \
    it != adj[v].end(); ++it)

int main() {
  int n_cases;
  scanf("%d", &n_cases);

  double arr1[1024];
  int perm[1024];
  double arr2[1024];
  bool taken[1024];
  for (int ctr = 0; ctr < n_cases; ++ctr) {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
      scanf("%lf", &arr1[i]);
    }
    for (int i = 0; i < n; ++i) {
      scanf("%lf", &arr2[i]);
    }
    sort(arr1, arr1+n);
    sort(arr2, arr2+n);

    for (int i = 0; i < n; ++i) perm[i] = i;
    int best_deceit = 0;
    int best_war = 0;

    int deceit = 0;
    int war = 0;
    memset(taken, 0, sizeof(taken));
    // deceit
    for (int i = 0; i < n; ++i) {
      int idx = perm[i];
      bool found = false;

      for (int j = 0; j < n; ++j) {
        if (!taken[j] && arr2[j] < arr1[idx]) {
          deceit += 1;
          found = true;
          taken[j] = true;
          break;
        }
      }
      if (!found) {
        for (int j = n-1; j >= 0; --j) {
          if (!taken[j]) {
            taken[j] = true;
            break;
          }
        }
      }
    }
    memset(taken, 0, sizeof(taken));
    // war
    for (int i = 0; i < n; ++i) {
      int idx = perm[i];
      bool found = false;
      for (int j = 0; j < n; ++j) {
        if (!taken[j] && arr2[j] > arr1[idx]) {
          found = true;
          taken[j] = true;
          break;
        }
      }
      if (!found) {
        war += 1;
        for (int j = 0; j < n; ++j) {
          if (!taken[j]) {
            taken[j] = true;
            break;
          }
        }
      }
    }
    if (deceit > best_deceit) {
      best_deceit = deceit;
    }
    if (war > best_war) {
      best_war = war;
    }

    printf("Case #%d: %d %d\n", ctr+1, best_deceit, best_war);
  }
  
  return 0;
}
