#include <cstdio>

void solve() {
  double cost, factory, cookies;
  scanf("%lf %lf %lf", &cost, &factory, &cookies);

  double time = 0;
  double rate = 2;
  double best = cookies / rate;
  for (int i = 1; i < 200 * 1005; i++) {
    time += cost / rate;
    rate += factory;

    double test = time + cookies / rate;
    if (best > test)
      best = test;
  }

  printf("%.7f\n", best);
}

int main() {
  int n;
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    printf("Case #%d: ", i+1);
    solve();
  }

  return 0;
}
