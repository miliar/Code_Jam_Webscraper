#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <ctime>

using namespace std;

int n;
int X;
int a[10005];
bool used[10005];

int main() {
  freopen("in", "r", stdin); freopen("out", "w", stdout); freopen("log", "w", stderr);
  int tt; scanf("%d", &tt);
  for (int cc = 1; cc <= tt; ++cc) {
    scanf("%d %d", &n, &X);
    for (int i = 0; i < n; ++i) scanf("%d", a + i);
    sort(a, a + n); reverse(a, a + n);
    for (int i = 0; i < n; ++i) used[i] = false;
    int ans = 0;
    for (int i = 0; i < n; ++i) {
      if (!used[i]) {
        ++ans;
        used[i] = true;
        for (int j = i + 1; j < n; ++j) {
          if (!used[j]) {
            if (a[i] + a[j] <= X) {
              used[j] = true;
              break;
            }
          }
        }
      }
    }
    printf("Case #%d: %d\n", cc, ans);
  }
  return 0;
}