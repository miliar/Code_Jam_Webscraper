#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

#define M 1000002013
int o[2000], e[2000], p[2000], ord[2000], n;

long long cost(int a, int b) {
  return ((a - b) * 1LL * n - (1LL * a - b) * (1LL * a - b - 1) / 2) % M;
}

bool cmp(int a, int b) {
  return o[a] < o[b];
}

bool cmpoff(pair<int, int> a, pair<int, int> b) {
  return b < a;
}

int work() {
  vector<pair<int, int> > train, off;
  int m;
  scanf("%d%d", &n, &m);
  long long c1 = 0;
  for (int i = 0; i < m; ++i) {
    scanf("%d%d%d", &o[i], &e[i], &p[i]);
    ord[i] = i;
    c1 = (c1 + cost(o[i], e[i]) * p[i]) % M;
  }
  sort(ord, ord + m, cmp);
  long long c2 = 0;
  for (int i = 0; i <= m; ++i) {
    int curstop;
    if (i == m) 
      curstop = n + 1;
    else 
      curstop = o[ord[i]];
    while (off.size() && off[0].first < curstop) {
      int p = train[0].second;
      int o = train[0].first;
      int e = off[0].first;
      int p2 = off[0].second;
      if (p > p2) p = p2;
      c2 = (c2 + cost(o, e) * p) % M;
#ifdef MY
      printf("Off %d %d %d\n", o, e, p);
#endif
      train[0].second -= p;
      off[0].second -= p;
      if (train[0].second == 0) {
        pop_heap(train.begin(), train.end());
        train.pop_back();
      }
      if (off[0].second == 0) {
        pop_heap(off.begin(), off.end(), cmpoff);
        off.pop_back();
      }
    }
    if (i == m) break;
    for (; i < m && o[ord[i]] == curstop; ++i) {
      train.push_back(make_pair(o[ord[i]], p[ord[i]]));
      off.push_back(make_pair(e[ord[i]], p[ord[i]]));
#ifdef MY
      printf("On %d %d %d\n", o[ord[i]], e[ord[i]], p[ord[i]]);
#endif
      push_heap(train.begin(), train.end());
      push_heap(off.begin(), off.end(), cmpoff);
    }
    --i;
  }
  return (c1 - c2 + M) % M;
}

int main() {
  int t;
  scanf("%d", &t);
  for (int i = 1; i <= t; ++i)  {
    printf("Case #%d: %d\n", i, work());
  }
}
