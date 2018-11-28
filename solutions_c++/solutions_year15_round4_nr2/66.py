#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

#define mset(a, v) memset(a, v, sizeof(a));
#define mset0(a) mset(a, 0);

void read() { }
template<typename... T> void read(int &h, T &... t) {
  scanf("%d", &h); read(t...);
}
template<typename... T> void read(LL &h, T &... t) {
  scanf("%lld", &h); read(t...);
}
template<typename... T> void read(double &h, T &... t) {
  scanf("%lf", &h); read(t...);
}

const int maxint = 0x7f7f7f7f;
const double eps = 1e-10, pi = acos(-1.0);

const int maxN = 111 + 22;
int n;
double V, T, rate[maxN], t[maxN];

double dblcmp(double x) {
  return x < -eps ? -1 : x > eps;
}

bool check(double mid) {
  vector<pair<double, double>> v;
  for (int i = 1; i <= n; ++i) {
    v.push_back(make_pair(t[i], mid * rate[i]));
  }
  sort(v.begin(), v.end());
  double amount = 0;
  for (int i = 0; i < n; ++i) {
    amount += v[i].second;
  }
  if (dblcmp(amount - V) < 0) return false;
  double mini = 0, maxi = 0, remain = V;
  for (int i = 0; i < n; ++i) {
    mini += min(remain, v[i].second) * v[i].first;
    remain -= min(remain, v[i].second);
  }
  reverse(v.begin(), v.end());
  remain = V;
  for (int i = 0; i < n; ++i) {
    maxi += min(remain, v[i].second) * v[i].first;
    remain -= min(remain, v[i].second);
  }
  mini /= V; maxi /= V;
  return dblcmp(T - mini) >= 0 && dblcmp(T - maxi) <= 0;
}

double solve() {
  double lo = 0, hi = 1e15, mid;
  bool found = false;
  for (int tt = 0; tt < 100; ++tt) {
    mid = (lo + hi) / 2;
    if (check(mid)) {
      hi = mid;
      found = true;
    } else lo = mid;
  }
  if (found) return lo;
  return -1;
}

int main() {
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);
  int tests;
  read(tests);
  for (int tt = 1; tt <= tests; ++tt) {
    read(n, V, T);
    for (int i = 1; i <= n; ++i) {
      read(rate[i], t[i]);
    }
    printf("Case #%d: ", tt);
    double a = solve();
    if (a == -1) puts("IMPOSSIBLE");
    else printf("%.10f\n", a);
    clog << tt << endl;
  }
  return 0;
}
