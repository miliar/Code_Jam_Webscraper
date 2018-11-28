#define NDEBUG
#include <algorithm>
#include <cstdio>
#include <functional>
#include <iostream>
#include <set>
using namespace std;

#define repeat(n) for (int repc = (n); repc > 0; --repc)

int solve1() {
  int n, cap;
  cin >> n >> cap;
  std::multiset<int, greater<int> > sizes;
  repeat (n) {
    int x;
    cin >> x;
    sizes.insert(x);
  }

  int out = 0;
  for (; !sizes.empty(); ++out) {
    int x = *sizes.begin(); sizes.erase(sizes.begin());
    auto it = sizes.lower_bound(cap - x);
    if (it != sizes.end()) {
      sizes.erase(it);
    }
  }
  return out;
}

int main() {
  ios_base::sync_with_stdio(0);

  int T;
  cin >> T;
  for (int tt=1; tt<=T; ++tt) {
    printf("Case #%d: %d\n", tt, solve1());
  }
}
