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


int main(int argc, char** argv)
{
  std::cin.tie(0);
  std::ios_base::sync_with_stdio(0);

  int T, n;

  std::string s;

  std::cin >> T;

  for (int t = 1; t <= T; t ++) {
    std::cin >> n >> s;

    int S = 0, r = 0, c = 0;

    for (int i = 0; i <= n; i ++) {
      int a = s[i] - '0';

      if (S >= i) {
        S += a;
      }
      else {
        r  = i - S;
        S += r + a;
        c += r;
      }
    }

    std::cout << "Case #" << t << ": " << c << std::endl;
  }
  
  return 0;
}
