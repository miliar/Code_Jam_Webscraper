#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <sstream>
#include <vector>


#define INF 1000000000
#define EPS 1e-8
#define MOD 1000000007
#define ALL(x) std::begin(x), std::end(x)


int main(int argc, char** argv)
{
  std::cin.tie(0);
  std::ios_base::sync_with_stdio(0);

  int T;
  
  std::cin >> T;

  for (int t = 1; t <= T; t ++) {
    double C, F, X;

    std::cin >> C >> F >> X;

    double f = 2, l = 0, u = C / 2, p, r, rm = 1e+9;

    int c = 0;

    while (1) {
      p = X / f;
      
      r = l + p;

      if (fabs(r - rm) < EPS)
        break;

      rm = std::min(r, rm);

      if (r > rm)
        break;

      f += F;
      l  = u;
      u += C / f;
    }
    
    std::cout << "Case #" << t << ": " << std::fixed << std::setprecision(9) << rm << std::endl;
  }

  return 0;
}
