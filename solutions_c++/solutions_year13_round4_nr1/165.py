#include <algorithm>
#include <cassert>
#include <iostream>
#include <map>
#include <set>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

typedef long long int64;
#define foreach(i,c) for ( typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i )
#define ALL(x) (x).begin(), (x).end()

const int MOD = 1000002013;

int64 sumto(int64 x) {
  assert(x >= 0);
  return x * (x+1) / 2;
}

int64 calccost(int64 N, int64 o, int64 e, int64 p) {
  assert(o <= e);
  if (o == e) {
    return 0;
  }
  return ((e-o) * N - sumto(e-o-1)) % MOD * p % MOD;
}

enum EventType { ON=0, OFF=1 };

struct Event {
  EventType type;
  int where;
  int p;
  friend bool operator<(const Event &e1, const Event &e2) {
    if (e1.where != e2.where) return e1.where < e2.where;
    if (e1.type != e2.type) return e1.type < e2.type;
    return false;
  }
};

struct Ticket {
  int origin;
  int count;
};

int64 solve1() {
  int64 expected = 0;
  vector<Event> events;

  int N, M;
  cin >> N >> M;
  for (int i=0; i<M; ++i) {
    int o, e, p;
    cin >> o >> e >> p;
    events.push_back((Event){ON, o, p});
    events.push_back((Event){OFF, e, p});
    expected += calccost(N, o, e, p);
    expected %= MOD;
  }
  sort(ALL(events));

  int64 actual = 0;
  stack<Ticket> tickets;
  foreach (it, events) {
    const Event &e = *it;
    if (e.type == ON) {
      tickets.push((Ticket){e.where, e.p});
    } else {
      int ppl = e.p;
      while (ppl > 0) {
        assert(!tickets.empty());
        int grab = min(tickets.top().count, ppl);
        actual += calccost(N, tickets.top().origin, e.where, grab);
        actual %= MOD;
        
        ppl -= grab;
        tickets.top().count -= grab;
        if (tickets.top().count == 0) {
          tickets.pop();
        }
      }
    }
  }
  
  return ((expected - actual) % MOD + MOD) % MOD;
}

int main() {
  cin.sync_with_stdio(0);

  int T;
  cin >> T;
  for (int tt=1; tt<=T; ++tt) {
    cout << "Case #" << tt << ": " << solve1() << '\n';
  }
  
  return 0;
}
