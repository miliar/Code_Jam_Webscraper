#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <cmath>

using namespace std;

void doTest() {
  int n, x;
  scanf("%d%d", &n, &x);
  vector<int> v(n, 0);
  for (int i = 0; i < n; ++i)
    scanf("%d", &v[i]);
  sort(v.rbegin(), v.rend());
  vector<bool> used(n, false);
  int ans = 0;
  for (int i = 0; i < v.size(); ++i) {
    if (!used[i]) {
      ++ans;
      used[i] = true;
      for (int j = i + 1; j < v.size(); ++j) {
        if (!used[j] && v[i] + v[j] <= x) {
          used[j] = true;
          break;
        }
      }
    }
  }
  printf("%d\n", ans);
}

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int T;
  scanf("%d", &T);
  for (int test = 1; test <= T; ++test) {
    printf("Case #%d: ", test);
    doTest();
  }
  return 0;
}