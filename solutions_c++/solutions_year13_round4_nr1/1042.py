#include <cassert>
#include <iostream>
#include <map>

using namespace std;

struct Segment {
  int o, e, p;
  Segment(int o, int e, int p) : o(o), e(e), p(p) {};
  bool operator < (const Segment &rhv) const {
    return o > rhv.o || o == rhv.o && e > rhv.e;
  }
};

int main() {

  int T;
  int N, M;
  int o, e, p;
  long long res;
  cin >> T;
  for (int CASE = 1; CASE <= T; CASE++) {
    cin >> N >> M;
    res = 0;
    map<pair<int, int>, int> segs;
    for (int i = 0; i < M; i++) {
      cin >> o >> e >> p;
      res -= (e - o) * (e - o - 1ll) / 2 * p;
      res %= 1000002013ll;
      segs[make_pair(o, e)] += p;
    }
    for (auto it = segs.begin(); it != segs.end(); it++) {
      for (auto it2 = it; ++it2 != segs.end();) {
        if (it->second > 0) {
          if (it->first.second >= it2->first.first) {
            if (it->first.first < it2->first.first && it2->first.second > it->first.second) {
              int mp = min(it->second, it2->second);
              // cout << "[" << it->first.first << "," << it->first.second << "] ~ [" << it2->first.first << "," << it2->first.second << "] = " << mp << endl;
              assert(mp >= 0);
              if (mp > 0) {
                segs[make_pair(it->first.first, it2->first.second)] += mp;
                segs[make_pair(it2->first.first, it->first.second)] += mp;
                it->second -= mp;
                it2->second -= mp;
              }
            }
          } else {
            break;
          }
        } else {
          break;
        }
      }
    }
    for (auto it = segs.begin(); it != segs.end(); it++) if (it->second) {
      // cout << "[" << it->first.first << "," << it->first.second << "] = " << it->second << endl;
      res += (it->first.second - it->first.first) * (it->first.second - it->first.first - 1ll) / 2 * it->second;
      res %= 1000002013ll;
    }
    cout << "Case #" << CASE << ": " << res << endl;
  }

}