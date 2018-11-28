#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>
#include <cassert>

using namespace std;

#define out(x) cerr << #x"=" << x << endl
#define INF 0xfffffff
#define N 1010

int cnt[N];
int sum[N];

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("e.out", "w", stdout);
  int t;
  scanf("%d", &t);
  for (int id = 1; id <= t; ++id) {
    char str[N];
    int n;
    scanf("%d", &n);
    scanf("%s", str);
    for (int i = 0; i <= n; ++i) {
      cnt[i] = str[i]-'0';
    }
    sum[0] = cnt[0];
    for (int i = 1; i <= n; ++i) {
      sum[i] = sum[i-1] + cnt[i];
    }
//    for (int i = 1; i <= n; ++i) {
//      printf("%d ", sum[i]);
//    }
//    printf("\n");
    int ans = 0;
    for (int i = 1; i <= n; ++i) {
      int tmp = max(i-sum[i-1], 0);
      ans = max(tmp, ans);
//      printf("%d\n", tmp);
    }
    printf("Case #%d: ", id);
    printf("%d\n", ans);
  }
  return 0;
}
