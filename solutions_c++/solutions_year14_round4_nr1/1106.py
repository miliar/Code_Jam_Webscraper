#include <algorithm>
#include <functional>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <iostream>
#include <limits>
#include <map>
#include <queue>
#include <set>
#include <list>
#include <vector>
#include <sstream>
#include <numeric>
using std::cin;
using std::cout;


int main() {
  std::ios_base::sync_with_stdio(false);
//  std::freopen("/Users/kuznetsovs/Hobby/Console/Console/1.txt", "rb", stdin);
  std::freopen("/Users/kuznetsovs/Hobby/Console/Console/A-large.in", "rb", stdin);
  std::freopen("/Users/kuznetsovs/Hobby/Console/Console/A-large.out", "wb", stdout);

  int T;
  cin >> T;
  for (int tc = 0; tc < T; ++tc) {
    int N, X;
    cin >> N >> X;

    std::multiset<int> S;
    for (int i = 0; i < N; ++i) {
      int v;
      cin >> v;
      S.insert(v);
    }

    int answer = 0;
    while (!S.empty()) {
      ++answer;

      int value = *S.rbegin();
      S.erase(S.find(value));

      if (S.empty()) {
        break;
      }

      int remaining = X - value;

      std::multiset<int>::iterator it = S.upper_bound(remaining);
      if (it != S.begin()) {
        --it;
        assert(*it <= remaining);
        S.erase(it);
      }
    }

    cout << "Case #" << tc + 1 << ": " << answer << '\n';
  }
  return 0;
}
