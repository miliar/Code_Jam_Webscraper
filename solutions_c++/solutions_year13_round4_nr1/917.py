#include <cstdio>
#include <map>
#include <vector>
#include <set>
#include <algorithm>
#include <utility>

using namespace std;

struct edge {
  int from;
  int to;
  int count;
};

struct event {
  int pos;
  int type;
  long long count;
};

bool operator<(const event& a, const event& b) {
  return a.pos == b.pos ? a.type > b.type : a.pos < b.pos;
}

long long calcDist(long long from, long long to, long long startFare) {
  long long k = to - from;
  return k * (2 * startFare - k + 1) / 2;
}

long long findMax(const vector<event>& v, const vector<int>& revPosMap, int startFare) {
  long long res = 0;
  vector<long long> count(revPosMap.size());
  for (const auto& ev: v) {
//    fprintf(stderr, "pos: %d, type: %d\n", ev.pos, ev.type);
    if (ev.type == 1) {
      count[ev.pos] += ev.count;
    } else {
      long long curCount = ev.count;
      for (int i = count.size() - 1; i >= 0; --i) {
        if (!curCount) {
          break;
        }
        int sub = min(curCount, count[i]);
        res += calcDist(revPosMap[i], revPosMap[ev.pos], startFare) * sub;
        count[i] -= sub;
        curCount -= sub;
      }
    }
  }
  return res;
}

int main() {
  int T;
  scanf("%d", &T);
  for (int t = 0; t < T; ++t) {
    int N, M;
    scanf("%d %d", &N, &M);
    vector<edge> a;
    set<int> pos;
    long long fair = 0;
    for (int i = 0; i < M; ++i) {
      int p, q, r;
      scanf("%d %d %d", &p, &q, &r);
      a.push_back(edge{p, q, r});
      pos.insert(p);
      pos.insert(q);
      fair += calcDist(p, q, N) * r;
    }
    map<int, int> posMap;
    vector<int> posRevMap(pos.size());
    int index = 0;
    for (set<int>::iterator it = pos.begin(); it != pos.end(); ++it) {
      posMap[*it] = index;
      posRevMap[index] = *it;
      ++index;
    }
    vector<event> events;
    for (int i = 0; i < M; ++i) {
      events.push_back(event{posMap[a[i].from], 1, a[i].count});
      events.push_back(event{posMap[a[i].to], -1, a[i].count});
    }
    sort(events.begin(), events.end());
    long long res = findMax(events, posRevMap, N);
//    fprintf(stderr, "%lld\n", fair);
    printf("Case #%d: %lld\n", t + 1, fair - res);
  }
}
