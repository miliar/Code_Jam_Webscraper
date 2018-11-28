#include <cstdio>

using namespace std;

typedef long long LL;

#define POW2(a) ((1LL) << (a))

void input(void);
void solve(void);
LL bestRank(LL x);
LL worstRank(LL x);

LL n, p;
int case_cnt = 1;

int main(void) {
  int t;
  scanf("%d", &t);
  while (t--) {
    input();
    solve();
  }
  return 0;
}

void input(void) {
  scanf("%lld %lld", &n, &p);
}

void solve(void) {
  LL left = 1;
  LL right = POW2(n);
  LL res1 = -1;
  while (left <= right) {
    LL mid = (left + right) / 2;
    if (worstRank(mid) <= p) {
      res1 = mid;
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  left = 1;
  right = POW2(n);
  LL res2 = -1;
  while (left <= right) {
    LL mid = (left + right) / 2;
    if (bestRank(mid) <= p) {
      res2 = mid;
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  printf("Case #%d: %lld %lld\n", case_cnt++, res1 - 1, res2 - 1);
}

LL bestRank(LL x) {
  LL N = POW2(n);
  LL a = x - 1;
  LL b = N - x;
  while (b > 0) {
    a = (a + 1) / 2;
    b = (b - 1) / 2;
  }
  return a + 1;
}

LL worstRank(LL x) {
  LL N = POW2(n);
  LL a = x - 1;
  LL b = N - x;
  while (a > 0) {
    a = (a - 1) / 2;
    b = (b + 1) / 2;
  }
  return N - (b + 1) + 1;
}

