#include <algorithm>
#include <cassert>
#include <cstring>
#include <iostream>

using namespace std;

#define LOG(x) cerr << #x << " = " << (x) << "\n"

typedef long long llint;
typedef pair<int,int> pii;

void solve() {
  int n;
  scanf("%d", &n);
  static int a[1010];

  for (int i = 0; i <= n; ++i)
    scanf("%1d", a+i);

  int standing = 0;
  int friends = 0;
  for (int i = 0; i <= n; ++i) {
    if (standing < i) {
      friends += i - standing;
      standing += i - standing;
    }
    standing += a[i];
  }

  printf("%d\n", friends);
}

int main() {
  int t; scanf("%d", &t);
  for (int i = 0; i < t; ++i) {
    printf("Case #%d: ", i+1);
    solve();
  }
  return 0;
}

