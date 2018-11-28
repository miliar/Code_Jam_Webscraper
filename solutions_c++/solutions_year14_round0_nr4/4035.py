#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

#define REP(i, n) for(int i = 0; i < n; i++)
#define INF 0x3f3f3f3f
typedef long long int int64;

int n;
double v[1020];
double w[1020];
bool used[1020];

int calcula2() {
  memset(used, false, sizeof(used));
  int res = 0;
  REP(i, n) {
    bool foi = false;
    REP(j, n) {
      if (used[j]) continue;
      if (w[j] > v[i]) {
        used[j] = true;
        foi = true;
        res++;
        break;
      }
    }
    if (!foi) {
      break;
    }
  }
  return n-res;
}

int calcula1() {
  int i = n-1;
  int res = 0;
  for (int j = n-1; j >= 0; j--) {
    if (w[j] > v[i]) {
      res++;
    }
    else {
      i--;
    }
  }
  return n - res;
}

int main() {
	int t;
  scanf("%d", &t);
  REP(k, t) {
    scanf("%d", &n);
    REP(i, n) scanf("%lf", &v[i]);
    REP(i, n) scanf("%lf", &w[i]);
    sort(v, v+n);
    sort(w, w+n);
    int a = calcula1();
    int b = calcula2();
    printf("Case #%d: %d %d\n", k+1, a, b);
  }
  return 0;
}