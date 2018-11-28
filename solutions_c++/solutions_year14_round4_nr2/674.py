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

const int INF = ~0U >> 2;

int work() {
  int n;
  scanf("%d", &n);

  VI a;
  a.resize(n);
  REP (i, n) {
    scanf("%d", &a[i]);
  }

  int ans = 0;
  REP (i, n - 1) {
    int k = 0;
    REP (j, SZ(a)) {
      if (a[j] < a[k]) {
        k = j;
      }
    }
    ans += min(SZ(a) - 1 - k, k);
    a.erase(a.begin() + k);
  }
  return ans;
}

int main() {
  int n_case;
  scanf("%d", &n_case);
  for (int index = 1; index <= n_case; ++index) {
    printf("Case #%d: %d\n", index, work());
  }
  return 0;
}
