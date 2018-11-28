#include <bits/stdc++.h>

using namespace std;

int main() {
//  freopen("in.txt", "rt", stdin);
  freopen("A-large.in", "rt", stdin);
  freopen("A-large.out", "wt", stdout);
  int t; scanf("%d", &t);
  for(int tst = 1; tst <= t; ++tst) {
    int n, x;
    multiset<int> a;
    scanf("%d %d", &n, &x);
    for(int i = 0; i < n; ++i) {
      int s; scanf("%d", &s);
      a.insert(s);
    }
    int ans = 0;
    while(a.size() > 1) {
      int v = *a.rbegin();
      a.erase(a.find(v));
      auto it = a.lower_bound(x - v);
      if(it == a.end()) --it;
      if(v + *it > x && it != a.begin())
        --it;
      if(v + *it <= x && it != a.end())
        a.erase(it);
      ++ans;
    }
    if(a.size()) ++ans;
    printf("Case #%d: %d\n", tst, ans);
  }
  return 0;
}
