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
using std::cin;
using std::cout;

int WarGame(const std::vector<double>& Naomi, const std::vector<double>& Ken) {
  std::set<double> K(Ken.begin(), Ken.end());

  int wins_count = 0;
  for (double value : Naomi) {
    if (value > *K.rbegin()) {
      ++wins_count;
      K.erase(K.begin());
    } else {
      K.erase(K.lower_bound(value));
    }
  }

  return wins_count;
}

int DeceitfulWarGame(std::vector<double> Naomi,
                     const std::vector<double>& Ken) {
  std::sort(Naomi.begin(), Naomi.end());
  std::set<double> K(Ken.begin(), Ken.end());

  int wins_count = 0;
  for (double value : Naomi) {
    if (value < *K.begin()) {
      K.erase(*K.rbegin());
    } else {
      ++wins_count;
      K.erase(K.begin());
    }
  }
  return wins_count;
}


int main() {
  std::ios_base::sync_with_stdio(false);
//  std::freopen("/Users/kuznetsovs/Hobby/Console/Console/1.txt", "rb", stdin);
  std::freopen("/Users/kuznetsovs/Hobby/Console/Console/D-large.in", "rb", stdin);
  std::freopen("/Users/kuznetsovs/Hobby/Console/Console/D-large.out", "wb", stdout);
  int T;
  cin >> T;

  for (int tc = 0; tc < T; ++tc) {
    int N;
    cin >> N;

    std::vector<double> Naomi(N);
    for (double& v : Naomi) {
      cin >> v;
    }
    std::vector<double> Ken(N);
    for (double& v : Ken) {
      cin >> v;
    }

    cout << "Case #" << tc + 1 << ": " << DeceitfulWarGame(Naomi, Ken) << ' ' << WarGame(Naomi, Ken) << '\n';
  }
  return 0;
}
