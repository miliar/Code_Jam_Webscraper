#define NDEBUG
#include <algorithm>
#include <cassert>
#include <climits>
#include <cstdio>
#include <iostream>
#include <map>
#include <utility>
#include <vector>
using namespace std;

template<typename T, typename U> inline void makemin(T &res, const U &x) {
  if (x < res) {
    res = x;
  }
}
template<typename T, typename U> inline void makemax(T &res, const U &x) {
  if (x > res) {
    res = x;
  }
}

int solve1() {
  int N, K;
  cin >> N >> K;
  vector<int> S(N-K+1);
  for (int& s : S) {
    cin >> s;
  }
  vector<int> D;
  for (int i=0; i+1<(int)S.size(); ++i) {
    D.push_back(S[i+1] - S[i]);
  }

  vector<pair<int, int> > ranges;
  for (int seed=0; seed<K; ++seed) {
    int d = 0;
    int a = 0, b = 0;
    for (int i=seed+K; i<N; i+=K) {
      d += D[i-K];
      makemin(a, d);
      makemax(b, d);
    }
    ranges.push_back(make_pair(a, b));
  }
  // debug(ranges);

  int ans = INT_MAX;
  for (int first=-1000000; first<=1000000; ++first) {
  // for (const int first : candidates) {
    map<int, int> mapp;

    int sum = S[0];
    for (pair<int, int> r : ranges) {
      int d = first - r.first;
      r.first += d;
      r.second += d;
      sum -= d;
      ++mapp[r.second];
    }

    if (sum < 0) {
      continue;
    }

    // debug(first);
    // debug(sum);

    while (sum > 0) {
      auto it = mapp.begin();
      // debug(*it);
      // debug(sum);
      int a = it->first;
      int delta = max(1, sum / it->second);
      if (mapp.size() > 1) {
        auto jt = mapp.begin();
        ++jt;
        makemin(delta, jt->first - a);
      }
      assert(delta > 0);
      if (sum >= delta * it->second) {
        mapp[a + delta] += it->second;
        sum -= delta * it->second;
        mapp.erase(it);
      } else {
        assert(delta == 1);
        mapp[a + delta] += sum;
        mapp[a] -= sum;
        sum = 0;
      }
    }

    int high_b = mapp.rbegin()->first;
    makemin(ans, high_b - first);
  }
  // assert(ans != INT_MAX);
  return ans;
}

int main() {
  ios_base::sync_with_stdio(0);

  int T;
  cin >> T;
  for (int tt=1; tt<=T; ++tt) {
    printf("Case #%d: %d\n", tt, solve1());
    fflush(stdout);
  }
}
