#include <cstdio>
#include <vector>

using namespace std;

typedef long long LL;

static const LL N = 1e8;
bool nprime[N+1];
vector<LL> factor;
int n, j;
char bs[50];

void sieve() {
  nprime[0] = nprime[1] = false;
  for (LL i = 2; i * i <= N; ++i) {
    if (nprime[i]) continue;
    for (LL k = i * i; k <= N; k += i) {
      nprime[k] = true;
    }
  }
  for (LL i = 2; i <= N; ++i) {
    if (!nprime[i]) {
      factor.push_back(i);
    }
  }
}

LL fact(const LL& num) {
  for (auto &f : factor) {
    if (f * f > num)
      return -1;
    if (num % f == 0)
      return f;
  }
  return -1;
}

LL base(LL msk, const LL& b) {
  LL res = 0L, m = 1L;
  while (msk) {
    if (msk & 0x1) {
      res += m;
    }
    msk >>= 1;
    m *= b;
  }
  return res;
}

vector<LL> check(const LL& msk, bool *status) {
  vector<LL> res;
  for (int b = 2; b <= 10; ++b) {
    LL f = fact(base(msk, b));
    if (f == -1) {
      *status = false;
      return res;
    }
    res.push_back(f);
  }
  return res;
}

void format(const LL &num) {
  for (int i = 0; i < n; ++i) {
    if (num & (1 << i)) {
      bs[n - 1 - i] = '1';
    } else {
      bs[n - 1 - i] = '0';
    }
  }
  bs[n] = '\0';
}

void solve() {
  LL bnd = (1 << n) - 1;
  LL cnt = 0;
  for (LL i = 1; i <= bnd && cnt < j; ++i) {
    if ((i & 1) && (i & (1 << (n-1)))) {  
      bool s = true;
      vector<LL> vec = check(i, &s);
      if (s) {
        format(i);
        printf("%s", bs);
        for (auto &iv : vec) {
          printf(" %lld", iv);
        }
        printf("\n");
        ++cnt;
      }
    }
  }
}

int main() {
  sieve();
  int t;
  scanf("%d", &t);
  for (int i = 1; i <= t; ++i) {
    scanf("%d%d", &n, &j);
    printf("Case #%d:\n", i);
    solve();
  }
  return 0;
}