#include <algorithm>
#include <cassert>
#include <cstdio>
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


#define INF 1000000002486618624LL
#define MOD 1000000007
#define ALL(x) std::begin(x), std::end(x)


int main(int argc, char** argv)
{
  std::cin.tie(0);
  std::ios_base::sync_with_stdio(0);

  int T;

  std::cin >> T;

  for (int t = 1; t <= T; t ++) {
    std::string s, ss;

    std::cin >> s;

    for (const auto& c : s)
      if (ss.empty()) {
        ss.push_back(c);
      }
      else if (c < ss.front()) {
        ss.push_back(c);
      }
      else {
        ss.insert(std::begin(ss), c);
      }

    std::cout << "Case #" << t << ": " << ss << std::endl;
  }
  
  return 0;
}
