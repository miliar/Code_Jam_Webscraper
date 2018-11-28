#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <numeric>
#include <utility>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;
const int M = 1000002013;


struct Travel {
  int o, e, p;
  Travel *pt;
  bool operator<(const Travel &t) const {
    if (e < t.e) return true;
    if (e > t.e) return false;
    return o > t.o;
  }
  bool operator>(const Travel &t) const {
    if (o > t.o) return true;
    if (o < t.o) return false;
    if (e > t.e) return true;
    if (e < t.e) return false;
    return p < t.p;
  }
};

Travel tr[10002];
//priority_queue<Travel> pq;
//priority_queue<Travel, vector<Travel>, greater<Travel> > pq2;
int n, m;


inline long long calc(int a) {
  return (((long long)n + n - a + 1) * a) / 2;
}

inline long long calc(int a, int b, int c, int d) {
  if (a < 0 || b < 0 || c < 0 || d < 0) return -1;
  return calc(a) + calc(b) - calc(c) - calc(d);
}

long long change(int i, int j) {
  long long x = calc(tr[i].e - tr[i].o, tr[j].e - tr[j].o, tr[i].e - tr[j].o, tr[j].e - tr[i].o);
  long long p = min(tr[i].p, tr[j].p);
  tr[i].p -= p;
  tr[j].p -= p;
  
  if (tr[i].e > tr[j].o) {
    tr[m].o = tr[j].o;
    tr[m].e = tr[i].e;
    tr[m].p = p;
    ++m;
  }
 if (tr[j].e > tr[i].o) {
    tr[m].o = tr[i].o;
    tr[m].e = tr[j].e;
    tr[m].p = p;
    ++m;
  }
  return x * p;
}
void solve() {
  scanf("%d%d", &n, &m);
  for (int i = 0; i < m; ++i) {
    scanf("%d%d%d", &tr[i].o, &tr[i].e, &tr[i].p);
  }
//  sort(tr, tr + m, Travel::cmp);

  bool ok;

  long long ret = 0;
  do {
    ok = false;
    vector<pair<long long, pair<int, int> > > v;
    for (int i = 0; i < m; ++i) {
      if (!tr[i].p) continue;
      for (int j = i + 1; j < m; ++j) {
        if (!tr[j].p) continue;
        long long x = calc(tr[i].e - tr[i].o, tr[j].e - tr[j].o, tr[i].e - tr[j].o, tr[j].e - tr[i].o);
        if (x > 0) {
          v.push_back(make_pair(-x, make_pair(i, j)));
        }
      }
    }
    sort(v.begin(), v.end());
    for (size_t i = 0; i < v.size(); ++i) {
      ret += change(v[i].second.first, v[i].second.second);
      ok = true;
      break;
    }
  } while (ok);


/*
  for (int i = 0; i < m; ++i) {
    tr[i].pt = tr + i;
    pq.push(tr[i]);
    pq2.push(tr[i]);
  }

  long long ret = 0;
  while (!pq2.empty()) {
//  for (int i = 0; i < m; ++i) {
    //printf("[%d]: %d %d\n",i, tr[i].o, tr[i].e);
    Travel l = pq2.top();
    //printf("l %d %d\n", l.o, l.e);
    if (l.pt) {
      l.p = l.pt->p;
    }
    pq2.pop();
    vector<Travel> tmp;
    while (l.p && !pq.empty()) {
      //printf("%d %d\n", tr[i].p, pq.size());
      Travel t = pq.top();
      pq.pop();
      if (t.pt) {
        t.p = t.pt->p;
      }
     // printf("pq %d %d\n", t.o, t.e);
      if (l.o >= t.o) continue;
      if (t.o > l.e) {
        tmp.push_back(t);
        continue;
      }
      if (l.e >= t.e) break;
      long long p = min(l.p, t.p);
      ret += p * calc(l.e - l.o, t.e - t.o, l.e - t.o, t.e - l.o);
      t.p -= p;
      if (t.pt) {
        t.pt->p -= p;
      }
      if (t.p) {
        tmp.push_back(t);
        
      }
      if (t.o < l.e) {
        Travel nt;
        nt.p = p;
        nt.o = t.o;
        nt.e = l.e;
        nt.pt = 0;
        tmp.push_back(nt);
        pq2.push(nt);
      }
      l.p -= p;
    }
    for (size_t i = 0; i < tmp.size(); ++i) {
      pq.push(tmp[i]);
    }
  }
*/
  printf("%lld\n", ret);
}

int main() {
  int t;
  scanf("%d", &t);
  for (int tc = 1; tc <= t; ++tc) {
    printf("Case #%d: ", tc);
    solve();
  }
  return 0;
}
