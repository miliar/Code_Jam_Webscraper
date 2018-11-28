#include <cstdio>
#include <cassert>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <utility>
#include <sstream>
#include <climits>
using namespace std;
typedef long long ll;

int solve() {
  int D;
  int dt[1000];

  scanf(" %d", &D);
  
  for (int i = 0; i < D; ++i) {
    scanf(" %d", &dt[i]);
  }

  int ans = INT_MAX;
  
  for (int i = 1; i <= 1000; ++i) {
    int cnt = i;
    for (int j = 0; j < D; ++j) {
      cnt += dt[j] / i;
      if (dt[j] % i == 0) cnt--;
    }
    ans = min(ans, cnt);
  }
  return ans;
}

int main() {

  int T;
  scanf(" %d", &T);
  
  for (int ii = 0; ii < T; ii++) {
    printf("Case #%d: %d\n", ii + 1, solve());
  }
}
