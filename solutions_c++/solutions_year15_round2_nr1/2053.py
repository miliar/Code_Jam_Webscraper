#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
const double PI = acos(-1);
const double EPS = 1e-7;

#define PB push_back
#define MP make_pair
#define FOR(_i, _from, _to) for (int (_i) = (_from), (_batas) = (_to); (_i) <= (_batas); (_i)++)
#define REP(_i, _n) for (int (_i) = 0, (_batas) = (_n); (_i) < (_batas); (_i)++)
#define SZ(_x) ((int)(_x).size())

const int MAX_N = 1000000;
int tc;
int memo[MAX_N + 5];

int rev(int n) {
  int ret = 0;
  if (n == 0) return 0;
  while(n > 0) {
    ret = ret*10 + (n%10);
    n /= 10;
  }
  return ret;
}

int f(int n) {
  int &ret = memo[n];
  if (ret != -1) return ret;
  if (n == 1) ret = 1;
  else {
    ret = 1 + f(n-1);
    if (((n % 10) != 0) ) {
      int r = rev(n);
      if (r < n) ret = min(ret, 1 + f(r));
    }
  }
  return ret;
}

void solve() {
  int N;
  scanf("%d", &N);
  printf("Case #%d: %d\n", tc, f(N));
}

void initDP() {
  memset(memo, -1, sizeof memo);
  
  for (int i = 1; i <= MAX_N; i++) {
    f(i);
  }
}

int main() {
  initDP();
  //for(int i = 1; i <= MAX_N; i++) printf("%d\n", f(i));
  
  int T;
  scanf("%d", &T);
  for (tc = 1; tc <= T; tc++) solve();
	return 0;
}
