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
#include <utility>
static const int INF = std::numeric_limits<int>::max();
bool iscons(char c)
{
  const char s[] = "aiueo";
  return strchr(s, c) == 0;
}
int main()
{
  int tests;
  std::cin >> tests;
  for(int test = 1; test <= tests; ++test) {
    std::string S;
    int N;
    std::cin >> S >> N;
    long long res = 0;
    int n = 0;
    int start = 0;
    for(int i = 0; i < (int)S.size(); ++i) {
      if(iscons(S[i])) {
        ++n;
        if(n == N) {
          // std::cout << "i=" << i << std::endl;
          // std::cout << "end=" << (i+1-N) << std::endl;
          res += (long long)((i+1-N)-start+1)*(S.size()-i);
          --n;
          start = i+2-N;
        }
      } else {
        n = 0;
      }
    }
    std::cout << "Case #" << test << ": " << res << std::endl;
  }
}

