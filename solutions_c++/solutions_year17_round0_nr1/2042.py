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
  string s;
  int ans = 0;
  int K;
  cin >> s >> K;
  
  for (int i = 0; i <= s.size() - K; i++) {
    if (s[i] == '-') {
      ans++;
      for (int j = 0; j < K; ++j) {
	if (s[i + j] == '-') {
	  s[i + j] = '+';
	} else {
	  s[i + j] = '-';
	}
      }
    }
  }
  for (int i = s.size() - K + 1; i < s.size(); i++) {
    if (s[i] == '-') {
      return -1;
    }
  }
  return ans;
}

int main() {

  int T;
  scanf(" %d", &T);

  for (int ii = 0; ii < T; ii++) {
    printf("Case #%d: ", ii + 1);
    int ans = solve();
    if (ans < 0) {
      printf("IMPOSSIBLE\n");
    } else {
      printf("%d\n", ans);
    }
  }
}
