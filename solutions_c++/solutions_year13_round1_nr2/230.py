#include <iostream>
using namespace std;
const int N = 10000;
const int RR = (1 << 14);
int a[N];
int n;
int next[N];
int tr[RR * 2];
void Update(int v, int value) {
  while (v) {
    if (tr[v] < value) tr[v] = value;
    v /= 2;
  }
}

int Find(int value, int R) {
  int v = 1;
  while (v < R) {
    if (tr[v * 2] > value) v *= 2;
    else v = v * 2 + 1;
  }
  return v - R;
}
int main() {
  int tc;
  long long ne, nr;
  scanf("%d", &tc);
  for (int cas=1; cas <= tc; ++cas) {
    scanf("%lld%lld%d", &ne, &nr, &n);
    for (int i = 0; i < n; ++i) scanf("%d", &a[i]);
    long long cur = ne;
    long long ans = 0;

    int R = 1;
    while (R < n) R *= 2;
    memset(tr, 0, sizeof(int) * R * 2);
    for (int i = n - 1; i >= 0; --i) {
      if (tr[1] > a[i]) {
        next[i] = Find(a[i], R);
      } else {
        next[i] = i;
      }
      Update(i + R, a[i]);
    }
    if (nr > ne) nr = ne;
    for (int i = 0; i < n; ++i) {
      if (next[i] == i) {
        ans += cur * a[i];
        cur = 0;
      } else {
        long long x = std::min(std::max( cur + (next[i] - i) * nr - ne, (long long)0), cur);
        cur -= x;
        ans += x * a[i];
      }
      cur += nr;
    }
    printf("Case #%d: %lld\n", cas, ans);
  }
  return 0;
}
