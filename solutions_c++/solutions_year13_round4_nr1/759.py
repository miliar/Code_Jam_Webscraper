#include <algorithm>
#include <functional>

#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <string>
#include <vector>
#include <map>

using namespace std;

typedef long long llint;

const llint mod = 1000002013;

struct Event {
  int type;
  int x;
  llint cnt;

  friend bool operator < (const Event& a, const Event& b) {
    if (a.x != b.x) return a.x < b.x;
    return a.type < b.type;
  }
};

int N, M;

int main(void)
{
  int T; scanf("%d", &T);

  for (int counter = 0; counter < T; ++counter) {
    vector<Event> events;
    map<int, llint> left;

    llint orig_cost = 0;

    scanf("%d %d", &N, &M);
    for (int i = 0; i < M; ++i) {
      int a, b, c; scanf("%d %d %d", &a, &b, &c); --a, --b;
      events.push_back((Event){0, a, c});
      events.push_back((Event){1, b, c});
      llint d = b - a;
      orig_cost += c * (llint)( (N*d - (d-1)*d/2) % mod ) % mod;
      orig_cost %= mod;
    }

    sort(events.begin(), events.end());
    llint cost = 0;

    for (vector<Event>::iterator it = events.begin(); it != events.end(); ++it) {
      if (it->type == 0) { // ulaz
        left[it->x] += it->cnt;
      } else {
        llint cnt = it->cnt;

        assert(!left.empty());
        while (cnt > 0) {
          int x1 = left.rbegin()->first;
          llint &cap = left.rbegin()->second;
          assert(cap > 0);
          llint d = it->x - x1;

          llint delta = min(cnt, cap);
          
          cap -= delta;
          cnt -= delta;

          cost = ( cost + delta * ((N*d - (d-1)*d/2) % mod) ) % mod;

          if (cap == 0) {
            left.erase(--left.end());
          }
        }
      }
    }
    
    llint sol = orig_cost - cost;
    sol %= mod;
    sol += mod;
    sol %= mod;

    //    printf("orig = %lld cost = %lld\n", orig_cost, cost);
    printf("Case #%d: %lld\n", counter + 1, sol);
    fflush(stdout);
  }

  return (0-0);
}
