#include <algorithm>
#include <cassert>
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
#define MOD 1000000007
#define ALL(x) std::begin(x), std::end(x)


int main(int argc, char** argv)
{
  std::cin.tie(0);
  std::ios_base::sync_with_stdio(0);

  int T, K, x;

  std::cin >> T;

  for (int t = 1; t <= T; t ++) {
    std::vector<int> a, b, c;

    std::cin >> K;

    for (int i = 0; i < 4; i ++)
      for (int j = 0; j < 4; j ++) {
        std::cin >> x;

        if (i == K - 1)
          a.push_back(x);
      }
    
    std::cin >> K;

    for (int i = 0; i < 4; i ++)
      for (int j = 0; j < 4; j ++) {
        std::cin >> x;

        if (i == K - 1)
          b.push_back(x);
      }

    std::sort(ALL(a));

    std::sort(ALL(b));

    std::set_intersection(ALL(a), ALL(b), std::back_inserter(c));

    int size = c.size();

    std::cout << "Case #" << t << ": ";
    
    if (size == 0) {
      std::cout << "Volunteer cheated!";
    }
    else if (size == 1) {
      std::cout << c.front();
    }
    else {
      std::cout << "Bad magician!";
    }
    std::cout << std::endl;
  }

  return 0;
}
