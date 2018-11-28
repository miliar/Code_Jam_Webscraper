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
#include <unordered_map>
#include <vector>


#define INF 1000000000
#define MOD 1000000007
#define ALL(x) std::begin(x), std::end(x)


const std::map<std::tuple<int, int, int>, std::string> result = {
  {{1, 1, 1}, "GABRIEL"},
  {{1, 1, 2}, "GABRIEL"},
  {{1, 1, 3}, "GABRIEL"},
  {{1, 1, 4}, "GABRIEL"},
  {{1, 2, 2}, "GABRIEL"},
  {{1, 2, 3}, "GABRIEL"},
  {{1, 2, 4}, "GABRIEL"},
  {{1, 3, 3}, "GABRIEL"},
  {{1, 3, 4}, "GABRIEL"},
  {{1, 4, 4}, "GABRIEL"},

  {{2, 1, 1}, "RICHARD"},
  {{2, 1, 2}, "GABRIEL"},
  {{2, 1, 3}, "RICHARD"},
  {{2, 1, 4}, "GABRIEL"},
  {{2, 2, 2}, "GABRIEL"},
  {{2, 2, 3}, "GABRIEL"},
  {{2, 2, 4}, "GABRIEL"},
  {{2, 3, 3}, "RICHARD"},
  {{2, 3, 4}, "GABRIEL"},
  {{2, 4, 4}, "GABRIEL"},

  {{3, 1, 1}, "RICHARD"},
  {{3, 1, 2}, "RICHARD"},
  {{3, 1, 3}, "RICHARD"},
  {{3, 1, 4}, "RICHARD"},
  {{3, 2, 2}, "RICHARD"},
  {{3, 2, 3}, "GABRIEL"},
  {{3, 2, 4}, "RICHARD"},
  {{3, 3, 3}, "GABRIEL"},
  {{3, 3, 4}, "GABRIEL"},
  {{3, 4, 4}, "RICHARD"},

  {{4, 1, 1}, "RICHARD"},
  {{4, 1, 2}, "RICHARD"},
  {{4, 1, 3}, "RICHARD"},
  {{4, 1, 4}, "RICHARD"},
  {{4, 2, 2}, "RICHARD"},
  {{4, 2, 3}, "RICHARD"},
  {{4, 2, 4}, "RICHARD"},
  {{4, 3, 3}, "RICHARD"},
  {{4, 3, 4}, "GABRIEL"},
  {{4, 4, 4}, "GABRIEL"}
};


int main(int argc, char** argv)
{
  std::cin.tie(0);
  std::ios_base::sync_with_stdio(0);

  int T, X, R, C;

  std::cin >> T;

  for (int t = 1; t <= T; t ++) {
    std::cin >> X >> R >> C;

    if (R > C)
      std::swap(R, C);

    std::cout << "Case #" << t << ": " << result.at(std::make_tuple(X, R, C)) << std::endl;
  }
  
  return 0;
}
