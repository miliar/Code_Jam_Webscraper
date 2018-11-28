/* 
  2014.03.26 15:10
  http://codeforces.ru/gym/100289/
*/


#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cmath>
#include <memory.h>
#include <cmath>
#include <string> 
#include <ctime>
#include <sstream>

using namespace std;

// #undef Fdg_Home

char str[50005];
vector<int> w[202];

int f[500000], e[500000];
map<string, int> to;

int add(string s) {
  if (to.count(s)) return to[s];
  int x = to.size();
  return to[s] = x;
}

void solveTest(int CS) {
  printf("Case #%d: ", CS);
  int n;
  scanf("%d\n", &n);
  for (int i = 0; i < n; ++i) {
    gets(str);
    istringstream ss(str);
    string s;
    w[i].clear();
    while (ss >> s) {
      w[i].push_back(add(s));
    }
  }
  memset(e, 0, sizeof(e));
  memset(f, 0, sizeof(f));
  for (auto s : w[0]) e[s]++;
  for (auto s : w[1]) f[s]++;
  int ans = 1e+9;
  for (int mask = 0; mask < (1<<(n - 2)); ++mask) {
    int nmask = ((mask << 1) | 1) << 1;
    for (int i = 2; i < n; ++i) {
      bool what = nmask & (1<<i);
      for (auto s : w[i]) {
        if (what) f[s]++;
        else e[s]++;
      }
    }
    int cur = 0;
    for (int i = 0; i < to.size(); ++i) {
      if (f[i] > 0 && e[i] > 0) ++cur;
    }
    for (int i = 2; i < n; ++i) {
      bool what = nmask & (1<<i);
      for (auto s : w[i]) {
        if (what) f[s]--;
        else e[s]--;
      }
    }
    ans = min(ans, cur);
  }
  printf("%d\n", ans);
}

int main() {
// #ifndef Fdg_Home
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
// #endif
  int T;
  scanf("%d\n", &T);
  for (int test = 1; test <= T; ++test) {
    solveTest(test);
  }
  return 0;
}