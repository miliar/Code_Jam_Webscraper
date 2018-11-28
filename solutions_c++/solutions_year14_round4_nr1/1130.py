#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
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
#include <complex>

using namespace std;

typedef list<int> EdgeList;
typedef vector<EdgeList> AdjList;
typedef pair<int, int> ii;
typedef vector<ii> vii;

#define FOR_EDGE(adj,v,it) for (EdgeList::iterator it = adj[v].begin(); \
    it != adj[v].end(); ++it)

struct Point : public complex<double> {
  int idx;
  double& operator[](int idx) {
    if (idx == 0) return complex<double>::real();
    else return complex<double>::imag();
  }
  const double& operator[](int idx) const {
    if (idx == 0) return complex<double>::real();
    else return complex<double>::imag();
  }
};
#define X(p) real(p)
#define Y(p) imag(p)


struct Cmp {
  int idx;
  Cmp(int idx): idx(idx){};
  bool operator()(const Point& p1, const Point& p2) const {
    return p1[idx] < p2[idx];
  }
};

int main() {
  int n_cases;
  scanf("%d", &n_cases);
  int arr[10024];
  int perm[12];
  for (int ctr = 0; ctr < n_cases; ++ctr) {
    int n, x;
    scanf("%d %d", &n, &x);
    for (int i = 0; i < n; ++ i) {
      scanf("%d", &arr[i]);
    }
    printf("Case #%d: ", ctr+1);

    set<ii> mset;
    for (int i = 0; i < n; ++i) {
      mset.insert(ii(arr[i], i));
    }
    
    int n_discs = 0;
    while (mset.size()) {
      if (mset.size() == 1) {
        ++n_discs;
        mset.clear();
        continue;
      }
      ii vv = *mset.begin();
      int v = mset.begin()->first;
      set<ii>::iterator it = mset.upper_bound(make_pair(x-v, n+1));
      --it;
      int u = it->first;
      ii uu = *it;
      mset.erase(vv);
      if (x - u >= v) {
        mset.erase(uu);
      }
      ++n_discs;
    }
    printf("%d\n", n_discs);
  }
}
