#include <cstdio>
#include <cstring>
#include <set>

using namespace std;

int main()
{
  int T, t = 1;
  int n, i, p1, p2;
  double a, b;
  set<double> oa, ob, sa, sb;
  set<double>::iterator itr;

  for (scanf("%d", &T); T; --T) {
    scanf("%d", &n);
    oa.clear(); ob.clear();
    for (i = 0; i < n; ++i) {
      scanf("%lf", &a);
      oa.insert(a);
    }
    for (i = 0; i < n; ++i) {
      scanf("%lf", &b);
      ob.insert(b);
    }

    sa = oa; sb = ob;
    p1 = 0;
    while(!sa.empty()) {
      a = *(sa.begin());
      itr = sb.upper_bound(a);
      if (itr == sb.end()) {
        ++p1;
        itr = sb.begin();
      }
      sa.erase(a);
      sb.erase(itr);
    }

    sa = oa; sb = ob;
    p2 = 0;
    while(!sa.empty()) {
      a = *(sa.begin());
      b = *(sb.begin());
      if (a < b) {
        sb.erase(*sb.rbegin());
      }
      else {
        ++p2;
        sb.erase(sb.begin());
      }
      sa.erase(a);
    }

    printf("Case #%d: %d %d\n", t++, p2, p1);
  }

  return 0;
}
