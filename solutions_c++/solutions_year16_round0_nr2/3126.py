#include <cstdio>
#include <cmath>
#include <cstring>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <map>

int T;

int solve(std::string str) {
  str.erase(std::unique(str.begin(), str.end()), str.end());
  int res = 0;
  for(int i = 0; i < (int)str.size(); ++i) {
    if( str[i] == '-' ) res += 2;
  }
  assert( str.size() != 0 );
  if( str[0] == '-' ) {
    res -= 1;
  }
  return res;
}

int main() {
  std::string str;
  scanf("%d", &T);
  for(int i = 1; i <= T; ++i) {
    std::cin >> str;
    int res = solve(str);
    printf("Case #%d: %d\n", i, res);
  }
  
  
  return 0;
}
