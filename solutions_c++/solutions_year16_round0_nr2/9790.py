#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <iterator>
#define FOR(i,a,n) for(int i = (a); i < (int)(n); ++i)
#define foreach(itr,c) for(decltype((c).begin()) itr=(c).begin(); itr != (c).end(); itr++)
#define MP(a,b) make_pair(a,b)

using namespace std;

//typedef __int64 ll;
//typedef unsigned __int64 ull;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> PII;

char s[150];

int n;

int solve() {
  int i = 0;
  int ans = 0;
  if(s[0] == '-') ans = 1;
  while(i < n && s[i] == '-') ++i;
  while(i < n) {
    while(i < n && s[i] == '+') ++i;
    if(i == n) break;
    ans += 2;
    while(i < n && s[i] == '-') ++i;
  }
  return ans;
}

int main() {
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);
  int t;
  cin >> t;
  FOR(tt, 1, t + 1) {
    cin >> s;
    n = strlen(s);
    int ans = solve();
    printf("Case #%d: %d\n", tt, ans);
  }
  return 0;
}

/*
int dp0[120][120], dp1[120][120];
char s[150];

int n;

int solve() {
  FOR(i, 0, n) if(s[i] == '+') s[i] = 0; else s[i] = 1;
  memset(dp0, -1, sizeof(dp0));
  memset(dp1, -1, sizeof(dp1));
  FOR(i, 0, n) dp0[i][i] = dp1[i][i] = s[i];
  FOR(k, 1, n) {
    FOR(i, 0, n - k) {
      dp[i][i+k] = dp[]
      FOR(j, i, i + k) {
        dp0[i][]
      }
    }
  }
}

int main() {
  int t;
  scanf("%d", &t);
  FOR(tt, 1, t + 1) {
    scanf("%s", s);
    int ans = solve();
    printf("Caee #%d: %d\n", ans);
  }
  return 0;
}
*/
