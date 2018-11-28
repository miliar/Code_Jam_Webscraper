#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

const long long P = 1000002013LL;

const long long N_MAX = 2000000000LL;
const int M_MAX = 5000;

long long old_save;
long long N;
int M;

struct Event {
  Event () : loc(-1), num(-1) {}
  Event (long long loc_, long long num_) : loc(loc_), num(num_) {}

  long long loc;
  long long num;

  bool operator<(const Event & other) const {
    if (loc != other.loc)
      return loc < other.loc;
    return num > other.num;
  }
};

Event events[2 * M_MAX];


long long savings(long long dist) {
  return dist * (dist - 1) / 2;
}

void init() {
  old_save = 0LL;

  cin >> N >> M;
  for (int i = 0; i < M; i++) {
    long long o, e, p;
    cin >> o >> e >> p;

    events[2 * i] = Event(o, p);
    events[2 * i + 1] = Event(e, -p);

    old_save += (p * (savings(e - o) % P));
    old_save %= P;
  }
}

void solve_case(int t) {
  init();
  sort(events, events + 2 * M);

  vector<Event> cur_stack;
  long long new_save = 0LL;

  for (int i = 0; i < 2 * M; i++) {
    Event evt = events[i];
    long long p = evt.num;
    long long cur_loc = evt.loc;

    assert(p != 0);

    if (p > 0) {
      cur_stack.push_back(evt);
      continue;
    }

    while (p < 0) {
      assert(cur_stack.size() > 0);
      Event & last = cur_stack.back();
      long long amt = last.num, last_loc = last.loc;

      if ((-p) >= amt) {
        cur_stack.pop_back();
      } else {
        amt = -p;
        last.num -= amt;
      }

      p += amt;
      new_save += amt * (savings(cur_loc - last_loc) % P);
      new_save %= P;
    }
  }

  assert(cur_stack.size() == 0);
  long long answer = (new_save - old_save + P) % P;
  cout << "Case #" << t << ": " << answer << "\n";
}

int main() {
  int T;
  cin >> T;

  for (int i = 0; i < T; i++) {
    solve_case(i + 1);
  }

  return 0;
}
