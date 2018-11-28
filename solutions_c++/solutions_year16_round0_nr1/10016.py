#include <unordered_set>
#include <stdio.h>
using namespace std;

int solve(int n, unordered_set<int> s) {
  if (n == 0)
    return -1;
  int x, i = 1;
  int ret;
  while(!s.empty()) {
    x = n*i;
    ret = x;
    while (x != 0) {
        s.erase(x%10);
        x = x / 10;
    }
    ++i;
  }
  return ret;
}

int main() {
  unordered_set<int> s;
  int t, n;
  scanf("%d",&t);
  for (int k = 1; k <= t; ++k) {
    for(int i = 0; i < 10; ++i)
      s.insert(i);
    scanf("%d",&n);
    int ans = solve(n, s);
    if (ans == -1) printf("Case #%d: INSOMNIA\n", k);
    else printf("Case #%d: %d\n",k,ans);
  }
  return 0;
}
