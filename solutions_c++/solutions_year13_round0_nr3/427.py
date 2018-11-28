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
bool check(long long n)
{
  char v[256];
  int size = 0;
  while(n) {
    v[size] = n%10;
    n /= 10;
    ++size;
  }
  for(int i = 0, j = size-1; i < j; ++i, --j) {
    if(v[i] != v[j]) {
      return false;
    }
  }
  return true;
}
int main()
{
  int tests;
  std::cin >> tests;

  std::vector<std::pair<long long, int> > v(1);
  for(int i = 1; i <= 10000000; ++i) {
    if(check(i) && check((long long)i*i)) {
      v.push_back(std::make_pair((long long)i*i, v.back().second+1));
    }
  }

  for(int test = 1; test <= tests; ++test) {
    long long A, B;
    std::cin >> A >> B;
    std::vector<std::pair<long long, int> >::iterator i =
      std::lower_bound(v.begin(), v.end(), std::make_pair(A, 0));
    std::vector<std::pair<long long, int> >::iterator j =
      std::lower_bound(v.begin(), v.end(), std::make_pair(B, 0));
    if(i == v.end() || (*i).first >= A) {
      --i;
    }
    if(j == v.end() || (*j).first > B) {
      --j;
    }
    std::cout << "Case #" << test << ": "
              << ((*j).second - (*i).second) << std::endl;
  }
}

