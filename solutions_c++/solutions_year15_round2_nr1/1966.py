#include <string>
#include <vector>
#include <cstring>
#include <cmath>
#include <utility>
#include <algorithm>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <list>
#include <iomanip>
#include <ctime>
#include <cassert>
#include <stack>
#include <unordered_map>
#include <unordered_set>

#define what_is(x) cout << #x << " is " << x << endl;

using namespace std;

typedef long long ll;

const int maxv = 1e6 + 10;

int dp[maxv], pre[maxv], both[maxv];

int reverse_num(int n) {
  int ans = 0, cur = 0;
  while (n > 0) {
    ans = ans * 10 + n % 10;
    n /= 10;
    cur++;
  }
  return ans;
}

int main () {
  std::ios::sync_with_stdio(false);
  for (int i = 0; i <= 20; i++) {
    dp[i] = i;
    pre[i] = i - 1;
  }
  for (int i = 21; i < maxv; i++) {
    int rev = reverse_num(i);
    if (i % 10 == 0 || rev >= i) {
      dp[i] = dp[i - 1] + 1;
      pre[i] = i - 1;
    }
    else {
      if (dp[i - 1] < dp[rev]) {
	pre[i] = i - 1;
      }
      else if (dp[i - 1] > dp[rev]){
	pre[i] = rev;
      }
      else {
	pre[i] = i - 1;
	both[i] = 1;
      }
      dp[i] = min(dp[i - 1] + 1, dp[rev] + 1);
    }
  }
  int t;
  cin >> t;
  for (int i = 0; i < t; i++) {
    int n;
    cin >> n;
    cout << "Case #" << i + 1 << ": " << dp[n] << endl;
  }
  return 0;
}
