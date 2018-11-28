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
int N, M;
int a[100][100];
bool check()
{
  std::vector<int> hmax(N), vmax(M);
  for(int i = 0; i < N; ++i) {
    for(int j = 0; j < M; ++j) {
      hmax[i] = std::max(hmax[i], a[i][j]);
      vmax[j] = std::max(vmax[j], a[i][j]);
    }
  }
  for(int i = 0; i < N; ++i) {
    for(int j = 0; j < M; ++j) {
      if(hmax[i] > a[i][j] && vmax[j] > a[i][j]) {
        return false;
      }
    }
  }
  return true;
}
int main()
{
  int tests;
  std::cin >> tests;
  for(int test = 1; test <= tests; ++test) {
    memset(a, 0, sizeof(a));
    std::cin >> N >> M;
    for(int i = 0; i < N; ++i) {
      for(int j = 0; j < M; ++j) {
        std::cin >> a[i][j];
      }
    }
    std::cout << "Case #" << test << ": "
              << (check() ? "YES" : "NO") << std::endl;
  }
}

