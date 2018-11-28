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

int main() {
  int n_cases;
  scanf("%d", &n_cases);
  for (int ctr = 0; ctr < n_cases; ++ctr){
    char str[1024];
    int arr[1024];
    int k;
    scanf("%s %d", str, &k);
    int n = strlen(str);
    for (int i = 0; i < n; ++i) {
      arr[i] = str[i] == '+' ? 1 : 0;
    }
    // greed is good
    int flips = 0;
    for (int i = 0; i < n - k + 1; ++i) {
      if (!arr[i]) {
        flips += 1;
        for (int j = i; j < i + k; ++j) {
          arr[j] ^= 1;
        }
      }
    }
    if (all_of(arr, arr+n, [](int x) { return x == 1; })) {
      printf("Case #%d: %d\n", ctr+1, flips);
    } else {
      printf("Case #%d: IMPOSSIBLE\n", ctr+1);
    }
  }
  return 0;
}
