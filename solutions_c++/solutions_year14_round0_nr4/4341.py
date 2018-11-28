#define PRETEST
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <math.h>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <iomanip>
#include <sstream>
using namespace std;

#define INF 0x4f4f4f4f
#define FILL(a,b) memset(a,b,sizeof(a))
#define SQR(a) ((a) * (a))

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<string, int> psi;
typedef map<string, int> msi;
typedef map<int, int> mii;

int main(int argc, char *argv[]) {
#ifdef PRETEST
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
#endif
  vector<double> a;
  vector<double> b;
  set<double> sb;
  int T;
  scanf("%d", &T);
  for (int z = 1; z <= T; ++z) {
    int n;
    scanf("%d", &n);
    a.clear();
    b.clear();
    sb.clear();
    for (int i = 0; i < n; ++i) {
      double x;
      scanf("%lf", &x);
      a.push_back(x);
    }
    for (int i = 0; i < n; ++i) {
      double x;
      scanf("%lf", &x);
      b.push_back(x);
      sb.insert(x);
    }
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    int l = 0, ra = n - 1, rb = n - 1;
    int ans = 0;
    while (l <= ra) {
      if (a[ra] > b[rb]) {
        ra--;
        rb--;
        ans++;
      } else {
        l++;
        rb--;
      }
    }
    printf("Case #%d: ", z);
    printf("%d ", ans);
    ans = 0;
    for (int i = 0; i < n; ++i) {
      set<double>::iterator it = sb.lower_bound(a[i]);
      if (it != sb.end()) {
        sb.erase(it);
      } else {
        ++ans;
        sb.erase(sb.begin());
      }
    }
    printf("%d\n", ans);
  }
  
  return 0;
}
