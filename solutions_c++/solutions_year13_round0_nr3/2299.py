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

bool is_palindrome(ullong x) {
  char str[30];
  memset(str, 0, sizeof(str));
  sprintf(str, "%llu", x);
  int len = strlen(str);
  for (int i = 0; i < len; ++i) {
    if (str[i] != str[len-1-i]) return false;
  }
  return true;
}

const ullong LIMIT = 20000000ULL;
// only works for small and large-1
int main() {
  vector<ullong> vec;
  // precompute!
  for (ullong i = 1; i <= LIMIT; ++i) {
    if (is_palindrome(i)) {
      ullong sq = i*i;
      if (is_palindrome(sq)) {
        vec.push_back(sq);
      }
    }
  }
  
  int n_cases;
  scanf("%d", &n_cases);
  for (int ctr = 0; ctr < n_cases; ++ctr) {
    ullong a, b;
    scanf("%llu %llu", &a, &b);

    int cnt = upper_bound(vec.begin(), vec.end(), b) - lower_bound(vec.begin(), vec.end(), a);
    printf("Case #%d: %d\n", ctr+1, cnt);
  }

  return 0;
}
