#include <algorithm>
#include <cassert>
#include <cstring>
#include <iostream>
#include <set>

using namespace std;

#define LOG(x) cerr << #x << " = " << (x) << "\n"

typedef long long llint;
typedef pair<int,int> pii;
const int MAXP = (int)1e9 + 10;

void solve() {
  int n;
  scanf("%d", &n);
  static int a[1010];

  for (int i = 0; i < n; ++i)
    scanf("%d", a+i);

  int ans = MAXP;
  for (int max_dio = 1; max_dio <= 1000; ++max_dio) {
    int x = 0;
    for (int i = 0; i < n; ++i) {
      x += (a[i] - 1) / max_dio;
    }
    ans = min(ans, x + max_dio);
  }

  printf("%d\n", ans);
}

int main() {
  int t; scanf("%d", &t);
  for (int i = 0; i < t; ++i) {
    printf("Case #%d: ", i+1);
    solve();
  }
  return 0;
}

