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
string arr[10];
int m, n;
int assignment[10];
int best;
int best_cnt;

void recurse(int idx) {
  if (idx == m) {
    set<string> prefixes;
    int val = 0;
    for (int i = 0; i < n; ++i) {
#ifdef DEBUG
      printf("Assigned to %d: ", i);
#endif
      for (int j = 0; j < m; ++j) {
        if (assignment[j] == i) {
          // part of server i
#ifdef DEBUG
          printf("%d ", j);
#endif
          for (int k = 0; k <= arr[j].size(); ++k) {
            prefixes.insert(arr[j].substr(0, k));
          }
        }
      }
#ifdef DEBUG
      puts("");
      
      printf("PREFIXES\n");
      for (set<string>::iterator it = prefixes.begin(); it != prefixes.end(); ++it) {
        printf("'%s' ", it->c_str());
      }
      puts("");
#endif
      val += prefixes.size();
      prefixes.clear();
    }
    if (val > best) {
      best = val;
      best_cnt = 0;
    }
    if (val == best) {
      ++best_cnt;
    }
    return;
  }

  for (int i = 0; i < n; ++i) {
    assignment[idx] = i;
    recurse(idx + 1);
  }
}

int main() {
  int n_cases;
  scanf("%d", &n_cases);
  char str[32];
  for (int ctr = 0; ctr < n_cases; ++ctr) {
    best = -1;
    best_cnt = 0;
    scanf("%d %d", &m, &n);
    for (int i = 0; i < m; ++i) {
      scanf("%s", str);
      arr[i] = string(str);
    }

    recurse(0);

    printf("Case #%d: %d %d\n", ctr+1, best, best_cnt);
  }
}
