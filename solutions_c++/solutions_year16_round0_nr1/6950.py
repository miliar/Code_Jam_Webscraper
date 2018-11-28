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
    ullong n;
    scanf("%llu", &n);
    if (n == 0) {
      printf("Case #%d: INSOMNIA\n", ctr+1);
      continue;
    }
    bool seen[10];
    int cnt = 0;
    memset(seen, 0, sizeof(seen));
    ullong mul;
    for (uint i = 0; ; ++i) {
      ullong x = i*n;
      mul = x;
      while (x > 0) {
        if (!seen[x % 10]) cnt += 1;
        seen[x % 10] = true;
        x /= 10;
      }
      if (cnt == 10) {
        break;
      }
    }
    printf("Case #%d: %llu\n", ctr+1, mul);
  }
  return 0;
}
