#include<cstdio>
#include<set>

using namespace std;
multiset<int> s;

int main() {
  int n, x, y, ans;
  int tt, uu;
  scanf("%d", &tt);
  for (int t=1; t<=tt; t++) {
    scanf("%d", &n);
    scanf("%d", &x);
    s.clear();
    for (int i = 0; i < n; i++) {
      scanf("%d", &y);
      s.insert(-y);
    }
    ans = 0;
    while (s.size() >= 2) {
      set<int>::iterator u = s.begin();
      uu = -(*u);
      s.erase(u);
      set<int>::iterator v = s.lower_bound(-(x-uu));
      if (v != s.end()) {
        s.erase(v);
      }
      ans++;
    }
    ans += s.size();
    printf("Case #%d: %d\n", t, ans);
  }
}
