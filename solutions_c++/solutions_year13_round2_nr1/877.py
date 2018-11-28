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
#include <map>
#include <utility>
static const int INF = std::numeric_limits<int>::max();
int A, N;
std::vector<int> v;
std::map<std::pair<long long, int>, int> memo;
long long solve(long long a, int x)
{
  if(x == N) {
    return 0;
  }
  if(memo.count(std::make_pair(a, x))) {
    return memo[std::make_pair(a, x)];
  }
  int res = 0;
  if(a > v[x]) {
    res = solve(a+v[x], x+1);
  } else if(a > 1) {
    res = std::min(solve(a+a-1, x) + 1, solve(a, x+1) + 1);
  } else {
    res = solve(a, x+1) + 1;
  }
  memo[std::make_pair(a, x)] = res;
  return res;
}
int main()
{
  int tests;
  std::cin >> tests;
  for(int test = 1; test <= tests; ++test) {
    std::cin >> A >> N;
    v = std::vector<int>(N);
    for(int i = 0; i < N; ++i) {
      std::cin >> v[i];
    }
    std::sort(v.begin(), v.end());
    memo.clear();
    std::cout << "Case #" << test << ": " << solve(A, 0) << std::endl;
  }
}

