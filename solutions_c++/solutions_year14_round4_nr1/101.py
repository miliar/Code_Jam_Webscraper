#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;

int T;
int n, X;
int a[10005];

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("A.out", "w", stdout);
  scanf("%d", &T);
  for (int test = 1; test <= T; ++test) {
    scanf("%d%d", &n, &X);
    for (int i = 0; i < n; ++i) {
      scanf("%d", &a[i]);
    }
    sort(a, a + n);
    reverse(a, a + n);
    vector<int> Q;
    for (int i = 0; i < n; ++i) {
      int sz = Q.size();
      bool flag = false;
      for (int j = 0; j < sz; ++j) {
        if (Q[j] >= a[i]) {
          Q[j] = -1;
          flag = true;
          break;
        }
      }
      if (!flag) {
        Q.push_back(X - a[i]);
      }
    }
    printf("Case #%d: %d\n", test, Q.size());
  }
  return 0;
}
