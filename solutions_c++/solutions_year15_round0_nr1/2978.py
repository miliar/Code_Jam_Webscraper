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
using namespace std;
typedef long long ll;

int solve() {
  int S;
  char dt[1100];

  scanf(" %d", &S);
  scanf(" %s", dt);

  int sum = 0;
  int ans = 0;

  for (int i = 0; i < S + 1; ++i) {
    dt[i] -= '0';
    if (i > sum + ans) {
      ans += i - (sum + ans);
    } 
    sum += dt[i];
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
