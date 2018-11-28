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
    double C, F, X;

    std::cin >> C >> F >> X;

    double cookies = 0.0;
    double t = 0.0;
    double rate = 2.0;

    double best_eta = INF;
    while(1) {
      best_eta = std::min(best_eta, (X - cookies) / rate + t);

      auto dt = (C - cookies) / rate;

      cookies = 0.0;
      rate += F;
      t += dt;

      if(best_eta < t) {
        break;
      }
    }

    std::cout << "Case #" << test << ": "
              << std::fixed << std::setprecision(9) << best_eta << std::endl;
  }
}
