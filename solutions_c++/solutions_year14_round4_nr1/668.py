#include <bits/stdc++.h>
using namespace std;
template<typename T> inline void checkMin(T &a, T b) { if(b<a) a=b; }
template<typename T> inline void checkMax(T &a, T b) { if(a<b) a=b; }
#define X first
#define Y second
#define MP make_pair
#define PB push_back
#define SZ(c) int((c).size())
#define ALL(c) (c).begin(),(c).end()
#define REP(i,n) for (int i=0;i<int(n);++i)
typedef long long lint;
typedef vector<int> VI;
typedef pair<int, int> PII;

int main() {
  int n_case;
  scanf("%d", &n_case);
  for (int index = 1; index <= n_case; ++index) {
    int n, x, a;
    scanf("%d%d", &n, &x);
    multiset<int> is;
    REP (i, n) {
      scanf("%d", &a);
      is.insert(a);
    }
    int ans = 0;
    for (auto iter = is.begin(); iter != is.end();) {
      ++ans;
      int a = *iter;
      iter = is.erase(iter);
      auto jter = is.upper_bound(x - a);
      if (jter != is.begin()) {
        --jter;
        if (iter == jter) iter = is.erase(jter);
        else is.erase(jter);
      }
    }
    printf("Case #%d: %d\n", index, ans);
  }
  return 0;
}
