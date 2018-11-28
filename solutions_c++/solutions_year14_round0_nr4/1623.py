#include <cstdio>
#include <cstring>
#include <set>

const int maxn = 1005;

int process1(std::set<double> a[]) {
  std::set<double> bak[] = {a[0], a[1]};
  int res = 0;
  for (std::set<double>::iterator iter = a[1].begin(); iter != a[1].end(); ++ iter) {
    if (a[0].upper_bound(*iter) != a[0].end()) {
      ++ res;
      a[0].erase(a[0].upper_bound(*iter));
    }
  }
  a[0] = bak[0];
  a[1] = bak[1];
  return res;
}

int process2(std::set<double> a[]) {
  int res = 0;
  for (std::set<double>::iterator iter = a[0].begin(); iter != a[0].end(); ++ iter) {
    if (a[1].upper_bound(*iter) != a[1].end()) a[1].erase(a[1].upper_bound(*iter));
    else {
      ++ res;
      a[1].erase(a[1].begin());
    }
  }
  return res;
}

int main() {
  int cas;
  scanf("%d", &cas);
  for (int t = 1; t <= cas; ++ t) {
    std::set<double> a[2];
    int n;
    scanf("%d", &n);
    for (int i = 0; i < 2; ++ i) {
      for (int j = 0; j < n; ++ j) {
        double x;
        scanf("%lf", &x);
        a[i].insert(x);
      }
    }
    printf("Case #%d: %d %d\n", t, process1(a), process2(a));
  }
  return 0;
}
