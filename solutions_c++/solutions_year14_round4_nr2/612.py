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
    int N;
    std::cin >> N;
    std::vector<int> A(N);
    for(int i = 0; i < N; ++i) {
      std::cin >> A[i];
    }

    std::vector<std::pair<int, int>> v(N);
    for(int i = 0; i < N; ++i) {
      v[i] = {A[i], i};
    }

    std::sort(std::begin(v), std::end(v));

    long long cost = 0;

    int min = 0;
    int max = N;
    int last = -1;
    for(int i = 0; i < N - 1; ++i) {
      int val = INF;
      int pos = 0;

      for(int j = min; j < max; ++j) {
        if(A[j] > last && A[j] < val) {
          val = A[j];
          pos = j;
        }
      }
      if(pos - min < max - 1 - pos) {
        cost += pos - min;
        std::rotate(std::begin(A) + min, std::begin(A) + pos,
                    std::begin(A) + pos + 1);
        ++min;
      } else {
        cost += max - 1 - pos;
        std::rotate(std::begin(A) + pos, std::begin(A) + pos + 1,
                    std::begin(A) + max);
        --max;
      }
    }

    std::cout << "Case #" << test << ": " << cost << std::endl;
  }
}
