#include <limits.h>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <limits>
#include <cassert>
#include <string>
#include <vector>
#include <deque>
#include <fstream>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <queue>
#include <iterator>
#include <set>
static const int INF = std::numeric_limits<int>::max();
int K, N;
std::multiset<int> dp[1 << 20];
std::vector<int> path[1 << 20];
int main()
{
  int tests;
  std::cin >> tests;
  for(int test = 1; test <= tests; ++test) {
    for(int i = 0; i < (1 << 20); ++i) {
      dp[i].clear();
      path[i].clear();
    }
    std::cin >> K >> N;
    for(int i = 0; i < K; ++i) {
      int a;
      std::cin >> a;
      dp[0].insert(a);
    }
    std::vector<int> T(N);
    std::vector<std::vector<int> > KEYS(N);
    for(int i = 0; i < N; ++i) {
      int a;
      std::cin >> T[i] >> a;
      for(int j = 0; j < a; ++j) {
        int b;
        std::cin >> b;
        KEYS[i].push_back(b);
      }
    }
    for(int i = 0; i < (1 << N); ++i) {
      if(dp[i].empty()) continue;
      for(int j = 0; j < N; ++j) {
        if((i & (1 << j)) == 0 && dp[i].find(T[j]) != dp[i].end()) {
          int ni = i | (1 << j);
          dp[ni] = dp[i];
          dp[ni].erase(dp[ni].find(T[j]));
          for(int k = 0; k < (int)KEYS[j].size(); ++k) {
            dp[ni].insert(KEYS[j][k]);
          }
          std::vector<int> v = path[i];
          v.push_back(j+1);
          if(path[ni].empty() || path[ni] > v) {
            path[ni] = v;
          }
        }
      }
    }
    std::cout << "Case #" << test << ": ";
    if(path[(1 << N)-1].empty()) {
      std::cout << "IMPOSSIBLE";
    } else {
      std::copy(path[(1 << N)-1].begin(), path[(1 << N)-1].end(),
                std::ostream_iterator<int>(std::cout, " "));
    }
    std::cout << std::endl;
  }
}

