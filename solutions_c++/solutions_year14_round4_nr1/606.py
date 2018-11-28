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
static const int INF = std::numeric_limits<int>::max();

int main()
{
  int T;
  std::cin >> T;
  for(int test = 1; test <= T; ++test) {
    int N, X;
    std::cin >> N >> X;
    std::vector<int> S(N);
    for(int i = 0; i < N; ++i) {
      std::cin >> S[i];
    }

    std::sort(std::begin(S), std::end(S));

    int i = 0, j = N - 1;

    int ans = 0;
    while(i <= j) {
      if(i == j) {
        ++ans;
        break;
      }
      if(S[i] + S[j] <= X) {
        ++i;
        --j;
        ++ans;
        continue;
      }
      --j;
      ++ans;
    }

    std::cout << "Case #" << test << ": " << ans << std::endl;
  }
}
