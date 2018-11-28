#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cassert>
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

int main() {
  int n_cases;
  scanf("%d", &n_cases);
  
  for (int ctr = 0; ctr < n_cases; ++ctr) {
    int x, r, c;
    scanf("%d %d %d", &x, &r, &c);
    if (r < c) swap(r, c);
    assert(r <= 4);
    if (x == 1) {
      printf("Case #%d: GABRIEL\n", ctr+1);
    } else if (x == 2) {
      if (r*c % 2 == 0) {
        printf("Case #%d: GABRIEL\n", ctr+1);
      } else {
        printf("Case #%d: RICHARD\n", ctr+1);
      }
    } else if (x == 3) {
      if (r <= 2) printf("Case #%d: RICHARD\n", ctr+1);
      else if (r == 3) {
        if (c == 1) printf("Case #%d: RICHARD\n", ctr+1);
        else {
          printf("Case #%d: GABRIEL\n", ctr+1);
        }
      } else { 
        if (c == 1) {
          printf("Case #%d: RICHARD\n", ctr+1);
        } else if (c == 2) {
          printf("Case #%d: RICHARD\n", ctr+1);
        } else if (c == 3) {
          printf("Case #%d: GABRIEL\n", ctr+1);
        } else {
          printf("Case #%d: RICHARD\n", ctr+1);
        }
      }
    } else if (x == 4) {
      if (r <= 3) {
        printf("Case #%d: RICHARD\n", ctr+1);
      } else {
        if (c == 1) printf("Case #%d: RICHARD\n", ctr+1);
        else if (c == 2) printf("Case #%d: RICHARD\n", ctr+1); // T
        else if (c == 3) printf("Case #%d: GABRIEL\n", ctr+1);
        else printf("Case #%d: GABRIEL\n", ctr+1);
      }
    }
  }
  
  return 0;
}
