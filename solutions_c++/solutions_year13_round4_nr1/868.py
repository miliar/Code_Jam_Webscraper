#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;


const long long mod = 1000002013;
struct Event {
  int pos;
  int type;
  int from;
  int cnt;
  Event() {
  }
  Event (int pos, int type, int from, int cnt):
    pos (pos), type (type), from (from), cnt(cnt) {
    }
};
bool operator < (const Event &a, const Event &b) {
  return a.pos < b.pos || (a.pos == b.pos && a.type < b.type);
}
int N;
int get_cost (int d) {
  if (d == 0) {
    return 0;
  }
  return (long long)(N + N - d + 1) * d / 2 % mod;
}
void run() {
  int edges_n;
  scanf ("%d%d", &N, &edges_n);
  vector <Event> v;
  map <int, long long> C;

  long long res = 0;
  for (int i = 0; i < edges_n; i++) {
    int a, b, p;
    scanf ("%d%d%d", &a, &b, &p);
    v.push_back (Event (a, -1, a, p));
    v.push_back (Event (b, +1, a, p));
    res += get_cost (b - a) * p;
    res %= mod;
  }
  sort (v.begin(), v.end());

  for (int i = 0; i < (int)v.size(); i++) {
    const Event &e = v[i];

    if (e.type == -1) {
      C[e.from] += e.cnt;
    } else {
      long long cnt = e.cnt;
      while (cnt > 0) {
        map <int, long long>::reverse_iterator x = C.rbegin();
        int cur_cost = get_cost (e.pos - x->first);
        long long cur_cnt = min (cnt, x->second);
        cnt -= cur_cnt;
        x->second -= cur_cnt;
        res -= cur_cnt * cur_cost;
        res %= mod;
        if (x->second == 0) {
          map <int, long long>::iterator y = C.end();
          y--;
          C.erase (y);
        }
      }
    }
  }
  assert (C.empty());
  res += mod;
  res %= mod;
  printf ("%d\n", (int)res);
}

int main (void) {
  int test_n;
  scanf ("%d", &test_n);
  for (int test_i = 0; test_i < test_n; test_i++) {
    fprintf (stderr, "%d\n", test_i);
    printf ("Case #%d: ", test_i + 1);
    run();
  }

  return 0;
}
