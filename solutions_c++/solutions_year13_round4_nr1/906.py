#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <algorithm>
#include <assert.h>
using namespace std;

void print_128(__uint128_t s) {
  if (s == 0) printf("0");
  else {
    string r;
    while (s > 0) {
      string g(1, s % 10 + '0');
      r = g + r;
      s /= 10;
    }
    printf("%s", r.c_str());
  }
}

long long n;
__uint128_t get_cost(long long d) {
  return (n * 2 - d + 1) * d / 2;
}
int main() {
  int tc;
  cin >> tc;
  for (int cas = 1; cas <= tc; ++cas) {
    int m;
    cin >> n >> m;
    __uint128_t ori_cost = 0;
    map<int, long long> mg;
    for (int i = 0; i < m; ++i) {
      int s, t, p;
      cin >> s >> t >> p;
      ori_cost += get_cost(t - s) * p;
      if (mg.find(s) == mg.end()) mg[s] = 0;
      if (mg.find(t) == mg.end()) mg[t] = 0;
      mg[s] += p;
      mg[t] -= p;
    }
    vector<pair<int, long long> > gl;
    for (map<int, long long>::const_iterator it = mg.begin(); it != mg.end(); ++it) {
      gl.push_back(*it);
    }
    __uint128_t cost = 0;
    for (int en = 0; en < gl.size(); ++en) {
      int p = en - 1;
      while (gl[en].second < 0) {
        while (gl[p].second <= 0) --p;
        long long g = (gl[p].second + gl[en].second > 0 ? -gl[en].second : gl[p].second);
        long long d = gl[en].first - gl[p].first;
        cost += get_cost(d) * g;
        gl[en].second += g;
        gl[p].second -= g;
        // cerr << d << " " << g << endl;
      }
    } // for
    printf("Case #%d: ", cas);
    print_128(ori_cost - cost);
    printf("\n");
  }
}
