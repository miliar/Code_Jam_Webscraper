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

int main()
{
  int T;

  std::cin >> T;
  for(int test = 1; test <= T; ++test) {
    std::vector<int> v(17);

    for(int k = 0; k < 2; ++k) {
      int a;
      std::cin >> a;

      for(int i = 0; i < 4; ++i) {
        for(int j = 0; j < 4; ++j) {
          int x;
          std::cin >> x;
          if(i + 1 == a) {
            ++v[x];
          }
        }
      }
    }

    int ans = -1;
    for(int i = 1; i <= 16; ++i) {
      if(v[i] == 2) {
        if(ans == -1) {
          ans = i;
        } else {
          ans = -2;
          break;
        }
      }
    }
    std::cout << "Case #" << test << ": ";
    switch(ans) {
    case -1:
      std::cout << "Volunteer cheated!";
      break;
    case -2:
      std::cout << "Bad magician!";
      break;
    default:
      std::cout << ans;
    }
    std::cout << std::endl;
  }
}
