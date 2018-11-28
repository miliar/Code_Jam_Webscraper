#include <cstdio>
#include <algorithm>
#include <map>

using namespace std;

const int MAXN = 155;
const int MAXL = 44;

const int inf = 1 << 30;
const int HALF = 20;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<long long, long long> pll;
const int P1 = 1E9 + 7;
const int P2 = 1E9 + 9;

int T;
int N, L;

char str[MAXL];
ll ar[MAXN];
ll ar2[MAXN];
ll tmp[MAXN];

ull hsh() {
  sort(tmp, tmp + N);
  ull h1 = 1;
  for(int i = 0; i < N; ++i) {
    h1 = h1 * P1 + tmp[i];
  }
  return h1;
}

int go() {
  map<ull, int> vis;
  scanf("%d %d", &N, &L);
  for(int i = 0; i < N; ++i) {
    scanf("%s", str);
    ar[i] = 0;
    for(int j = 0; j < L; ++j) {
      ar[i] = 2 * ar[i] + str[j] - '0';
    }
  }

  for(int i = 0; i < N; ++i) {
    scanf("%s", str);
    ar2[i] = 0;
    for(int j = 0; j < L; ++j) {
      ar2[i] = 2 * ar2[i] + str[j] - '0';
    }
  }


  int up = min(HALF, L);
  for(int i = 0; i < (1 << up); ++i) {
    int cnt = 0;
    for(int j = 0; j < up; ++j) {
      if ((i >> j) & 1) ++cnt;
    }
    for(int j = 0; j < N; ++j) {
      tmp[j] = ar[j] ^ i;
    }
    int &x = vis[hsh()];
    if (!x) x = cnt + 1;
    else x = min(x, cnt + 1);
  }

  int ret = inf;
  for(ll i = 0; i < (1 << (L - up)); ++i) {
    int cnt = 0;
    for(int j = 0; j < L - up; ++j) {
      if ((i >> j) & 1) ++cnt;
    }
    for(int j = 0; j < N; ++j) {
      tmp[j] = ar2[j] ^ (i << up);
    }

    int x = vis[hsh()];
    if (x) {
      int ans = x - 1 + cnt;
      if (ans < ret) ret = ans;
    }
  }

  if (ret == inf) ret = -1;
  return ret;
}

int main() {
  scanf("%d", &T);
  for(int t = 1; t <= T; ++t) {
    printf("Case #%d: ", t);
    int ans = go();
    if (ans == -1) printf("NOT POSSIBLE\n");
    else printf("%d\n", ans);
  }
  return 0;
}
