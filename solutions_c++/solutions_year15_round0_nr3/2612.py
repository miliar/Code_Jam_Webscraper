// Uses Eigen: http://eigen.tuxfamily.org/index.php?title=Main_Page
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
#include <eigen3/Eigen/Geometry>

using namespace std;
using namespace __gnu_cxx;
using Eigen::Quaternion;

typedef unsigned long long ullong;
typedef long long llong;
typedef list<int> EdgeList;
typedef vector<EdgeList> AdjList;
typedef pair<int, int> ii;
typedef vector<ii> vii;

#define FOR_EDGE(adj,v,it) for (EdgeList::iterator it = adj[v].begin(); \
    it != adj[v].end(); ++it)

bool operator==(Quaternion<int> const & lhs, Quaternion<int> const & rhs) {
  return lhs.w() == rhs.w() && lhs.x() == rhs.x() && lhs.y() == rhs.y() && lhs.z() == rhs.z();
}

bool operator!=(Quaternion<int> const & lhs, Quaternion<int> const & rhs) {
  return lhs.w() != rhs.w() || lhs.x() != rhs.x() || lhs.y() != rhs.y() || lhs.z() != rhs.z();
}

int main() {
  int n_cases;
  scanf("%d", &n_cases);

  Quaternion<int> arr[10000];
  Quaternion<int> *cache[10000];
  for (int i = 0; i < 10000; ++i) {
    cache[i] = new Quaternion<int>[10000];
  }
  const Quaternion<int> I = Quaternion<int>(0, 1, 0, 0);
  const Quaternion<int> J = Quaternion<int>(0, 0, 1, 0);
  const Quaternion<int> K = Quaternion<int>(0, 0, 0, 1);
  for (int ctr = 0; ctr < n_cases; ++ctr) {
    int l, x;
    scanf("%d%d", &l, &x);
    getchar();
    for (int i = 0; i < l; ++i) {
      char ch = getchar();
      if (ch == 'i') {
        arr[i] = I;
      } else if (ch == 'j') {
        arr[i] = J;
      } else if (ch == 'k') {
        arr[i] = K;
      }
    }
    if (l*x < 3) {
      printf("Case #%d: NO\n", ctr+1);
      continue;
    }
    for (int i = 1; i < x; ++i) {
      copy(arr, arr+l, arr+l*i);
    }

    for (int i = 0; i < l*x; ++i) {
      cache[i][i] = arr[i];
      for (int j = i+1; j < l*x; ++j) {
        cache[i][j] = cache[i][j-1] * arr[j];
      }
    }
    bool ok = false;
    for (int i = 0; i < l*x-2; ++i) {
      if (cache[0][i] != I) continue;
      for (int j = i+1; j < l*x-1; ++j) {
        if (cache[i+1][j] != J || cache[j+1][l*x-1] != K) continue;
        ok = true;
        break;
      }
      if (ok) break;
    }
    if (ok) printf("Case #%d: YES\n", ctr+1);
    else printf("Case #%d: NO\n", ctr+1);
  }
  
  return 0;
}
